from django.contrib import admin
from .models import *

class ActivityAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Activity._meta.fields]
    list_filter = ('activity',)
    search_fields = ["activity", "subject"]

    class Meta:
        model = Activity

class MarksOfActivityAdmin (admin.ModelAdmin):

    list_display = [field.name for field in MarksOfActivity._meta.fields]

    class Meta:
        model = MarksOfActivity

    list_filter = ('stud',)
    search_fields = ["act", "stud", "mark"]


class SubjectAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subject._meta.fields]

    class Meta:
        model = Subject

    search_fields = ["subj"]


class CompetenceAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Competence._meta.fields]

    class Meta:
        model = Competence

    search_fields = ["comp_name"]


admin.site.register(MarksOfActivity, MarksOfActivityAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Competence, CompetenceAdmin)

