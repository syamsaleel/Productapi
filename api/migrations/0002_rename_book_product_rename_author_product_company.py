# Generated by Django 4.2.3 on 2023-07-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='Company',
        ),
    ]
