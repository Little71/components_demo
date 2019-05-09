def initila_session(request, user):
    permissions = user.roles.all().values('permissions__url').distinct()
    permission_list = []
    for item in permissions:
        permission_list.append(item['permissions__url'])
    request.session['user_id'] = user.pk
    request.session['permission_list'] = permission_list
