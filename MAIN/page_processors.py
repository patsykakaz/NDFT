#-*- coding: utf-8 -*-

# from django import forms
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
from mezzanine.pages.page_processors import processor_for
from .models import *
# from mezzanine.blog.models import BlogPost

# from mezzanine.core.request import current_request

@processor_for("/")
def processor_projet(request, page):
    random_products = Product.objects.all().order_by('?')[:16]
    bandit_products = Product.objects.exclude(pk__in=random_products)
    # last_blog = BlogPost.objects.last()
    # print len(bandit_products)
    return locals()

@processor_for(Category)
def processor_projet(request, page):
    category = targetCat = Category.objects.get(pk=page.pk)
    try: 
        products = Product.objects.filter(cat_product=category).order_by('?')[:32]
    except:
        pass
    return locals()

@processor_for(Product)
def processor_projet(request, page):
    product = Product.objects.get(pk=page.pk)
    targetCat = product.cat_product
    if "Plist" in request.session and str(product.pk) in request.session['Plist']:
        wished = True
    try: 
        related_products = Product.objects.filter(cat_product=product.cat_product).exclude(pk=product.pk).order_by('?')[:4]
    except:
        pass
    if "Plist" in request.session and product.pk in request.session['Plist']:
            addToken = True
    return locals()


