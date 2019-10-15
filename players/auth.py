from django.contrib.auth.models import User
from players.models import Profile


class AuthBackend:
    def authenticate(self, request, secret=None, **kwargs):
        try:
            profile = Profile.objects.get(secret=secret)
            user = profile.user

            if not user.is_superuser:
                return None

            print('Found user with secret', user)
            return user
        except Exception as err:
            print('cannot authenticate with secret...', err)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
