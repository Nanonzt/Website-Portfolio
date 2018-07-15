from django.shortcuts import render


def index(request):
    return render(request, 'Main/index.html', {})

def about(request):
    return render(request, 'Main/about.html', {})

def skills(request):
    return render(request, 'Main/skills.html', {})

def contact(request):
    return render(request, 'Main/contact.html', {})
