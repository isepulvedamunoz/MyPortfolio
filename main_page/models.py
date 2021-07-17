from django.db import models
from django.db.models.fields import CharField


class Personal_info(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    introduction = models.CharField(max_length=255)
    

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name_project = models.CharField(max_length=255)
    languaje = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='static/assets/img/')
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    type_project = models.CharField(max_length=50)
    id_person = models.ForeignKey(Personal_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_project

class educ_info(models.Model):
    type_info = models.CharField(max_length=100)
    name_info = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    id_person = models.ForeignKey(Personal_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_info

class Profesional_info(models.Model):
    position = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    id_person = models.ForeignKey(Personal_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.position


