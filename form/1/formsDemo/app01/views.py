from django.shortcuts import render,redirect

# Create your views here.

from .models import *

def books(request):
    book_list=Book.objects.all()
    return render(request,"books.html",locals())


def addbook(request):
    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish_id=request.POST.get("publish_id")
        author_pk_list=request.POST.getlist("author_pk_list") # [1,2]

        book_obj=Book.objects.create(title=title,price=price,date=date,publish_id=publish_id)
        book_obj.authors.add(*author_pk_list)


        return redirect("/books/")


    publish_list=Publish.objects.all()
    author_list=Author.objects.all()
    return render(request,"add.html",locals())


def editbook(request,edit_book_id):
    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish_id=request.POST.get("publish_id")
        author_pk_list=request.POST.getlist("author_pk_list") # [1,2]

        Book.objects.filter(pk=edit_book_id).update(title=title,price=price,date=date,publish_id=publish_id)
        book_obj=Book.objects.filter(pk=edit_book_id).first()
        book_obj.authors.set(author_pk_list)


        return redirect("/books/")



    edit_book=Book.objects.filter(pk=edit_book_id).first()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request,"edit.html",locals())