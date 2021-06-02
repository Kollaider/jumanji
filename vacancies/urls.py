

from django.urls import path
from vacancies import views

urlpatterns = [
    path('', views.ListVacanciesView.as_view()),
    path('<int:pk>', views.DetailVacancyView.as_view()),
    path('cat/<str:specialty>', views.ListSpecialtyView.as_view()),

]
