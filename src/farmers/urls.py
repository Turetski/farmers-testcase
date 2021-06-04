from django.urls import path
from .views import *


urlpatterns = [
    path('api/customers', CustomerListView.as_view()),
    path('api/farms', FarmListView.as_view()),
]