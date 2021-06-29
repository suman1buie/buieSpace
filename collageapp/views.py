from django.shortcuts import render
from .models import Atrical , UserProfile , Academic , Semester, Study , Trade, Year, Metarial, Subject, Sellybus ,Question ,Subject ,Sellybus
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import  User,auth
from django.views.generic import DetailView
from django.views.generic import ListView
from . forms import SignUpForm 
from django.views.generic.edit import CreateView , UpdateView
from django.contrib.messages.views import SuccessMessageMixin


def Signup(request):
    if request.method == 'POST':
        form      = SignUpForm(request.POST)
        email     = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1!=password2:
            messages.error(request,"password no match!!! Try again")
            return redirect('/collageapp/signup/')
		
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email Allredy Register.. !!Try new One..!")
            return redirect('/collageapp/signup/')

        elif form.is_valid():
            form.save()
            messages.success(request,"Account create successfully! :)\n Now Log In")
            return redirect('/collageapp/signin/')
        else:
            messages.error(request,'Unsuccessful :(.... try again!!!')
            return redirect('/collageapp/signup/')
    else:
        form = SignUpForm()
    return render(request,"signup.html",{'form':form})




def Home(request):
    return render(request,"index.html")


def Article(request):
    curentUserProfile = 'none'
    allArtical = Atrical.objects.all()
    if(str(request.user)!="AnonymousUser"):
        curentUserProfile = UserProfile.objects.get(user=request.user)

    return render(request,"artical.html",{ "articals": allArtical,'currentUser':curentUserProfile})


def Academi(request):
    return render(request,"academi.html")


def Profile(request,pk):
    profile = User.objects.get(pk=pk)
    uProfile = UserProfile.objects.get(user=profile)
    return render(request,"profile.html",{ "profile":uProfile})


def AboutUs(request):
    return render(request,"about.html")


def SignIn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You loged In successfully!!!")
            return redirect('/collageapp/artical/')
        else:
            messages.error(request,"invalid username or password")
            return redirect('/collageapp/signin/')
    
    return render(request,"signin.html",{})


def log_out(request):
	auth.logout(request)
	messages.success(request,"You Loged Out Successfully !")
	return redirect('/collageapp/artical/')



class ProfileUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'editprofile.html'
    model  		  = UserProfile
    fields 		  = ['department','roll','passoutyr','first_name','last_name','profile_pic','socal_link','ph_no','description'] 
    success_url = '/collageapp/artical/'
    success_message = "profile updae successfully"


class PostCreate(CreateView):
    template_name = "uploadFile.html"
    model  = Atrical
    fields = ["description","title","image"]
    def form_valid(self,form):
        self.objects = form.save()
        self.objects.uploded_by = self.request.user
        self.objects.save()
        messages.success(self.request,"Your Post Upload successfully!")
        return redirect('/collageapp/artical/')
    

def delete(request,pk):
	want_to_delete_item = Atrical.objects.get(pk=pk)
	want_to_delete_item.delete()
	messages.success(request,"Post Delete Successfully :)")
	return redirect('/collageapp/artical/')


class EditPostView(SuccessMessageMixin,UpdateView):
	template_name   = 'editPost.html'
	model  	        = Atrical
	fields          = ["description","title","image"]
	success_url     = '/collageapp/artical/'
	success_message =  "Post Update Successfully! :)"
 

def Notice(request):
    notices = Academic.objects.all()
    allNotices = []
    for notice in notices:
        if(str(notice.catagory)=="Notice"):
            allNotices.append(notice)
    
    return render(request,'notice.html',{"Notices":allNotices})



def ClassRoutine(request):
    semester = Semester.objects.all()
    year = Year.objects.all()
    trade = Trade.objects.all()
    if request.method=="POST":
        sem = request.POST['semm']
        yer = request.POST['year']
        dep = request.POST['depp']
        allRoutine = []
        routines = Academic.objects.all()
        for routin in routines:
            if (str(routin.catagory)=='Class Routine' and (str(routin.department)==str(dep) or str(dep) == "Select Department" ) and (str(routin.year) == str(yer) or str(yer) == "Select Year") and (str(routin.sem) == str(sem) or str(sem) == "Select Semester" )):
                allRoutine.append(routin)
        return render(request,'classRoutine.html',{'sems':semester,'years':year,'trades':trade,'routins':allRoutine}) 
    
    return render(request,'classRoutine.html',{'sems':semester,'years':year,'trades':trade})


def study(request):
    semester = Semester.objects.all()
    year = Year.objects.all()
    trade = Trade.objects.all()
    if request.method=="POST":
        sem = request.POST['semm']
        yer = request.POST['year']
        dep = request.POST['depp']
        subjects = Study.objects.all()
        allSubject = []
        for subject in subjects:
            if ((str(subject.department)==str(dep) or str(dep) == "Select Department" ) and (str(subject.year) == str(yer) or str(yer) == "Select Year") and (str(subject.sem) == str(sem) or str(sem) == "Select Semester" )):
                allSubject.append(subject)
        return render(request,"studymet.html",{'sems':semester,'years':year,'trades':trade,"subjects":allSubject})
    
    return render(request,"studymet.html",{'sems':semester,'years':year,'trades':trade})



def sullybus(request,pk):
    subject = Subject.objects.get(pk=pk)
    syb = Sellybus.objects.filter(subject=subject)
    return render(request,"sullybus.html",{"sybs":syb,"subject":subject})


def notes(request,pk):
    subject = Subject.objects.get(pk=pk)
    notes = Metarial.objects.filter(subject=subject)
    return render(request,"notes.html",{"notes":notes,"subject":subject})


def question(request,pk):
    subject = Subject.objects.get(pk=pk)
    qus = Question.objects.filter(subject=subject)
    return render(request,"question.html",{"questions":qus,"subject":subject})