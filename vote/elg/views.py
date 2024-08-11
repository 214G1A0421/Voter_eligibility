from django.shortcuts import render

# Create your views here.
def func1(request,age):
    d={'age':age}
    return render(request,'list.html',d)
