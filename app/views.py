from django.shortcuts import render

def hello(request):
    return render(request, 'templates/main.html')

def code_language(request):
    return render(request, "templates/code_language.html")

def linux(request):
    return render(request, "templates/linux.html")