# Generated by Django 4.1.2 on 2022-10-30 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0028_alter_category_detail_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_detail',
            old_name='title',
            new_name='ti',
        ),
    ]
