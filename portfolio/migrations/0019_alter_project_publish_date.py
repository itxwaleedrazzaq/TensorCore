# Generated by Django 4.2.8 on 2024-02-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_project_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='publish_date',
            field=models.DateField(default=False),
        ),
    ]
