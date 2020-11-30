from django.shortcuts import render

# Create your views here.
def dm(request):
    return render(request, 'dm.html')

def cj1(request):
    return render(request, 'cj1.html')

def cj2(request):
    return render(request, 'cj2.html')