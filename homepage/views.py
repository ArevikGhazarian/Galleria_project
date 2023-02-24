from django.shortcuts import render


def base(request):
    return render(request, 'homepage/base.html')
