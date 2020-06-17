from django.db import models
from common.models import TimeStampMixin


RESTAURANT = 'RE'
COFFEE = 'CO'
PUB = 'PU'
CELLAR = 'CE'
BAR_TYPE_CATEGORIES_CHOICES = [
    (RESTAURANT, 'Restaurant'),
    (COFFEE, 'Coffee'),
    (PUB, 'Pub'),
    (CELLAR, 'Wine Cellar'),
]


class Bar(TimeStampMixin):
    name = models.CharField("Bar name", max_length=128)
    bar_type = models.CharField('Bar type',
                                max_length=2,
                                choices=BAR_TYPE_CATEGORIES_CHOICES)
    zip_code = models.CharField(max_length=16,
                                blank=False,
                                null=False)
    readonly_fields = ('created_at', 'updated_at', )

    def __str__(self):
        return f'{self.name} - {self.bar_type}'
