from django import forms
from django.forms import CharField, TextInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class CustomAdminLoginForm(AuthenticationForm):

    secret = CharField(
        max_length=6,
        strip=False,
        label="SECRET",
        required=False,
        widget=TextInput(attrs={'autofocus': True}),
    )

    error_messages = {
        'invalid_login': "Please enter a correct secret or user and password",
    }

    def clean(self):
        secret = self.cleaned_data.get('secret')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(
            secret=secret,
            username=username,
            password=password,
            backend='players.auth.AuthBackend')

        if self.user_cache is None:
            raise self.get_invalid_login_error()

        self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'secret': 'invaid secret'},
        )
