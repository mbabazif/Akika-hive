from django.shortcuts import render,redirect
from .forms import StudentForm,FreelancerForm,EnterpriseForm,BusinessForm,AcademicForm,GovernmentForm,ContactForm,Subscribe
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .models import Student
from django.http import HttpResponse, Http404,HttpResponseRedirect

from django.core.mail import send_mail, BadHeaderError
from .email import send_welcome_email
from django.conf import settings
from . import forms
from akika.settings import EMAIL_HOST_USER









# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'start.html')

def search_results(request):

    if 'student' in request.GET and request.GET["student"]:
        search_term = request.GET.get("student")
        searched_student = Student.search_by_first_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-hive/search.html',{"message":message,"student": searched_student})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-hive/search.html',{"message":message}) 


@login_required(login_url='/accounts/login/')
def student(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
           first_name = form.save(commit=False)
           last_name = form.save(commit=False)
           education_level = form.save(commit=False)
           student_email= form.save(commit=False)
            # article.editor = current_user
           first_name .save()
           last_name .save()
           education_level .save()
           student_email .save()
        return redirect('welcome')

    else:
        form = StudentForm()
    return render(request, 'student.html', {"form": form})


@login_required(login_url='/accounts/login/')
def freelancer(request):
    current_user = request.user
    if request.method == 'POST':
        form = FreelancerForm(request.POST, request.FILES)
        if form.is_valid():
           freelancer_names= form.save(commit=False)
           project_name = form.save(commit=False)
           freelancer_email = form.save(commit=False)
           freelancer_names .save()
           project_name .save()
           freelancer_email .save()
          
        return redirect('welcome')

    else:
        form = FreelancerForm()
    return render(request, 'freelancer.html', {"form": form})


@login_required(login_url='/accounts/login/')
def enterprise(request):
    current_user = request.user
    if request.method == 'POST':
        form = EnterpriseForm(request.POST, request.FILES)
        if form.is_valid():
           enterprise_founder= form.save(commit=False)
           enterprise_name = form.save(commit=False)
           enterprise_location = form.save(commit=False)
           entrprise_email= form.save(commit=False)
            # article.editor = current_user
           enterprise_founder .save()
           enterprise_name .save()
           enterprise_location .save()
           entrprise_email .save()
        return redirect('welcome')

    else:
        form =EnterpriseForm()
    return render(request, 'enterprise.html', {"form": form})


@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
           business_founder = form.save(commit=False)
           business_name = form.save(commit=False)
           business_location = form.save(commit=False)
           business_email= form.save(commit=False)
            # article.editor = current_user
           business_founder .save()
           business_name .save()
           business_location .save()
           business_email .save()
        return redirect('welcome')

    else:
        form = BusinessForm()
    return render(request, 'businessform.html', {"form": form})


@login_required(login_url='/accounts/login/')
def academic(request):
    current_user = request.user
    if request.method == 'POST':
        form = AcademicForm(request.POST, request.FILES)
        if form.is_valid():
           academic_name = form.save(commit=False)
           academic_location = form.save(commit=False)
           academic_email = form.save(commit=False)
          
            # article.editor = current_user

           academic_name  .save()
           academic_location .save()
           academic_email .save()
        return redirect('welcome')

    else:
        form = AcademicForm()
    return render(request, 'academic.html', {"form": form})


@login_required(login_url='/accounts/login/')
def government(request):
    current_user = request.user
    if request.method == 'POST':
        form = GovernmentForm(request.POST, request.FILES)
        if form.is_valid():
           first_name = form.save(commit=False)
           last_name = form.save(commit=False)
           education_level = form.save(commit=False)
           student_email= form.save(commit=False)
            # article.editor = current_user
           first_name .save()
           last_name .save()
           education_level .save()
           student_email .save()
        return redirect('welcome')

    else:
        form = GovernmentForm()
    return render(request, 'government.html', {"form": form})


def about(request):
    return render(request, 'about.html')

def solutions(request):
    return render(request, 'solutions.html')

def solution1(request):
    return render(request, 'solution1.html')   


def contactus(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['umulisaa0@gmail.com'], 
		 fail_silently=False)
	return render(request, 'contact.html')


def enterpreneurship(request):
    return render(request, 'enterpreneurship.html')



    # Create your views here.
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Akika-Bee-Hive'
        message = 'Hope you are enjoying your journey with Akika-Bee-Hive'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})



def team(request):
    return render(request, 'team.html')

def academics(request):
    return render(request, 'academic.html')

def fintech(request):
    return render(request, 'fintech.html')

def software(request):
    return render(request, 'software.html')    

def enterpreneurs(request):
    return render(request, 'enterpreneurs.html')
def internet(request):
    return render(request, 'internet.html')
def cloudcomputing(request):
    return render(request, 'cloud-computing.html')

def machine(request):
    return render(request, 'machine-learning.html')

def robotics(request):
    return render(request, 'robotics.html')
def blockchain(request):
    return render(request, 'blockchain.html')

def security(request):
    return render(request, 'cyber-security.html')





    



