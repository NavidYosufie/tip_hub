# Generated by Django 4.1.2 on 2022-10-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0019_rename_detail_category_detail_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='videos.category'),
        ),
    ]