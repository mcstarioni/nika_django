from django.db import models

# the following lines added:
import datetime
from django.utils import timezone


class Student(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Студент %s %s" % (self.name, self.email,)
