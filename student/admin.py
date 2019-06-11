from django.contrib import admin
from .models import *


class StudentAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Student._meta.fields]
    # exclude = ["email"]
    # field = ["name"]
    list_filter = ('name',)
    search_fields = ["name", "email"]

    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)



