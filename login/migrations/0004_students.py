# Generated by Django 3.0.8 on 2020-08-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200801_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
