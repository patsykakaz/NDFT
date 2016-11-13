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

def checkList(request,Plist=False):
    products = []
    if Plist:
        if 'plist' not in request.session:
            request.session['plist']=[]
        plist = request.session['plist']
        for item in Plist.split('-'):
            products.append(Product.objects.get(pk=item))
            if not item in plist:
                plist = plist + [item]
        if not products:
            products = False
        request.session['plist'] = plist

    return render(request,'pages/checklist.html',locals())





