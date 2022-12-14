# Generated by Django 4.1.2 on 2022-10-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_caregory_detil'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregory_detil',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='videos.category'),
        ),
        migrations.RemoveField(
            model_name='caregory_detil',
            name='title',
        ),
        migrations.AddField(
            model_name='caregory_detil',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
