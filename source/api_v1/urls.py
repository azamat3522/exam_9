from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v1.views import CommentViewSet, PhotoViewSet

app_name = 'api_v1'

router = DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'photo', PhotoViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
