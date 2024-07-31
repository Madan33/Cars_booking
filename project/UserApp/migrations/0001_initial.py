# Generated by Django 5.0.2 on 2024-03-05 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('user_mail', models.CharField(max_length=200)),
                ('user_pasw', models.CharField(max_length=100)),
                ('user_pno', models.CharField(max_length=100)),
                ('license_no', models.CharField(max_length=100)),
                ('status', models.CharField(default='Active', max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='UserProfilePic',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.userregmodel')),
            ],
            options={
                'db_table': 'Profile Pic',
            },
        ),
        migrations.CreateModel(
            name='LicenseImgModel',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('license_img', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.userregmodel')),
            ],
            options={
                'db_table': 'User License',
            },
        ),
    ]