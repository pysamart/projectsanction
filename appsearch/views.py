from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def appsearch(request):
    # return HttpResponse("<h1>Bismillah</h1>")
    return render(request, 'index.html')