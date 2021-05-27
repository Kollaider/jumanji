from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View

class MainView(View):

    def get(self, request):

        return render(request, 'index.html')


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