# Generated by Django 5.0 on 2024-02-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_category_subscribers_delete_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postCategory',
            new_name='category',
        ),
    ]
