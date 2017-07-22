# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0019_auto_20170715_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingMultiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focus', models.CharField(choices=[('warmup', 'Warmup'), ('technique', 'Technique'), ('kick', 'Kick'), ('sprint', 'Sprint'), ('mid-distance', 'Mid Distance'), ('distance', 'Distance'), ('race', 'Race'), ('cooldown', 'Cooldown')], max_length=15)),
                ('multiplier', models.IntegerField()),
                ('training_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TrainingModel')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='set',
            name='swimmers',
            field=models.ManyToManyField(blank=True, null=True, to='teams.Swimmer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(choices=[('50 free', '50 Freestyle'), ('100 free', '100 Freestyle'), ('200 free', '200 Freestyle'), ('500 free', '500 Freestyle'), ('1000 free', '1000 Freestyle'), ('50 back', '50 Backstroke'), ('100 back', '100 Backstroke'), ('200 back', '200 Backstroke'), ('50 breast', '50 Breaststroke'), ('100 breast', '100 Breaststroke'), ('200 breast', '200 Breaststroke'), ('50 fly', '50 Butterfly'), ('100 fly', '100 Butterfly'), ('200 fly', '200 Butterfly'), ('base free', 'Freestyle Base'), ('base back', 'Backstroke Base'), ('base breaset', 'Breaststroke Base'), ('base fly', 'Butterfly Base')], max_length=10),
        ),
    ]
