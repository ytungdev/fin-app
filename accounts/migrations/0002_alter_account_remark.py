# Generated by Django 4.1.7 on 2023-03-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='remark',
            field=models.CharField(max_length=255, null=True),
        ),
    ]