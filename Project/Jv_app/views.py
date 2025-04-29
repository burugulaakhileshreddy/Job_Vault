from errno import EUSERS

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse,render,redirect
from .models import Internships,Full_Time,C2C,W2,Portfolios
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def Portfolio(request):
    portfolios = Portfolios.objects.filter(Status=True)
    return render(request,'Portfolio.html',{'portfolios': portfolios})

@login_required
def Home(request):

    user=request.user
    total_internships=Internships.objects.filter(user=user).count()
    total_full_times=Full_Time.objects.filter(user=user).count()
    total_c2c=C2C.objects.filter(user=user).count()
    total_w2=W2.objects.filter(user=user).count()
    return render(request,'Home.html',{'total_internships':total_internships,'total_full_times':total_full_times,'total_c2c':total_c2c,'total_w2':total_w2})

def Sign_Up(request):
    if request.method == 'POST':
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email Already Exists! <a href="''">Sign Up</a>')

        else:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            return redirect('Log_In')

    return render(request,'Sign_Up.html')


def Log_In(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=authenticate(request,username=email,password=password)

        if user is not None:

            login(request, user)
            return redirect('/Home/')
        else:

            messages.error(request, "Invalid email or password")
            return redirect('Log_In')

    return render(request, 'Log_In.html')

def Log_out(request):
    logout(request)
    return redirect('Log_In')

@login_required
def Add_Job(request):

    user=request.user
    num_forms=0
    if request.method =='POST':
        if 'num_forms' in request.POST:
            num_forms=int(request.POST.get('num_forms'))

            if num_forms > 0:
                form_range = range(num_forms)
                return render(request, 'Add_Job.html', {'num_forms': num_forms, 'form_range': form_range})


    if request.FILES:

        num_forms=int(request.POST.get('num_forms_form1'))

        for i in range(num_forms):

            job_type = request.POST.get(f'job_type_{i}')
            company_name = request.POST.get(f'company_name_{i}')
            platform = request.POST.get(f'platform_{i}')
            date = request.POST.get(f'date_{i}')
            resume = request.FILES.get(f'resume_{i}')
            cover_letter = request.FILES.get(f'cover_letter_{i}')
            link = request.POST.get(f'url_{i}')
            notes = request.POST.get(f'notes_{i}')

            user = request.user

            if job_type == 'internship':
                new_Internships = Internships(Company_Name=company_name, Date=date, Platform=platform,
                                                      Resume=resume, Cover_Letter=cover_letter, Link=link, Notes=notes,user=user)
                new_Internships.save()
            elif job_type == 'full_time':
                new_Full_Time = Full_Time(Company_Name=company_name, Date=date, Platform=platform,
                                                  Resume=resume, Cover_Letter=cover_letter, Link=link, Notes=notes,user=user)
                new_Full_Time.save()
            elif job_type == 'c2c':
                new_C2C = C2C(Company_Name=company_name, Date=date, Platform=platform, Resume=resume,
                                      Cover_Letter=cover_letter, Link=link, Notes=notes,user=user)
                new_C2C.save()
            elif job_type == 'w2':
                new_W2 = W2(Company_Name=company_name, Date=date, Platform=platform, Resume=resume,
                                    Cover_Letter=cover_letter, Link=link, Notes=notes,user=user)
                new_W2.save()

        messages.success(request, "Jobs Added Sucessfully")
        return redirect('Home')
    form_range = range(num_forms)
    return render(request,'Add_Job.html',{'num_forms':num_forms,'form_range':form_range})

@login_required
def Manage_Portfolio(request):

    user = request.user
    if request.method=='POST':
        portfolio_name=request.POST.get("portfolio_name")
        portfolio_file=request.FILES.get("portfolio_file")

        new_portfolios= Portfolios(user=user,Portfolio_Name=portfolio_name, Portfolio=portfolio_file)
        new_portfolios.save()

    display=Portfolios.objects.filter(user=user)
    current_portfolio=Portfolios.objects.filter(user=user,Status=True)
    return render(request,'Manage_Portfolio.html',{'display':display,'current_portfolio':current_portfolio})

@login_required
def Make_Current_Portfolio(request):

    if request.method == 'POST':
        selected_folio = request.POST.get('portfolio_id')
        user = request.user
        Portfolios.objects.filter(user=user).update(Status=False)

        Portfolios.objects.filter(id=selected_folio, user=user).update(Status=True)

    return redirect('Manage_Portfolio')

@login_required
def Display_Jobs(request,job_type):

    user=request.user

    if job_type == 'internships':
        display = Internships.objects.filter(user=user)  # Fetch all data from the Internships table
    elif job_type == 'full_time':
        display = Full_Time.objects.filter(user=user)  # Fetch data from the FullTime table
    elif job_type == 'c2c':
        display = C2C.objects.filter(user=user)  # Fetch data from the C2C table
    elif job_type == 'w2':
        display = W2.objects.filter(user=user)  # Fetch data from the W2 table
    else:
        display = []

    return render(request,'Display_Jobs.html',{'display':display,'job_type':job_type})



