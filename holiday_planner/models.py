import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate


class Employee(models.Model):
    user = models.OneToOneField(User)
    vacation_days = models.IntegerField(default=0)
    is_manager = models.BooleanField(default=False)

    def __unicode__(self):
        return str([self.user.username,
                    self.vacation_days,
                    'Manager' if self.is_manager else 'Regular'])


class Vacation(models.Model):
    employee = models.ForeignKey(Employee)
    vac_date = models.DateField()
    is_approved = models.BooleanField()

    def __unicode__(self):
        return str([self.employee.user.first_name + ' '
                    + self.employee.user.last_name,
                    self.vac_date,
                    'Approved' if self.is_approved else 'Requested'])

    @property
    def is_in_future(self):
        return (timezone.UTC() <
                timezone.make_aware(self.vac_date, 'UTC'))
