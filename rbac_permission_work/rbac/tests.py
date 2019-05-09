from django.test import TestCase

# Create your tests here.

l = ['/users/', '/users/add', '/users/delete/(\d+)', '/users/edit/(\d+)']

c_path = '/users/delete/9'


import re

flag = False

for i in l:
    promission = f'^{i}$'
    ret = re.match(promission,c_path)
    if ret:
        flag=True
        break

if flag:
    print('success')















