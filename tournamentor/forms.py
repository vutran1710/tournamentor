from django.forms import Form, CharField, ValidationError
from django.contrib.auth import authenticate


class UserLoginForm(Form):
    secret = CharField(label='Secret', max_length=6)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        secret = self.cleaned_data.get('secret')

        self.user_cache = authenticate(secret=secret, backend='players.auth.AuthBackend')

        if self.user_cache is None:
            raise self.get_invalid_login_error()

        self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'secret': 'invaid secret'},
        )

    def confirm_login_allowed(self, user):
        pass

    def get_user(self):
        return self.user_cache
