# Generated by Django 5.0.3 on 2024-04-28 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallerino', '0006_alter_post_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallerino.gallery'),
        ),
    ]
