from django.urls import path

from .views import Return200Ok

app_name = 'api'
urlpatterns = [
    path('', Return200Ok, name='root'),
    path('calls/', Return200Ok, name='calls'),
]
