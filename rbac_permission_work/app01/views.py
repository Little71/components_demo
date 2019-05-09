import re

from django.shortcuts import render, HttpResponse

# Create your views here.
from rbac.models import User, Role, Permission

class Per

def users(request):
    user_list = User.objects.all()
    permission_list = request.session.get('permission_list')
    print(permission_list)

    user_id = request.session.get('user_id')
    user=User.objects.filter(id=user_id).first()
    return render(request, 'users.html', locals())


def roles(request):
    role_list = Role.objects.all()

    return render(request, 'roles.html', locals())


def add_user(request):
    return HttpResponse('adduser')

def del_user(request,id):
    return HttpResponse(f'delete user {id}')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username, pwd=pwd).first()
        if user:
            from rbac.service.permission import initila_session
            initila_session(request, user)
            return HttpResponse('登录成功')
    return render(request, 'login.html')
