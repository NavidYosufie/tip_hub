# Generated by Django 4.1.2 on 2022-10-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0031_alter_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_detail',
            old_name='title',
            new_name='ti',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='videos.category_detail'),
        ),
    ]
