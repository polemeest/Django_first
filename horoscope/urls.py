from django.urls import path
from . import views


urlpatterns = [
    path('', views.horoscope),
    path('date/', views.enter_date, name='enter_date'),
    path('type/', views.by_type, name='by_type'),
    path('type/<str:elem>/', views.sort_by_type, name='sort_by_type'),
    path('<int:num>', views.get_by_num, name='what_number'),
    path('<str:sign>/', views.get_zodiac, name='what_zodiac'),
    path('date/<int:month>/<int:day>', views.get_date, name='what_date')

]