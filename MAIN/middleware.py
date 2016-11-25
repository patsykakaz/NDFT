#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.deprecation import MiddlewareMixin

from mezzanine.conf import settings
from models import *
from mezzanine.blog.models import BlogPost


class MenuMiddleware(object):

    def process_template_response(self, request, response):
        print 'process template response'
        # forbidden_domain = "lalettre"
        # if not request.user.is_authenticated() and not "admin/" in request.path and not "/user/" in request.path :
        #     return HttpResponseRedirect('/user/login/?next='+request.path)
        # else:
        #     print "request.user.is_authenticated = {}".format(request.user.is_authenticated())
        all_categories = Category.objects.all().order_by('-order')
        print all_categories
        last_blog = BlogPost.objects.last()
        response.context_data['all_categories'] = all_categories
        response.context_data['last_blog'] = last_blog
        return response






