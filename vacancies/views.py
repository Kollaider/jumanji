from django.db.models import Sum, Count
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View

from .models import Company, Specialty, Vacancy

from django.http import HttpResponseNotFound

class MainView(View):

    def get(self, request):

        specialities = {}
        for entry in Specialty.objects.all():
            specialities[entry.title] = Vacancy.objects.filter(specialty__code=entry.code).count()

        companies = {}
        for entry in Company.objects.all():
            companies[entry.logo] = Vacancy.objects.filter(company__name=entry.name).count()

        return render(request, 'index.html', context={'specialities': specialities,
                                                      'companies': companies,
                                                      })


class ListAllVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()

        return render(request, 'vacancies.html', context={'vacancies': vacancies,
                                                          'title': 'Все вакансии'})


class ListSpecialtyView(View):

    def get(self, request, specialty):
        vacancies = Vacancy.objects.filter(specialty__code=specialty)
        if not len(vacancies):
            return HttpResponseNotFound(f'Специальности с именем {specialty} нам не известено!')

        return render(request, 'vacancies.html', context={'vacancies': vacancies,
                                                          'title': specialty.capitalize()})


class CompanyView(View):

    def get(self, request, company_id):

        company = Company.objects.get(id=6)

        vacancies = Vacancy.objects.filter(company__name=company.name)

        return render(request, 'company.html', context={'company': company,
                                                        'vacancies': vacancies})


class VacancyView(View):

    def get(self, request, vacancy_id):

        vacancy = Vacancy.objects.get(id=4)

        print(vacancy.company.name)
        company = Company.objects.get(name=vacancy.company.name)
        print(company)
        return render(request, 'vacancy.html', context={'vacancy': vacancy,
                                                        'company': company})
