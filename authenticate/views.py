from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                  form.save()
                  return HttpResponseRedirect (reverse('account:login'))
    else:
        form = RegisterForm()
    # form = FeedbackForm()
    # if request.method == 'POST':
    #     user_name = request.POST['username']
    #     password = request.POST['password']
    #     email = request.POST['email']

    #     if User.objects.filter(username=user_name).exists():
    #         messages.info(request,'username exist')
    #     else:
    #         user = User.objects.create_user(username=user_name,password=password,email=email)
    #         user.set_password(password)
    #         user.save()
    #         messages.info(request,'username created')

    return render(request,'authenticate/signup.html',{'form':form})


def login(request):
      return HttpResponse('gfv')