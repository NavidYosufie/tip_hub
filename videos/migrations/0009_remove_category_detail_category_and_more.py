# Generated by Django 4.1.2 on 2022-10-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_category_category_detail_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_detail',
            name='category',
        ),
        migrations.AddField(
            model_name='category_detail',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='videos.category'),
        ),
    ]
