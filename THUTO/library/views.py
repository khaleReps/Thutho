from django.shortcuts import render

# Create your views here.

def development(request):
    context = {}
    return render(request, 'library/library-development.html', context)

def featured(request):
    context = {}
    return render(request, 'library/library-featured.html', context)

def filters_development(request):
    context = {}
    return render(request, 'library/library-filters-development.html', context)

def filters_development_list(request):
    context = {}
    return render(request, 'library/library-filters-development-list.html', context)

def filters(request):
    context = {}
    return render(request, 'library/library-filters.html', context)

def filters_list(request):
    context = {}
    return render(request, 'library/library-filters-list.html', context)

def library(request):
    context = {}
    return render(request, 'library/library.html', context)