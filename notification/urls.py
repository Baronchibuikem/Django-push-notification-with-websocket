from django.urls import path

from notification import views

app_name = 'app_notification'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
]
  