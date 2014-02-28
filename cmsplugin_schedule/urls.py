
try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from .views import EventListView

urlpatterns = patterns('',
    url(r'^get-calendar-events/(?P<calendar_slug>[\.\w-]+)/$',
       EventListView.as_view(),
       name='get-calendar-events'),
)
