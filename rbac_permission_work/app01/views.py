import re

from django.shortcuts import render, HttpResponse

# Create your views here.
from rbac.models import User, Role, Permission


def users(request):
    user_list = User.objects.all()
    return render(request, 'users.html', locals())


def roles(request):
    role_list = Role.objects.all()

    return render(request, 'roles.html', locals())


def add_user(request):
    permission_list = request.session['permission_list']
    current_path = request.path
    flag = False
    for i in permission_list:
        promission = f'^{i}$'
        ret = re.match(promission, current_path)
        if not ret:
            flag = True
            break

    if not flag:
        return HttpResponse('没有访问权限')
    return HttpResponse('adduser')


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
