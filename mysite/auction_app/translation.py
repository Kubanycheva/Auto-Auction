from .models import Category, Brand, Model, Car
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand_name',)


@register(Model)
class ModelTranslationOptions(TranslationOptions):
    fields = ('model_name',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description', 'task',)






