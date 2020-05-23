from django.db import models
from django.utils import timezone

class Course(models.Model) :
    name = models.CharField(max_length = 20)
    code = models.CharField(max_length = 10)

    def __str__(self) :
        return self.code + ': ' + self.name

class ResearchArea(models.Model) :
    name = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name

class Professor(models.Model) :
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    dsgn = models.CharField(max_length = 20)
    department = models.CharField(max_length = 20)
    email = models.EmailField()
    contact_no = models.CharField(max_length = 10)
    courses_taken = models.ManyToManyField(Course)
    research_area = models.ManyToManyField(ResearchArea)

    def __str__(self) :
        return self.first_name + ' ' + self.last_name

class Publication(models.Model) :
    title = models.CharField(max_length = 100)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)

    def __str__(self) :
        return self.title

class Notice(models.Model) :
    title = models.CharField(max_length = 20)
    text = models.TextField()
    created_date = models.DateField(default = timezone.now)

    def __str__(self) :
        return self.title


class Assignment(models.Model) :
    title = models.CharField(max_length = 20)
    assign_file = models.FileField(upload_to = 'faculty/')
    created_date = models.DateField(default = timezone.now)

    def __str__(self) :
        return self.title