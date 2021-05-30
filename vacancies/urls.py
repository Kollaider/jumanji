

from django.urls import path
from vacancies import views

urlpatterns = [
    path('', views.ListAllVacanciesView.as_view()),
    path('<int:vacancy_id>', views.VacancyView.as_view()),
    path('cat/<str:specialty>', views.ListSpecialtyView.as_view()),

]
