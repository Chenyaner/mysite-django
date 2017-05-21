from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello,current_datetime,hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$',hello),
	('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
