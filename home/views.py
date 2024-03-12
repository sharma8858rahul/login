from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.core.exceptions import MultipleObjectsReturned

@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')
# Create your views here.

def index(request):
    return render(request, 'index.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
           

        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')  

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def HomePage(request):
    return render(request, 'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def forget_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except MultipleObjectsReturned:
                user = User.objects.filter(email=email).first()
            subject = 'Password Reset Request'
            message = f'Hi {user.username},\n\nYou have requested a password reset. Click the link below to reset your password:\nhttp://your-site.com/password-reset/{user.reset_token}/\n\nIf you did not request a password reset, please ignore this email.'
            send_mail(
                subject=subject,
                message=message,
                from_email='your-email@example.com',
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect('forget_password_success')
    else:
        form = PasswordResetForm()
    return render(request, 'forget_password.html', {'form': form})

