from django.conf import settings
from django.db import models
from contracts.models import Contract
from users.models import SUPPORT


class Event(models.Model):
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        limit_choices_to={'status': True},
        related_name='event'
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'team': 3}
    )
    event_status = models.BooleanField(default=False, verbose_name="Completed")
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        name = f"{self.contract.client.lastname}, {self.contract.client.firstname}"
        date = self.event_date.strftime('%Y-%m-%d')
        if self.event_status is False:
            stat = "UPCOMING"
        else:
            stat = "COMPLETED"

        return f"Event #{self.id} : {name} | Date : {date} ({stat})"
