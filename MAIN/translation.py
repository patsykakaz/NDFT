#-*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import *

class TranslatedCategory(TranslationOptions):
    fields = ("presentation_parrain",)

class TranslatedProduct(TranslationOptions):
    fields = ('productName','baseline','presentation_product','discount','presentation_sup',)

translator.register(Category, TranslatedCategory)
translator.register(Product, TranslatedProduct)