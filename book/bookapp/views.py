from bookapp.models import Bookinfo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render, redirect
from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.


def showbook(request):
    book=Bookinfo.objects.all()
    data = {}
    data['book'] = book
    
    genrelist=[]
    for i in book:
      genrelist.append(i.genre)
    genre_unique = []
    unique_numbers = set(genrelist)
    for number in unique_numbers:
        genre_unique.append(number)
    data['k']=genre_unique
    language_list=[]
    for i in book:
      language_list.append(i.language)
    language_unique = []
    unique_numbers = set(language_list)
    for number in unique_numbers:
        language_unique.append(number)
    print(language_unique)
    data['la']=language_unique
    print("language_unique",language_unique)
   
    return render(request,'book/showbooks.html', data)

def addbook(request):
    bookform=forms.bookform()
    if request.method=='POST':
        productForm=forms.bookform(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return redirect('showbook')
    return render(request,'book/addbook.html',{'bookform':bookform})


def searchbook(request):
    genrelist1 = request.POST.getlist('genrecheck[]')
    languagelist = request.POST.getlist('langauagecheck[]')
    print(genrelist1)
    print(languagelist)

    book=Bookinfo.objects.all()

    genrelist=[]
    for i in book:
      genrelist.append(i.genre)
    genre_unique = []
    unique_numbers = set(genrelist)
    for number in unique_numbers:
        genre_unique.append(number)
    language_list=[]
    for i in book:
      language_list.append(i.language)
    language_unique = []
    unique_numbers = set(language_list)
    for number in unique_numbers:
        language_unique.append(number)
    print(language_unique)
    print("language_unique",language_unique)
    if not genrelist1:
        genrelist1=genre_unique 
    if not languagelist:
        languagelist=language_unique

    print("Test1",genrelist1)
    book= Bookinfo.objects.filter(genre__in=genrelist1 ).filter(language__in=languagelist)
  
    data= {}
    data['book'] = book
    data['k']=genre_unique
    data['la']=language_unique
    return render(request,'book/showbooks.html',data )