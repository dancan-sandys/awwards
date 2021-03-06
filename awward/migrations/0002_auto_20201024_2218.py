# Generated by Django 3.1.2 on 2020-10-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='yes', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='Description',
            field=models.TextField(),
        ),
    ]
