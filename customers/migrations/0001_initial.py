# Generated by Django 4.2.13 on 2024-06-17 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=255, unique=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'status_user',
                'verbose_name_plural': 'status_users',
                'db_table': 'accounts_status_users',
            },
        ),
        migrations.CreateModel(
            name='TypeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=255, unique=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'type_user',
                'verbose_name_plural': 'type_users',
                'db_table': 'accounts_type_users',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('ci', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('blocking_time', models.DateTimeField(blank=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_due_password', models.DateTimeField(default=datetime.datetime(2024, 12, 17, 17, 56, 25, 206988))),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.statususer')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.typeuser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'accounts_users',
            },
        ),
    ]
