from django.urls import path
from .views import *

urlpatterns = [
    path('curso/',curso),
    path('misdatos/',mis_datos),
    path('habilidades/',habilidades_blandas),
    path('',inicio),
]
