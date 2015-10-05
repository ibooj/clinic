# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor_name', models.CharField(verbose_name='ФИО доктора', max_length=100)),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(verbose_name='Время')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='День')),
                ('patient_name', models.CharField(verbose_name='ФИО', max_length=100)),
                ('doctor', models.ForeignKey(verbose_name='Доктор', to='clinic.Doctor')),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистратура',
            },
        ),
        migrations.AlterUniqueTogether(
            name='registry',
            unique_together=set([('time', 'date', 'patient_name')]),
        ),
    ]
