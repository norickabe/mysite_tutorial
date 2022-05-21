from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.top, name='top'),
    path('post/', views.post_list, name='post_list'),
]