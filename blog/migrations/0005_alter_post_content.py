# Generated by Django 5.1.2 on 2024-11-01 10:02

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
