from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def link1(request):
    return render(request,'home.html')

# Create your views here.
