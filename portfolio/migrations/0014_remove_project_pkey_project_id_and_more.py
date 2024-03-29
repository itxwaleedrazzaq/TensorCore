# Generated by Django 4.2.8 on 2024-02-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_remove_project_id_project_pkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pkey',
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, default=4, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
