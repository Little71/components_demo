from django.contrib import admin

# Register your models here.


from .models import User,Role,Permission

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)