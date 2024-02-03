from django.urls import path
from .views import (
                    cantact_view,
)

app_name = 'main'

urlpatterns = [
    path('cantact/', cantact_view, name='cantact')
]