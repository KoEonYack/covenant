from django.shortcuts import render

def python(request):
    return render(request, 'python/python_list.html')

def python1(request):
    return render(request, 'python/python_1.html')

def python2(request):
    return render(request, 'python/python_2.html')