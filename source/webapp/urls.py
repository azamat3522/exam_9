from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from webapp.views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]