from django.conf.urls import url

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, RegistrationSuperUserAPIView
)

app_name = 'authentication'

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/superuser?$', RegistrationSuperUserAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
