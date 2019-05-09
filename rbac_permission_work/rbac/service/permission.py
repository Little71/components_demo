def initila_session(request, user):
    # 1
    # permissions = user.roles.all().values('permissions__url').distinct()
    # permission_list = []
    # for item in permissions:
    #     permission_list.append(item['permissions__url'])
    # request.session['user_id'] = user.pk
    # request.session['permission_list'] = permission_list

    # 2
    permissions = user.roles.all().values(
        'permissions__url',
        'permissions__group_id',
        'permissions__action',
    ).distinct()

    '''
    <QuerySet [{'permissions__url': '/users/', 'permissions__group_id': 2, 'permissions__action': 'list'},
     {'permissions__url': '/users/add', 'permissions__group_id': 2, 'permissions__action': 'add'}, 
     {'permissions__url': '/users/edit/(\\d+)', 'permissions__group_id': 2, 'permissions__action': 'edit'},
      {'permissions__url': '/users/delete/(\\d+)', 'permissions__group_id': 2, 'permissions__action': 'delete'}]>'''

    permission_dict = {}
    for item in permissions:
        gid = item.get('permissions__group_id')
        if gid in permission_dict.keys():
            permission_dict[gid]['urls'].append(item.get('permissions__url'))
            permission_dict[gid]['action'].append(item.get('permissions__action'))
        else:
            permission_dict[gid] = {
                'urls': [item.get('permissions__url')],
                'actions': [item.get('permissions__action')],
            }
    request.session['user_id'] = user.pk
    request.session['permission_dict'] = permission_dict
