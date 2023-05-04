from modeltranslation.translator import TranslationOptions, translator

from .models import Product


class ProductTranslation(TranslationOptions):
    fields = ('description',)

translator.register(Product, ProductTranslation)