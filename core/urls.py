from django.urls import path
from . import views



urlpatterns = [
    path('Mood/', views.MoodView.as_view(), name='Mood-all'),
    path('<int:user_id>', views.HappyPlacesView, name='HappyPlacesView'),
    path('user/<int:userID>', views.stats, name='stats'),
    #path('stats/<int:user_id>', stats, name="stats"),
]