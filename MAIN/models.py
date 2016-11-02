#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.utils.sites import current_site_id, current_request

class Product(Page,RichText):
    """
        title = company name
        richText = description
    """
    category = models.ManyToManyField('Category',blank=False)
    town = models.CharField(max_length=255)
    productName = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=255)
    logo = FileField(verbose_name=_("logo"),
        upload_to=upload_to("MAIN.Product.logo", "logo"),
        format="Image", max_length=255, null=True, blank=True)
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Product.illustration", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    illustration1 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    illustration2 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    illustration3 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    team = FileField(upload_to=upload_to("MAIN.Product.illustration", "team"),
        format="Image", max_length=255, null=True, blank=True)
    link = models.URLField()
    website = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    class Meta:
        verbose_name='PRODUIT'
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.in_menus = []
        try:
            self.parent = Page.objects.get(title='PRODUITS')
        except: 
            pass
        super(Product, self).save(*args, **kwargs)


class Category(Page):
    illustration = FileField(verbose_name=_("illustration"),
        upload_to=upload_to("MAIN.Category.illustration", "category"),
        format="Image", max_length=255, null=True, blank=True)




