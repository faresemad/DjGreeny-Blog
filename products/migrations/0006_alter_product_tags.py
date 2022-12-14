# Generated by Django 4.1.3 on 2022-11-08 00:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('products', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name=False),
        ),
    ]
