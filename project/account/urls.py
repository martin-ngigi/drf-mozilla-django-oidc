from django.urls import path, include
from rest_framework import routers

# urls.py
from django.urls import path
from .views import OIDCLoginView, CustomLogoutView
from .views import MyOIDCAB, CustomLogoutView


urlpatterns = [
    path('user-infor/', OIDCLoginView.as_view(), name='oidc_user_infor'),
    #  path('user-infor/', MyOIDCAB, name='oidc_user_infor'),

    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
]
