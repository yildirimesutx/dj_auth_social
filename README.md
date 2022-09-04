# Django Google Authentication using django-allauth

- pip install django-allauth

```
AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]
```

```
INSTALLED_APPS = [

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

```

```
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```


python manage.py migrate




- kaynakca
   - https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8

  - https://github.com/wagnerdelima/drf-social-oauth2

  - https://django-allauth.readthedocs.io/en/latest/installation.html

  - https://www.youtube.com/watch?v=NG48CLLsb1A&ab_channel=JustDjangohttps://www.youtube.com/watch?v=NG48CLLsb1A&ab_channel=JustDjango

  - https://django-allauth.readthedocs.io/en/latest/installation.html