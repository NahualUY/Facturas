from django.core.management.base import BaseCommand
import facturas.settings as settings
import _mysql


class Command(BaseCommand):
    args = '<root_pwd>'
    pwd = ''
    pwd_cmd = ''

    def handle(self, *args, **options):
        if len(args) > 0:
            self.pwd = args[0]
            self.pwd_cmd = ' -p%s' % self.pwd_cmd

        db = _mysql.connect(host='127.0.0.1', user='root', passwd=self.pwd)
        try:
            db.query("DROP USER '%s'@'localhost'" % settings.local_settings['super_username'])
        except:
            print 'Error al borrar el usuario super'

        for user in [u for u in settings.local_settings['users'] if u != settings.local_settings['source_user']]:
            try:
                db.query("DROP USER '%s'@'localhost'" % user)
            except:
                print 'Error al borrar el usuario %s' % user
            try:
                db.query("DROP DATABASE facturas_%s" % user)
            except:
                print 'Error al borrar la base de datos de %s' % user

