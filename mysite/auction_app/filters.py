from django_filters import FilterSet
from .models import *


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
            'brand': ['exact'],
            'model': ['exact'],
            'fuel_type': ['exact'],
        }