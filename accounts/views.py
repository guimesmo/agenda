#-*- coding: utf-8 -*-
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView


from django.views.generic.edit import CreateView
from .forms import UserRegisterForm


class LoginView(FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'accounts/login.html'
    success_url = '/'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        The user has provided valid credentials (this was checked in
        AuthenticationForm.is_valid()). So now we can log him in.
        """
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def set_test_cookie(self):
        self.request.session.set_test_cookie()

    def check_and_delete_test_cookie(self):
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def get(self, request, *args, **kwargs):
        """
        Same as django.views.generic.edit.ProcessFormView.get(), but adds
        test cookie stuff
        """
        self.set_test_cookie()
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Same as django.views.generic.edit.ProcessFormView.post(),
        but adds test cookie stuff
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.check_and_delete_test_cookie()
            return self.form_valid(form)
        else:
            self.set_test_cookie()
            return self.form_invalid(form)


class RegisterUserView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    success_message = "Conta criada! Bem vindo à sua agenda!"

    def form_valid(self, form):
        form.save()
        authenticated_user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'])

        login(self.request, authenticated_user)
        return HttpResponseRedirect(self.success_url)

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login")
    # Redirect to a success page.


login_view = LoginView.as_view()
register_user = RegisterUserView.as_view()