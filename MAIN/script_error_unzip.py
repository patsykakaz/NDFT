#-*- coding: utf-8 -*-

from MAIN.models import *

kk = Projet.objects.all()
liste_len = []

for k in kk:
    lookup_fields = [k.logo, k.illustration, k.illustration2, k.illustration3, k.illustration4, k.team_pic]
    for field in lookup_fields:
        # liste_len.append(len(field))
        if len(field.name) > 200:
            print k.title
            print field.name
            print len(field.name)
        # liste_len.append(len(field.name))