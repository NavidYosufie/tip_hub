# Generated by Django 4.1.2 on 2022-10-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0030_rename_ti_category_detail_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='cat', to='videos.category_detail'),
        ),
    ]