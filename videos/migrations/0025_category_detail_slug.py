# Generated by Django 4.1.2 on 2022-10-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0024_category_detail_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_detail',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
