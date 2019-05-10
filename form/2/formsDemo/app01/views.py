from django.shortcuts import render,redirect

# Create your views here.

from .models import *

from django import forms
from django.forms import widgets

class BookForm(forms.Form):
    title = forms.CharField(max_length=32,label="书籍名称")
    price = forms.DecimalField(max_digits=8, decimal_places=2,label="价格")  # 999999.99
    date = forms.DateField(label="日期",
        widget=widgets.TextInput(attrs={"type":"date"})
    )

    #gender=forms.ChoiceField(choices=((1,"男"),(2,"女"),(3,"其他")))
    #publish=forms.ChoiceField(choices=Publish.objects.all().values_list("pk","title"))
    publish=forms.ModelChoiceField(queryset=Publish.objects.all())
    authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())






def books(request):
    book_list=Book.objects.all()
    return render(request,"books.html",locals())


def addbook(request):
    if request.method=="POST":
        form = BookForm(request.POST)

        if form.is_valid():

            print("cleaned_data",form.cleaned_data)
            title=form.cleaned_data.get("title")
            price=form.cleaned_data.get("price")
            date=form.cleaned_data.get("date")
            publish=form.cleaned_data.get("publish")
            authors=form.cleaned_data.get("authors") # [1,2]

            book_obj=Book.objects.create(title=title,price=price,date=date,publish=publish)
            book_obj.authors.add(*authors)


            return redirect("/books/")

    form=BookForm()
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

    form=BookForm()
    return render(request,"edit.html",locals())