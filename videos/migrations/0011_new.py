# Generated by Django 4.1.2 on 2022-10-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_category_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('bocy', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='Videos')),
            ],
        ),
    ]
