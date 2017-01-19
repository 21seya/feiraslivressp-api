# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longi', models.CharField(blank=True, default='', max_length=15)),
                ('lat', models.CharField(blank=True, default='', max_length=15)),
                ('setcens', models.CharField(blank=True, default='', max_length=20)),
                ('areap', models.CharField(blank=True, default='', max_length=20)),
                ('coddist', models.IntegerField()),
                ('distrito', models.CharField(blank=True, default='', max_length=20)),
                ('codsubpref', models.IntegerField()),
                ('subprefe', models.CharField(blank=True, default='', max_length=40)),
                ('regiao5', models.CharField(blank=True, default='', max_length=20)),
                ('regiao8', models.CharField(blank=True, default='', max_length=20)),
                ('nome_feira', models.CharField(blank=True, default='', max_length=40)),
                ('registro', models.CharField(blank=True, default='', max_length=10)),
                ('logradouro', models.CharField(blank=True, default='', max_length=40)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(blank=True, default='', max_length=40)),
                ('referencia', models.CharField(blank=True, default='', max_length=40)),
            ],
        ),
    ]
