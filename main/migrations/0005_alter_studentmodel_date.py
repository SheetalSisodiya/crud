# Generated by Django 5.1.4 on 2025-04-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_studentmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
