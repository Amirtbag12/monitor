from django.urls import re_path
from django.conf import settings
from main import views as main
from usage import views as usage


urlpatterns = [
    re_path(r'^$', main.index, name='index'),
    re_path(r'^main/$', main.getall, name='main'),
    re_path(r'^info/uptime/$', usage.uptime, name='uptime'),
    re_path(r'^info/memory/$', usage.memusage, name='memusage'),
    re_path(r'^info/cpuusage/$', usage.cpuusage, name='cpuusage'),
    re_path(r'^info/getdisk/$', usage.getdisk, name='getdisk'),
    re_path(r'^info/getusers/$', usage.getusers, name='getusers'),
    re_path(r'^info/getips/$', usage.getips, name='getips'),
    re_path(r'^info/gettraffic/$', usage.gettraffic, name='gettraffic'),
    re_path(r'^info/proc/$', usage.getproc, name='getproc'),
    re_path(r'^info/getdiskio/$', usage.getdiskio, name='getdiskio'),
    re_path(r'^info/loadaverage/$', usage.loadaverage, name='loadaverage'),
    re_path(r'^info/platform/([\w\-\.]+)/$', usage.platform, name='platform'),
    re_path(r'^info/getcpus/([\w\-\.]+)/$', usage.getcpus, name='getcpus'),
    re_path(r'^info/getnetstat/$', usage.getnetstat, name='getnetstat'),
]
