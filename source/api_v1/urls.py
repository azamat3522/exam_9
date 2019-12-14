from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import LogoutView



app_name = 'api_v1'

router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),

]