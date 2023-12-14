from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import GalleryForm, SignupForm
from .models import GalleryModel
from django.shortcuts import redirect

# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created!!')
            return redirect('login')
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                print('Form is valid')
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful!!')
                    return redirect('home')
            else:
                print('Form errors:', fm.errors)
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('home')

    
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = GalleryForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                img = GalleryModel.objects.all()
        else:
            fm = GalleryForm()
            img = GalleryModel.objects.all()
        return render(request, 'home.html', {'form':fm, 'Image':img})
    else:
        return redirect('login')
    
def new(request):
    fm = AuthenticationForm()
    return render(request, 'new.html', {'form':fm})

