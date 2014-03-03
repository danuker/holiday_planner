import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

from holiday_planner.models import Employee, Vacation

TEMPLATE_PATH = 'holiday_planner/templates'


def home(request):
    t = get_template('home.html')
    return HttpResponse(t.render(Context()))


def holidays(request, username):
    vacations = Vacation.objects.all()

    t = get_template('holidays_as_employee.html')
    c = Context({'username': username,
                 'holidays': vacations
                 })
    return HttpResponse(t.render(c))


def list_employees(request):
    employees = [{'name': e.user.first_name + ' ' + e.user.last_name,
                  'vacation_days': e.vacation_days}
                 for e in Employee.objects.all()]

    t = get_template('list_employees.html')
    return HttpResponse(t.render(Context({'employees': employees})))
