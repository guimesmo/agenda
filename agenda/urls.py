from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'agenda.views.home', name='home'),

    # event api
    url(r'^next_events/$', 'schedule.views.next_events', name='next_events'),
    url(r'^done_events/$', 'schedule.views.done_events', name='done_events'),
    url(r'^delayed_events/$', 'schedule.views.delayed_events',
        name='delayed_events'),
    url(r'^finish_event/(?P<event_id>\d+)$', 'schedule.views.finish_event',
        name='finish_event'),
    url(r'^update_events/$', 'schedule.views.update_events',
        name='update_events'),

    # event actions
    url(r'^event/$', 'schedule.views.event'),

    # account actions
    url(r'^accounts/login/$', 'accounts.views.login_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout_view'),
    url(r'^accounts/register/$', 'accounts.views.register_user'),

    # django admin
    url(r'^admin/', include(admin.site.urls)
    ),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
