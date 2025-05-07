from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Service,Enquiry
from .forms import ServiceForm
from .serializers import EnquirySerializer
from rest_framework import generics


def index(request):
    return render(request, 'landing/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'landing/login.html', {'error': 'Invalid credentials'})
    return render(request, 'landing/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    services = Service.objects.all()
    return render(request, 'landing/dashboard.html', {'services': services})

@login_required(login_url='login')
def add_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'landing/add_service.html', {'form': form})

@login_required(login_url='login')
def edit_service(request, pk):
    service = Service.objects.get(pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'landing/add_service.html', {'form': form, 'service': service})

@login_required(login_url='login')
def delete_service(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('dashboard')
    return render(request, 'landing/delete_service.html', {'service': service})




class EnquiryListCreateView(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all().order_by('-submitted_at')
    serializer_class = EnquirySerializer


def service(request):
    services = Service.objects.all()
    return render(request, 'landing/service.html', {'services': services})