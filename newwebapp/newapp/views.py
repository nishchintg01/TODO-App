from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_form,TodoApp
from .forms import ContactForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        student_name=request.POST['username']
        email_id=request.POST['email']
        section=request.POST['section']
        roll_no=request.POST['roll_no']
        stu=Student_form(stu_name=student_name,Stu_roll_no=roll_no,stu_section=section,Stu_email=email_id)
        stu.save()
        content={
        "stu":stu
        }
        return render(request,'newapp/index.html',content)

    return render(request,'newapp/form.html')

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        form.save()
        if form.is_valid():
            data=form.cleaned_data
            name=data['name']
            email=data['email']
            phone=data['phone_no']
            content={
            'name':name,
            'email':email,
            'phone':phone
            }
            return render(request,'newapp/index.html',content)
    a=ContactForm()

    return render(request,'newapp/index.html',{'a':a})
def Todoapp(request):
    if request.method == 'POST':
        a=request.POST['todo']
        data=TodoApp(task=a)
        data.save()
        messages.success(request,f'{a} has been added')
        a=False
        task=TodoApp.objects.order_by('-id')[:4]
        content={
        'task':task
        }
        return render(request,'newapp/todo.html',content)

    return render(request,'newapp/todo.html')
