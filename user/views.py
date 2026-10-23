
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .user import UserForm

# create your view here.

def listusers(request):
    template = loader.get_template('userlist.html');
    return  HttpResponse(template.render())

def userhome(request):
    return HttpResponse("<h1>This is list of user home page</h1>")

def adduser(request):
    if request.method=="GET":
        userform_obj =UserForm()
        return render (request,'adduser.html',{'userform':userform_obj});
    elif request.method=="POST":
         userform_data = UserForm(request.POST)
         if userform_data.is_valid():
            fname = userform_data.cleaned_data["fname"]
            mname = userform_data.cleaned_data["mname"]
            lname = userform_data.cleaned_data["lname"]
            return render(request,'adduser_success.html',{'fname':fname,'mname':mname,'lname':lname})
            
def adduser_success(request):
    return HttpResponse("User added successfully!")
            