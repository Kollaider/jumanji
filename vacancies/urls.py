

from django.urls import path
from vacancies import views

urlpatterns = [
    path('', views.ListAllVacanciesView.as_view()),
    path('22', views.VacancyView.as_view()),
    path('cat/frontend', views.ListSpecialtyView.as_view()),

]
