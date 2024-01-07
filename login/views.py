from django.shortcuts import render, redirect
from django.contrib import auth
from signup.models import EmployeeDetails 

# Create your views here.

def loginAction(request):
    if request.method == 'POST':
        em = request.POST['email']
        pwd = request.POST['pwd']
        mn = request.POST['designation']

        user = auth.authenticate(username=em, password=pwd)
        if user is not None:
            auth.login(request, user)
            if mn == 'manager':
                return render(request, 'managerDashboard.html') 
            elif mn == 'employee':
                return render(request, '/home')
            return redirect("/home") 
        else:
            message.info(request,'Invalid Credentials')
            return redirect("/login")

    else:
        return render(request, 'login_page.html')
