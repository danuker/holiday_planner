from django.conf.urls import patterns, include, url
from django.contrib import admin
from holiday_planner.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),

    url(r'^my_holidays/$', my_holidays),
    url(r'^holidays/([a-zA-Z][a-zA-Z0-9_]*)/$', holidays),
    url(r'^employees/$', list_employees),
)
