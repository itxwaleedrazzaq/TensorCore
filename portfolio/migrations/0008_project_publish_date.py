# Generated by Django 4.2.8 on 2024-02-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_project_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
