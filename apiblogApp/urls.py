from django.urls import path
from .views import PostView

urlpatterns = [
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/<int:id>', PostView.as_view(), name='post'),
]