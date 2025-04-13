from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('home',views.home,name='home'),
    path('activities/', views.activity_list, name='activity_list'),
    path('workouts/add/', views.add_workout, name='add_workout'),
    path('displaytimer/', views.display_timer, name='display_timer'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('dashboard/', views.dash_board,name='dash_board'),
    path('today/', views.display_today_workout, name='display_today_workout'),
    path('history/', views.history_view, name='history'),
    
]