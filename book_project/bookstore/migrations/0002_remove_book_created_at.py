# Generated by Django 2.0.4 on 2018-04-21 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
    ]