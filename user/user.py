from django import forms 

class UserForm (forms.Form):
    fname = forms.CharField(max_length=30,label="Enter First Name")
    mname = forms.CharField(label="Enter Middle Name")
    lname = forms.CharField(max_length=30,label="Enter last Name")
    email = forms.EmailField(label="Enter your Email Id")
    # password, gender, data of birth, mobile,address,city,
    password = forms.CharField(widget=forms.PasswordInput(),label="password")
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="Date of birth")  
    mobile = forms.CharField(max_length=10,label="mobile")
    gender= forms.ChoiceField(choices=[('','Select Gender'),('male','Male'),('female','Female')],label="Gender")    