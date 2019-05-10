import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class ValiPermission(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path
        valid_url_list = ['/login/', '/reg/', '/admin/.*']
        for valid_url in valid_url_list:
            ret = re.match(valid_url, current_path)
            if ret:
                return

        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')

        # permission_list = request.session.get('permission_list', '')
        # for i in permission_list:
        #     promission = f'^{i}$'
        #     ret = re.match(promission, current_path)
        #     if ret:
        #         flag = True
        #         break
        # if not flag:
        #     return HttpResponse('没有访问权限')

        permission_dict = request.session.get('permission_dict', dict())
        for item in permission_dict.values():
            for url in item['urls']:
                promission = f'^{url}$'
                ret = re.match(promission, current_path)
                if ret:
                    request.actions = item.get('actions')
                    return
        return HttpResponse('没有访问权限')
