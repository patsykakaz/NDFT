#-*- coding: utf-8 -*-

from .models import *


def categories(request):
    return {
        'all_categories': Category.objects.all()
    }