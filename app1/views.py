from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def link(request):
    return render(request,'link.html')
# Create your views here.
