# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 14:16
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0003_auto_20161107_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='presentation_product',
            field=mezzanine.core.fields.RichTextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='presentation_product_en',
            field=mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='presentation_product_fr',
            field=mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='presentation_sup',
            field=mezzanine.core.fields.RichTextField(blank=True, verbose_name='Presentation Start-up'),
        ),
        migrations.AlterField(
            model_name='product',
            name='presentation_sup_en',
            field=mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Presentation Start-up'),
        ),
        migrations.AlterField(
            model_name='product',
            name='presentation_sup_fr',
            field=mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Presentation Start-up'),
        ),
    ]
