from django.shortcuts import render, HttpResponse

# Create your views here.
from rbac.models import User, Role, Promission


def users(request):
    user_list = User.objects.all()
    return render(request, 'users.html', locals())

def roles(request):
    user_list = Role.objects.all()

    return render(request, 'users.html', locals())

def add_user(request):
    return HttpResponse('adduser')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username,pwd=pwd).first()
        print(user)
        if user:
            return HttpResponse('登录成功')
    return render(request, 'login.html')