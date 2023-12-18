from django.urls import path
from .views import home, result

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
]