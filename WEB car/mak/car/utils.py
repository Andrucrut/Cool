from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить машину", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Избранное", 'url_name': 'favorites'}
]


class DataMixin:
        def get_user_context(self, **kwargs):
            context = kwargs
            cats = Category.objects.all()
            context['menu'] = menu
            context['cats'] = cats
            if 'cat_selected' not in context:
                context['cat_selected'] = 0
            return context
