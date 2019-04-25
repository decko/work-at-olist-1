from django.urls import path

from .views import Return200Ok

app_name = 'core'
urlpatterns = [
    path('', Return200Ok, name='index'),
    path('api/v1/', Return200Ok, name='api'),
    path('api/v1/calls/', Return200Ok, name='calls'),
]
