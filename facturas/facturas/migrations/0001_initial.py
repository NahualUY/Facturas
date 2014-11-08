# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero', models.IntegerField(serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(max_digits=8, decimal_places=2)),
                ('esta_paga', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(related_name='facturas', on_delete=django.db.models.deletion.PROTECT, to='facturas.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='factura',
            name='producto',
            field=models.ForeignKey(related_name='facturas', on_delete=django.db.models.deletion.PROTECT, to='facturas.Producto'),
            preserve_default=True,
        ),
    ]
