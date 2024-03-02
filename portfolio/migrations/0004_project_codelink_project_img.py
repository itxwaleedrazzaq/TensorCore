# Generated by Django 4.2.8 on 2024-02-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='codelink',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(null=True, upload_to='display_pic'),
        ),
    ]