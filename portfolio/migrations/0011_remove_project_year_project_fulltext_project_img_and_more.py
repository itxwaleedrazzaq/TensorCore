# Generated by Django 4.2.8 on 2024-02-09 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_remove_project_fulltext_remove_project_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='year',
        ),
        migrations.AddField(
            model_name='project',
            name='fulltext',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='display_pic'),
        ),
        migrations.AddField(
            model_name='project',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
