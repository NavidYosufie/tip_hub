# Generated by Django 4.1.2 on 2022-10-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_category_video_slug_alter_video_body_video_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caregory_detil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ManyToManyField(blank=True, null=True, to='videos.category')),
            ],
        ),
    ]
