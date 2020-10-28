from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', home_view),
    path('menu/events/', event_view),
    path('menu/', menu_view),
    path('achievements/', achievement_view),
    path('projects/', project_view),
    path('welcome/', home_view),

]
