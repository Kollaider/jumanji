

from django.urls import path
from vacancies import views

urlpatterns = [
    path('', views.vacancy_list_view),
    path('<int:vacancy_id>', views.vacancy_view),
    path('cat/<str:vacancy_name>', views.specialty_view),

]
