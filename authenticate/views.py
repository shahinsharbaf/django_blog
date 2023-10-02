from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

    if User.objects.filter(username=user_name).exists():
        messages.info(request,'username exist')
    else:
        User.objects.create_user(username=user_name,password=password,email=email)

    return render(request,'authenticate/signup.html')