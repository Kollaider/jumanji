from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404
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

        return render(request, 'index.html', context={
            'specialities': specialities,
            'companies': companies
        })


class ListAllVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()

        return render(request, 'vacancies.html', context={
            'vacancies': vacancies,
            'title': 'Все вакансии'
        })


class ListSpecialtyView(View):

    def get(self, request, specialty):

        vacancies = Vacancy.objects.filter(specialty__code=specialty)

        print(vacancies)
        if not len(vacancies):
            raise Http404(f'Специальности с именем {specialty} нам не известено!')

        return render(request, 'vacancies.html', context={
            'vacancies': vacancies,
            'title': specialty.capitalize()
        })


class CompanyView(View):

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=1)

        vacancies = Vacancy.objects.filter(company__name=company.name)

        return render(request, 'company.html', context={
            'company': company,
            'vacancies': vacancies
        })


class VacancyView(View):

    def get(self, request, vacancy_id):

        vacancy = get_object_or_404(Vacancy, id=1)
        company = get_object_or_404(Company, name=vacancy.company.name)

        return render(request, 'vacancy.html', context={
            'vacancy': vacancy,
            'company': company})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Здесь ничего нет')


def custom_handler500(request):
    return HttpResponseServerError('На сервере что-то сломалось')
