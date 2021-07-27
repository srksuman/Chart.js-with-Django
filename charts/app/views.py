from django.contrib.admin.decorators import register
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.contrib import messages
from django.http import HttpResponseRedirect
import random
# Create your views here.
def showForm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student data is saved! view chart ")
            HttpResponseRedirect('/')

    form = StudentForm()
    return render(request,'html/index.html',context={'form':form})

def generating_different_color_function(l):
    print(l)
    rgb_list = []
    for _ in range(l):
        r = str(random.randint(0,256))
        g = str(random.randint(0,256))
        b = str(random.randint(0,256))
        rgb = f'rgb({r},{g},{b})'
        rgb_list.append(rgb)
    return rgb_list


def showChart(request):
    stu = Student.objects.all()
    color_list = generating_different_color_function(len(stu))
    return render(request,'html/chart.html',context={'color':color_list,'stu':stu})