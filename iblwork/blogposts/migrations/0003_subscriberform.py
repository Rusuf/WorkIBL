# Generated by Django 5.0.6 on 2024-05-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
