from django.urls import path
from .views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
    path('users/', CreateUserView.as_view(), name='user_create'),
]
