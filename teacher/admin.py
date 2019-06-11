from django.contrib import admin
from .models import *


class TeacherAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Teacher._meta.fields]
    list_filter = ('name',)
    search_fields = ["name", "position"]

    class Meta:
        model = Teacher

admin.site.register(Teacher, TeacherAdmin)


