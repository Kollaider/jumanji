from django.db.models import Sum, Count
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View

from .models import Company, Specialty, Vacancy

class MainView(View):

    def get(self, request):

        specialities = {}
        for entry in Specialty.objects.all():
            specialities[entry.title] = Vacancy.objects.filter(specialty__code=entry.code).count()

        companies = {}
        for entry in Company.objects.all():
            companies[entry.logo] = Vacancy.objects.filter(company__name=entry.name).count()

        return render(request, 'index.html', context={'specialities': specialities, 'companies': companies})


class ListAllVacanciesView(View):

    def get(self, request):

        return render(request, 'vacancies.html')



class ListSpecialtyView(View):

    def get(self, request):
        return render(request, 'vacancies.html')


class CompanyView(View):

    def get(self, request):
        return render(request, 'company.html')


class VacancyView(View):

    def get(self, request):
        return render(request, 'vacancy.html')