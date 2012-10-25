from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/avs/', include('avsUI.freenas.urls')),
)
