# Generated by Django 3.2.7 on 2021-09-22 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adress',
            name='user',
        ),
    ]