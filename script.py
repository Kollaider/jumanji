import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'jumanji.settings'
django.setup()

import data
from vacancies.models import Company, Specialty, Vacancy



def update_data(moc_data):
    for spec in moc_data.specialties:
        specialty = Specialty(
            code=spec.get("code"),
            title=spec.get("title")
        )
        specialty.save()

    for data_company in moc_data.companies:
        company = Company(
            name=data_company.get("title"),
            location=data_company.get("location"),
            logo=data_company.get('logo'),
            description=data_company.get("description"),
            employee_count=data_company.get("employee_count"),
        )
        company.save()

    for job in moc_data.jobs:
        vacancy = Vacancy(
            title=job.get("title"),
            specialty=Specialty.objects.get(code=job.get("specialty")),
            company=Company.objects.get(id=job.get("company")),
            skills=job.get("skills"),
            description=job.get("description"),
            salary_min=job.get("salary_from"),
            salary_max=job.get("salary_to"),
            published_at=job.get("published_at"),
        )
        vacancy.save()


def clean_data():
    Vacancy.objects.all().delete()
    Company.objects.all().delete()
    Specialty.objects.all().delete()


if __name__ == '__main__':
    update_data(data)
    # clean_data()