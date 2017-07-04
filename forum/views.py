from django.shortcuts import render

def feed(request):
    return render(request,'feed.html')

def ask(request):
    return render(request,'ask.html')
