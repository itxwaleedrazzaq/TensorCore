# Generated by Django 4.2.8 on 2024-02-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_remove_project_pkey_project_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='publish_date',
            field=models.DateField(default=False),
        ),
    ]
