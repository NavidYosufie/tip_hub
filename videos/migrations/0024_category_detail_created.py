# Generated by Django 4.1.2 on 2022-10-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0023_alter_video_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_detail',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
