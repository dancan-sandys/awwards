# Generated by Django 3.1.2 on 2020-10-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awward', '0002_auto_20201024_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.CharField(max_length=30),
        ),
    ]
