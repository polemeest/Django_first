from django.urls import path
from .views import *


urlpatterns = [
    path('', main),
    path('people/', people, name='secret_people'),
    path('<int:day>/', week_day_by_number),
    path('<str:day>/', week_day, name='what_day')
]
