# Generated by Django 4.1.7 on 2023-04-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashrecord',
            name='remark',
        ),
    ]