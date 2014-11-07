# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(max_length=9, serialize=False, primary_key=True)),
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
                ('esta_paga', models.BooleanField()),
                ('cliente', models.ForeignKey(related_name='facturas', to='facturas.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
