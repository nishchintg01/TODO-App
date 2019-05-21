from django.db import models

class Student_form(models.Model):
    stu_name = models.CharField(max_length=70)
    Stu_roll_no = models.IntegerField()
    stu_section = models.CharField(max_length=5)
    Stu_email = models.EmailField()

    def __str__(self):
        return self.stu_name

    class Meta:
        verbose_name_plural = "Student_form"

class TodoApp(models.Model):
    task=models.CharField(max_length=100)
    value=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural='task'
