#-*- coding: utf-8 -*-

from __future__ import unicode_literals
# import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
# from django.contrib.auth import logout, login, authenticate, get_backends
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

from mezzanine.utils.urls import login_redirect, next_url
from mezzanine.pages.models import Page
from .models import *


def allProducts(request):
    all_products = Product.objects.all().order_by('?')
    return render(request,'pages/index.html',locals())

# WishList Functions
def flushlist(request):
    request.session.flush()
    return redirect('home')

def add2list(request,pk):
    product = Product.objects.get(pk=int(pk))
    if 'Plist' not in request.session:
        request.session['Plist'] = [pk]
    else:
        if not pk in request.session['Plist']:
            request.session['Plist'] += [pk]
    addToken = True
    return redirect(product)
    # return render(request,'pages/product.html',locals())

def removeFromList(request,pk):
    request.session['Plist'].remove(pk)
    rmToken = True
    request.session.modified = True
    return redirect('wishlist')

def wishlist(request):
    products = []
    shareURL = "noeldelafrenchtech.fr/checklist/"
    if 'Plist' in request.session:
    # some products in the list
        Plist = request.session['Plist']
        for item in Plist:
            products.append(Product.objects.get(pk=item))
            if not item in Plist:
                Plist = Plist + [item]
            shareURL += str(item)+"-"
        if not products:
            products = False
        alt_products = Product.objects.exclude(id__in=[element.pk for element in products])
        request.session['Plist'] = Plist
    else: 
    # no product in the list
        products = False
        alt_products = Product.objects.all().order_by('?')[:4]
        # print alt_products
    shareURL = shareURL
    return render(request,'pages/sharelist.html',locals())

def viewlist(request,Plist=False):
    products = []
    if Plist:
        # if 'Plist' not in request.session:
            # request.session['Plist']=[]
        # Plist = str(request.session['Plist'])
        for item in Plist.split('-'):
            # item = int(item)
            try: 
                products.append(Product.objects.get(pk=item))
            except: 
                pass
            # if not item in Plist:
                # Plist = Plist + [item]
        if not products:
            products = False
            alt_products = Product.objects.all().order_by('?')[:4]
        # request.session['Plist'] = Plist

    return render(request,'pages/sharelist.html',locals())
# ./ WishList functions 




