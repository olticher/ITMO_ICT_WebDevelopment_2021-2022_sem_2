from django_filters import rest_framework as filters
from .models import *


class ToursPriceRangeFilter(filters.FilterSet):
    price = filters.RangeFilter()
    ordering = filters.OrderingFilter(
        fields=(
            ('date_from', 'price')
        )
    )

    class Meta:
        model = Tour
        fields = ['price']