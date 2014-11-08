from django.core.management.base import BaseCommand
import facturas.settings as settings
import _mysql
import subprocess


class Command(BaseCommand):
    args = '<root_pwd>'
    pwd = ''
    pwd_cmd = ''

    def handle(self, *args, **options):
        if len(args) > 0:
            self.pwd = args[0]
            self.pwd_cmd = ' -p%s' % self.pwd_cmd

        db = _mysql.connect(host='127.0.0.1', user='root', passwd=self.pwd)

        # generate dump
        filename = settings.local_settings['tmp_path'] + 'source.sql'
        f = open(filename, 'w')
        self.execute_bash('%smysqldump -u root%s facturas_%s' % (
            settings.local_settings['mysql_bin_path'], self.pwd_cmd, settings.local_settings['source_user']), f)
        f.close()

        # Check if the super user exists
        try:
            db.query("DROP USER '%s'@'localhost'" % settings.local_settings['super_username'])
        except:
            print 'Error al borrar el usuario super'
        try:
            db.query("GRANT USAGE ON *.* TO '%s'@'localhost' IDENTIFIED BY '%s';" % (settings.local_settings['super_username'], settings.local_settings['super_password']))
            db.query("GRANT ALL PRIVILEGES ON `facturas\_%s`.* TO '%s'@'localhost' WITH GRANT OPTION;" % (settings.local_settings['source_user'], settings.local_settings['super_username']))
        except:
            print 'No se pudo crear el usuario super'

        # Delete all these users from the database and their databases
        for user in [u for u in settings.local_settings['users'] if u != settings.local_settings['source_user']]:
            try:
                db.query("DROP USER '%s'@'localhost'" % user)
            except:
                print 'Error al borrar el usuario %s' % user

            try:
                db.query("DROP DATABASE facturas_%s" % user)
            except:
                print 'Error al borrar la base de datos de %s' % user

            db.query('CREATE DATABASE facturas_%s' % user)

            sql = """GRANT USAGE ON *.* TO '{0}'@'localhost' IDENTIFIED BY PASSWORD '*4B50912C29D6B4EE16B4FD1F940CAE837C350782';
                    GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES ON `facturas_{0}`.`facturas_factura` TO '{0}'@'localhost';
                    GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES ON `facturas_{0}`.`facturas_producto` TO '{0}'@'localhost';
                    GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES ON `facturas_{0}`.`facturas_cliente` TO '{0}'@'localhost';""".format(user)
            for part in [l for l in sql.split(';') if l != '']:
                db.query(part)

            f = open(filename, 'r')
            f.seek(0)
            self.execute_bash('%smysql -u root%s facturas_%s' % (
                settings.local_settings['mysql_bin_path'], self.pwd_cmd, user), in_file=f)
            f.close()

            print('%s terminado' % user)


    def execute_bash(self, command, out_file=None, in_file=None):
        sp = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE if out_file is None else out_file,
                              stderr=subprocess.PIPE, stdin=None if in_file is None else in_file)
        out, err = sp.communicate()
        if err:
            raise Exception(err)
        return out
