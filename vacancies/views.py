from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View

def main_view(request):

    return HttpResponse('Это главная страница!')

def vacancy_list_view(request):

    return HttpResponse(f'Здесь будут вакансии списком!')

def specialty_view(request, vacancy_name):

    return HttpResponse('Здесь будут вакансии по специальности!')


def company_view(request, company_id):
    return HttpResponse('Здесь будет информация о компании!')


def vacancy_view(request, vacancy_id):

    return HttpResponse('Здесь будет детальная информация о вакансии!')