from django.shortcuts import render, redirect

# Create your views here.

from .forms import NewUserForm
from django.contrib.auth import login
from user.models import Profile
from django.contrib.auth import authenticate, login as djangologin

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			enterDetails(request, user)
			# return render(request=request, template_name = "user/enterDetails.html")
	form = NewUserForm()
	return render (request=request, template_name="user/register.html", context={"register_form":form})

def enterDetails(request, user):
    if request.method == "POST":
        post = Profile()
        post.userAuth = user
        post.aadhar_number = request.post.get('aadhar_number')
        post.pan_number = request.post.get('pan_number')
        post.dob = request.post.get('dob')
        post.address = request.post.get('address')
        post.city = request.post.get('city')
        post.state = request.post.get('state')
        post.bank_name = request.post.get('bank_name')
        post.bank_account_number = request.post.get('bank_account_number')
        post.bank_IFSC_code = request.post.get('bank_IFSC_code')
        post.aadhar_proof = request.post.get('aadhar_proof')
        post.pan_proof = request.post.get('pan_proof')
        post.bank_proof = request.post.get('bank_proof')
        post.created_at = request.post.get('created_at')
        post.updated_at = request.post.get('updated_at')
        post.save()
        return render(request=request, template_name="user/login.html")
    return render (request=request, template_name="user/enterDetails.html", context={"user":user})

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            return redirect("Home")
    return render (request=request, template_name="user/login.html")