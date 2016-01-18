# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='fz_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56, verbose_name='title')),
                ('content', models.TextField(verbose_name='contents')),
                ('tags', models.CharField(blank=True, max_length=1023, verbose_name='label')),
                ('publish_date', models.DateTimeField()),
                ('ispublished', models.BooleanField()),
                ('commentcount', models.IntegerField(blank=True)),
                ('readcount', models.IntegerField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='fz_classic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('articecount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fz_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('commentator', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.fz_Article')),
            ],
        ),
        migrations.AddField(
            model_name='fz_article',
            name='classic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.fz_classic'),
        ),
    ]