import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'jumanji.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy
from data import jobs, companies, specialties


def add_entries(collections):
    if collections is companies:
        for collection in collections:
            Company.objects.create(
                name=collection['title'],
                location=collection['location'],
                logo=collection['logo'],
                description=collection['description'],
                employee_count=collection['employee_count']
            )

    elif collections is jobs:
        for collection in collections:
            Vacancy.objects.create(
                title=collection['title'],
                specialty=Specialty.objects.get(code=collection['specialty']),
                company=Company.objects.get(id=collection['company']),
                skills=collection['skills'],
                description=collection['description'],
                salary_min=collection['salary_from'],
                salary_max=collection['salary_to'],
                published_at=collection['posted']
            )

    elif collections is specialties:
        for collection in collections:
            Specialty.objects.create(
                code=collection['code'],
                title=collection['title'],
            )


if __name__ == '__main__':
    add_entries(jobs)
    add_entries(companies)
    add_entries(specialties)
