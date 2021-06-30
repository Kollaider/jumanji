from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import DetailView, ListView, TemplateView

from .models import Company, Specialty, Vacancy


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(count=Count('vacancies'))
        context['companies'] = Company.objects.annotate(count=Count('vacancies'))
        return context



class DetailCompanyView(DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'company.html'

    def get_queryset(self):
        return self.model.objects.prefetch_related('vacancies', 'vacancies__specialty')


class DetailVacancyView(DetailView):
    model = Vacancy
    context_object_name = 'vacancy'
    template_name = 'vacancy.html'
    queryset = model.objects.select_related('specialty', 'company')


class ListVacanciesView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies.html"
    queryset = model.objects.select_related("specialty", "company")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies_title"] = "Все вакансии"
        return context


class ListSpecialtyView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancies.html'

    def get_queryset(self):
        return (
            self.model.objects
                .filter(specialty__code=self.kwargs['specialty'])
                .select_related('specialty', 'company')
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies_title'] = self.kwargs['specialty']

        return context


def custom_handler404(request, exception):
    return HttpResponseNotFound('Здесь ничего нет')


def custom_handler500(request):
    return HttpResponseServerError('На сервере что-то сломалось')
