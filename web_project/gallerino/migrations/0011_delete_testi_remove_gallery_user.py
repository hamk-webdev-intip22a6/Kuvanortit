# Generated by Django 5.0.3 on 2024-04-29 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallerino', '0010_testi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='testi',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='user',
        ),
    ]
