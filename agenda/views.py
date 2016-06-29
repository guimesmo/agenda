# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class MainPage(TemplateView):
    template_name = "index.html"


home = MainPage.as_view()

