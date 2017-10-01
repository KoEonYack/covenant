from django.shortcuts import render

def python_lecture_list(request):
    return render(request, 'python/python_list.html')
# return render(request, 'python/python_list.html')

def python_lecture_1(request):
    return render(request, 'python_list/python_1.html')

def python_lecture_2(request):
    return render(request, 'python_list/python_2.html')

def python_lecture_3(request):
    return render(request, 'python_list/python_3.html')

def python_lecture_4(request):
    return render(request, 'python_list/python_4.html')

def python_lecture_5(request):
    return render(request, 'python_list/python_5.html')

def python_lecture_6(request):
    return render(request, 'python_list/python_6.html')

def python_lecture_7(request):
    return render(request, 'python_list/python_7.html')

