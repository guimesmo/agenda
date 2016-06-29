# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "username",)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count():
            raise forms.ValidationError(
                "Já existe um usuário com este email")
        return email