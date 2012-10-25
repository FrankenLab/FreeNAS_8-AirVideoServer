from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('avsUI.freenas.views',
     url(r'^edit$', 'edit', name="avs_edit"),
     url(r'^treemenu-icon$', 'treemenu_icon', name="treemenu_icon"),
     url(r'^_s/treemenu$', 'treemenu', name="treemenu"),
     url(r'^_s/start$', 'start', name="start"),
     url(r'^_s/stop$', 'stop', name="stop"),
     url(r'^_s/status$', 'status', name="status"),
)
