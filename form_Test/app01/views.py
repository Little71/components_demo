from django.shortcuts import render, redirect
from django import forms
from django.forms import widgets
from django.forms import ModelForm
# Create your views here.

from .models import Book, Publish, Author


# class BookForm(forms.Form):
#     title = forms.CharField(max_length=32, label='书籍名')
#     price = forms.DecimalField(max_digits=8, decimal_places=2, label='价格')
#     date = forms.DateField(widget=widgets.TextInput(attrs={'type': 'date'}), label='日期')
#
#     #渲染select标签   choices里面的元组 渲染 option标签
#     # gender = forms.ChoiceField(choices=((1, '男'), (2, '女'), (3, '外星人')))
#
#     # publish = forms.ChoiceField(choices=Publish.objects.all().values_list('pk','name'))
#
#     publish = forms.ModelChoiceField(queryset=Publish.objects.all())
#     author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': '书籍名',
            'price':'价格',
        }
        widgets={
            'date':widgets.TextInput(attrs={'type':'date'})
        }


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', locals())


def addbook(request):
    # publish_list = Publish.objects.all()
    # author_list = Author.objects.all()
    # if request.method == "POST":
    #     title = request.POST.get('title')
    #     price = request.POST.get('price')
    #     date = request.POST.get('date')
    #     publish_id = request.POST.get('publish_id')
    #     author_pk_list = request.POST.getlist('author_pk_list')
    #     bookobj = Book.objects.create(title=title, price=price, date=date, publish_id=publish_id)
    #     # add() 用于给多对多绑定关系 在第三方的关系表上生成对应的记录
    #     # set() 编辑的时候使用，删除原有的，在新增记录
    #     bookobj.authors.add(*author_pk_list)
    #     return redirect('/books/')
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # title = form.changed_data.get('title')
            # price = form.changed_data.get('price')
            # date = form.changed_data.get('date')
            # publish = form.changed_data.get('publish')
            # authors = request.POST.getlist('authors')
            # bookobj = Book.objects.create(title=title, price=price, date=date, publish=publish)
            # bookobj.authors.add(*publish)
            return redirect('/books/')
    form = BookForm()
    return render(request, 'addbook.html', locals())


def editbook(request, pk):
    edit_book = Book.objects.filter(pk=pk).first()
    # publish_list = Publish.objects.all()
    # author_list = Author.objects.all()

    if request.method == "POST":
        form = BookForm(request.POST, instance=edit_book)
        if form.is_valid():
            form.save()
            # title = request.POST.get('title')
            # price = request.POST.get('price')
            # date = request.POST.get('date')
            # publish_id = request.POST.get('publish_id')
            # author_pk_list = request.POST.getlist('author_pk_list')
            #
            # Book.objects.filter(pk=pk).update(title=title, price=price, date=date, publish_id=publish_id)
            # bookobj = Book.objects.filter(pk=pk).first()
            # bookobj.authors.set(author_pk_list)
            return redirect('/books/')

    form = BookForm(instance=edit_book)  # 原生的form不能处理编辑的初始数据，只能自己写

    return render(request, 'editbook.html', locals())
