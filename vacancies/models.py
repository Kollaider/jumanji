from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=16)
    location = models.CharField(max_length=32)
    logo = models.CharField(max_length=32)
    description = models.TextField()
    employee_count = models.IntegerField()

class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=32)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):

    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return f'Vacancy {self.pk}'