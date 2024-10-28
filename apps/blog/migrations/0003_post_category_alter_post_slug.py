# Generated by Django 5.1.2 on 2024-10-19 16:12

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=mptt.fields.TreeForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
