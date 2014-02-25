import datetime

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=100)
    vacation_days = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __unicode__(self):
        return str([self.name,
                    self.vacation_days,
                    'Admin' if self.is_admin else 'User'])


class Vacation(models.Model):
    employee = models.ForeignKey(Employee)
    vac_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __unicode__(self):
        return str([self.employee.name,
                    self.vac_date,
                    'Approved' if self.is_approved else 'Requested'])

    def is_soon(self):
        return (timezone.now() <
                timezone.make_aware(self.vac_date, 'Europe/Bucharest') <
                timezone.now() - datetime.timedelta(days=7))
