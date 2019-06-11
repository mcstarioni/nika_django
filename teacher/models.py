from django.db import models
from student.models import Student

class Teacher(models.Model):
    name = models.CharField(max_length=604, blank=True, null=True, default=None)
    position = models.CharField(max_length=604, blank=True, null=True, default=None)


    def __str__(self):
        return "Преподаватель %s должность %s " % (self.name, self.position)

