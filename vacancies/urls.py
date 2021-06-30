
from django.urls import path
from vacancies import views


urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    # Вакансии
    path('vacancies/', views.ListVacanciesView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>', views.DetailVacancyView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:specialty>', views.ListSpecialtyView.as_view(), name='specialization'),
    # Компании
    path('companies/<int:pk>', views.DetailCompanyView.as_view(), name='company'),
]
