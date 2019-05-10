from django import template

register = template.Library()

@register.inclusion_tag('rbac/menu.html')
def get_num(request):
    menu_list_permissions = request.session.get('menu_list_permissions')
    return {'menu_list_permissions':menu_list_permissions}