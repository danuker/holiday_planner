import datetime
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required

from holiday_planner.models import Employee, Vacation

TEMPLATE_PATH = 'holiday_planner/templates'


def home(request):

    if request.user.is_authenticated():
        redirect('/my_holidays/')

    t = get_template('home.html')
    return HttpResponse(t.render(Context()))


@login_required
def my_holidays(request):
    vacations = Vacation.objects.all()
    username = request.user.username

    t = get_template('holidays.html')
    c = Context({'username': username,
                 'holidays': vacations,
                 })
    return HttpResponse(t.render(c))


@permission_required('holiday_planner.manage')
def holidays(request, username):
    vacations = Vacation.objects.all()

    t = get_template('holidays.html')
    c = Context({'username': username,
                 'holidays': vacations,
                 })
    return HttpResponse(t.render(c))


@permission_required('holiday_planner.manage')
def list_employees(request):
    employees = [{'name': e.user.first_name + ' ' + e.user.last_name,
                  'vacation_days': e.vacation_days}
                 for e in Employee.objects.all()]

    t = get_template('list_employees.html')
    return HttpResponse(t.render(Context({'employees': employees})))
