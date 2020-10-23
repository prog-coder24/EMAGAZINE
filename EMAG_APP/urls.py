from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', home_view),
    path('add_event/', event_view),
    path('menu/', menu_view),
    path('achievement/', achievement_view),
    path('project/', project_view),
    path('welcome/', home_view),

]
