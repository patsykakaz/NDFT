#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


category_fieldsets = deepcopy(PageAdmin.fieldsets)
category_fieldsets[0][1]["fields"].insert(-1, "illustration")
class CategoryAdmin(PageAdmin):
    fieldsets = category_fieldsets


product_fieldsets = deepcopy(PageAdmin.fieldsets)
product_fieldsets[0][1]["fields"].insert(-1, "category")
product_fieldsets[0][1]["fields"].insert(-1, "baseline")
product_fieldsets[0][1]["fields"].insert(-1, "presentation_product")
product_fieldsets[0][1]["fields"].insert(-1, "town")
product_fieldsets[0][1]["fields"].insert(-1, "productName")
product_fieldsets[0][1]["fields"].insert(-1, "price")
product_fieldsets[0][1]["fields"].insert(-1, "discount")
product_fieldsets[0][1]["fields"].insert(-1, "presentation_sup")
product_fieldsets[0][1]["fields"].insert(-1, "logo")
product_fieldsets[0][1]["fields"].insert(-1, "illustration")
product_fieldsets[0][1]["fields"].insert(-1, "illustration2")
product_fieldsets[0][1]["fields"].insert(-1, "illustration3")
product_fieldsets[0][1]["fields"].insert(-1, "illustration4")
product_fieldsets[0][1]["fields"].insert(-1, "team_pic")
product_fieldsets[0][1]["fields"].insert(-1, "mainLink")
product_fieldsets[0][1]["fields"].insert(-1, "website")
product_fieldsets[0][1]["fields"].insert(-1, "facebook")
product_fieldsets[0][1]["fields"].insert(-1, "twitter")
product_fieldsets[0][1]["fields"].insert(-1, "instagram")
class ProductAdmin(PageAdmin):
    fieldsets = product_fieldsets

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)







