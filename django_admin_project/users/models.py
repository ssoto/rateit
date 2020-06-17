from django.db import models

from common.models import TimeStampMixin


class User(TimeStampMixin):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=16,
                                blank=False, null=False)

    def __str__(self):
        return self.first_name
