from django.shortcuts import render


def first(request):
    return render(request, 'first_project.html')
