from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('', LoginRedirect.as_view(), name='login_redirect'),
] + default_urlpatterns(GoogleProvider)
