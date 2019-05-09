import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class ValiPermission(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path
        flag = False
        valid_url_list = ['/login/', '/reg/','/admin/.*']
        for valid_url in valid_url_list:
            ret = re.match(valid_url, current_path)
            if not ret:
                return

        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login/')

        permission_list = request.session.get('permission_list', '')
        for i in permission_list:
            promission = f'^{i}$'
            ret = re.match(promission, current_path)
            if not ret:
                flag = True
                break

        if not flag:
            return HttpResponse('没有访问权限')
