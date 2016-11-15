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


def verification(request):
    all_sup = Product.objects.all()
    return render(request,'verification.html',locals())

def add2list(request,pk):
    product = Product.objects.get(pk=pk)
    if 'Plist' not in request.session:
        request.session['Plist'] = [pk]
    else: 
        request.session['¨Pist'] = request.session['plist'] + [pk]
    return render(request,'pages/product.html',locals())

def checklist(request,Plist=False):
    products = []
    if Plist:
        if 'Plist' not in request.session:
            request.session['Plist']=[]
        Plist = request.session['Plist']
        for item in Plist.split('-'):
            products.append(Product.objects.get(pk=item))
            if not item in Plist:
                Plist = Plist + [item]
        if not products:
            products = False
        request.session['Plist'] = Plist

    return render(request,'pages/checklist.html',locals())

def sharelist(request):
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
        request.session['Plist'] = Plist
    else: 
    # no product in the list
        pass
    shareURL = shareURL
    print shareURL
    return render(request,'pages/sharelist.html',locals())

def all(request):
    all_products = Product.objects.all()
    return render(request,'pages/index.html',locals())




