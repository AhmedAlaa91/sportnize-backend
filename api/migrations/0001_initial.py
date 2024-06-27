# Generated by Django 5.0.6 on 2024-06-27 08:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('height', models.FloatField(blank=True, null=True, verbose_name='Height')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Weight')),
                ('height_unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Height Unit')),
                ('weight_unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Weight Unit')),
                ('age', models.SmallIntegerField(blank=True, null=True, verbose_name='Age')),
                ('school', models.CharField(blank=True, max_length=150, null=True, verbose_name='School')),
                ('sport', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sport')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Admin. ', null=True, verbose_name='Admin')),
                ('is_client', models.BooleanField(default=False, help_text='Designates whether this user should be treated as a Client. ', null=True, verbose_name='Client')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Client')], help_text='User Role in A system ', null=True, verbose_name='User Type')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', null=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', null=True, verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
