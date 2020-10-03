from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', home_view),
    path('event/', event_view)
]
