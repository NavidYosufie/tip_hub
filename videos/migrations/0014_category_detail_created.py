# Generated by Django 4.1.2 on 2022-10-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_remove_category_detail_category_category_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_detail',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]