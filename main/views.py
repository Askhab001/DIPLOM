from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def main(request):
    return render(request, 'aza1.html')


def aza(request):
    return render(request, 'aza2.html')

def asa(request):
    return render(request, 'aza3.html')