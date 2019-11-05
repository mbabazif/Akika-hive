# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-04 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_name', models.CharField(max_length=60)),
                ('academic_location', models.CharField(max_length=60)),
                ('academic_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_founder', models.CharField(max_length=60)),
                ('business_name', models.CharField(max_length=60)),
                ('business_location', models.CharField(max_length=30)),
                ('business_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_founder', models.CharField(max_length=60)),
                ('enterprise_name', models.CharField(max_length=60)),
                ('enterprise_location', models.CharField(max_length=30)),
                ('entrprise_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer_names', models.CharField(max_length=60)),
                ('project_name', models.CharField(max_length=60)),
                ('freelancer_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=60)),
                ('institution_location', models.CharField(max_length=60)),
                ('institution_adress', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('education_level', models.CharField(max_length=120)),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
