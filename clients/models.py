from django.conf import settings
from django.db import models
from users.models import SALES


class Client(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'team': SALES}
    )
    status = models.BooleanField(default=False, verbose_name="Converted")

    def __str__(self):
        if self.status is False:
            stat = "PROSPECT"
        else:
            stat = "CONVERTED"
        return f"Client #{self.id} : {self.lastname}, {self.firstname} ({stat})"
