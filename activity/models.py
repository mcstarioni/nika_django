from django.db import models
from student.models import Student
from teacher.models import Teacher


class Competence(models.Model):
    comp_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    def __str__(self):
        return "предмет %s" % (self.comp_name)

class Subject(models.Model):
    subj = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "предмет %s" % (self.subj)




class Activity(models.Model):
    activity = models.CharField(max_length=128, blank=True, null=True, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Активность %s по предмету %s" % (self.activity, self.subject,)


class MarksOfActivity(models.Model):

    act = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    mark = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    score = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    stud = models.ForeignKey(Student, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)

    # stud = models.ForeignKey(
    #     'Student',
    #     on_delete=models.DO_NOTHING, blank=True, null=True, default=None
    # )



    # def save(self, *args,**kwargs):
    #     finaly_mark = self.mark*self.score*2
    #     super(MarksOfActivityAct, self).save(self, *args,**kwargs)


    def __str__(self):
        return "Оценка %s студента %s по предмету %s" % (self.mark, self.stud, self.act)
