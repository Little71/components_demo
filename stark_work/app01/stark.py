from stark.service.stark import site, ModelStark

from django.urls import reverse
from .models import *

from django.utils.safestring import mark_safe


class BookConfig(ModelStark):
    list_display = ['title', 'price','publish','authors']
    list_display_links = ['title']

    def patch_init(self, request, queryset):
        print(queryset)
        queryset.update(price=100)

    actions = [patch_init]
    list_filter = ['publish','authors']


class PublishConfig(ModelStark):
    list_display = ['nid', 'name', 'city', 'email']
    list_display_links = ['name']


site.register(Book, BookConfig)

site.register(Publish, PublishConfig)
site.register(Author)
site.register(AuthorDetail)
