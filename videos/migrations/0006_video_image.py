# Generated by Django 4.1.2 on 2022-10-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_remove_caregory_detil_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Videos/image'),
        ),
    ]
