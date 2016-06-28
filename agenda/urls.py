from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'agenda.views.home', name='home'),
    url(r'^next_events/$', 'agenda.views.next_events', name='next_events'),
    url(r'^done_events/$', 'agenda.views.done_events', name='done_events'),
    url(r'^delayed_events/$', 'agenda.views.delayed_events',
        name='delayed_events'),
    url(r'^finish_event/(?P<event_id>\d+)$', 'agenda.views.finish_event',
        name='finish_event'),
    url(r'^event/$', 'agenda.views.event', name='home'),
    url(r'^admin/', include(admin.site.urls)
    ),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
