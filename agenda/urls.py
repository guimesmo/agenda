from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from schedule.views import EventsListSet

urlpatterns = patterns('',
    url(r'^$', 'agenda.views.home', name='home'),

    # event api
    url(r'events/$', EventsListSet.as_view()),

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
