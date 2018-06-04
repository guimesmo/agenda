from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from schedule.views import EventsListSet, EventDetail

from agenda import views as agenda_views
from accounts import views as accounts_views


urlpatterns = [
               url(r'^$', agenda_views.home, name='home'),

               # event api
               url(r'events/$', EventsListSet.as_view()),
               url(r'events/(?P<pk>\d+)$', EventDetail.as_view()),

               # account actions
               url(r'^accounts/login/$', accounts_views.login_view),
               url(r'^accounts/logout/$', accounts_views.logout_view),
               url(r'^accounts/register/$', accounts_views.register_user),

               # django admin
               url(r'^admin/', admin.site.urls),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
