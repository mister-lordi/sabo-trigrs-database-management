# Generated by Django 3.1.2 on 2020-11-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigrs', '0004_remove_datatrigrsdetail_path_to_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatrigrsdetail',
            name='file_upload_status',
            field=models.TextField(default=None),
        ),
    ]
