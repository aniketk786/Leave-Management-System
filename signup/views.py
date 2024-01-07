from django.shortcuts import render, redirect
from django.contrib import messages
from .models import * 
# import sqlite3 as sql
# fn=''
# ln=''
# emp=''
# em=''
# pwd=''

# Create your views here.
def signupAction(request):
    error=""
    if request.method=="POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empc']
        em = request.POST['email']
        pwd = request.POST['pwd']
        mn = request.POST['designation']
        if User.objects.filter(email=em).exists():
            messages.info(request,'Username is taken already')
        else:
            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password = pwd)
                EmployeeDetails.objects.create(user=user, empcode=ec, designation=mn)
                error="no"
                if mn == 'manager':
                    return render(request, 'managerDashboard.html')  # Replace 'manager-url' with your manager URL name
                elif mn == 'employee':
                    return render(request, 'abc.html')  # Replace 'employee-url' with your employee URL name
            except:
                error="yes"
            
    return render(request, 'signup_page.html', locals())

def emp_login(request):
    return render(request,'emp_login.html')


    
