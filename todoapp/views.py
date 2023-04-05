from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyloginForm
from .forms import SignUpForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from.forms import NotesForm, ContactForm
from .models import Notes, Contact

# Login

class Mylogin(LoginView):
    template_name = 'todoapp/login.html'
    authentication_form = MyloginForm
# Logout
@method_decorator(login_required, name='dispatch')
class MyLogout(LogoutView):
    template_name = 'todoapp/logout.html'

@method_decorator(login_required, name='dispatch')
class home(TemplateView):
    template_name = 'todoapp/home.html'

@method_decorator(login_required, name='dispatch')
class dashboard(TemplateView):
    template_name = 'todoapp/dashboard.html'


class index(TemplateView):
    template_name = 'todoapp/index.html'



# Registration
def UserSignUp(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created')
    else:
        fm=SignUpForm()
    return render (request, 'todoapp/signup.html', {'form':fm})

def aboutSec(request):
    return render(request, 'todoapp/about.html')

@login_required
def Homeadd(request):
    if request.method == "POST":
        fm = NotesForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = NotesForm()
    else:
        fm = NotesForm()
    
    return render(request, 'todoapp/home.html', {'form': fm})   

@login_required
def ViewNotes(request):
    stu = Notes.objects.all()
    return render (request,'todoapp/yourNotes.html', { 'stu':stu})

def editNotes(request, id):
    if request.method == "POST":
        fm = Notes.objects.get(pk=id)
        nt = NotesForm(request.POST, instance=fm)
        if nt.is_valid():
            nt.save()
        return HttpResponseRedirect('/yourNotes/')
    else:
        fm = Notes.objects.get(pk=id)
        nt = NotesForm(instance=fm)
        return render(request, 'todoapp/editnote.html', {'form': nt})
    
def contactUs(request):
    if request.method == "POST":
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your Message has been submitted, We will reach you soon')
        return render (request, 'todoapp/contactUs.html',{'form':fm})
    else:
        fm = ContactForm()
        return render(request,'todoapp/contactUs.html',{'form':fm})

@login_required
def deleteNotes(request, id):
    if request.method == "POST":
        stu = Notes.objects.get(pk=id)
        stu.delete()
    return HttpResponseRedirect('/yourNotes/')