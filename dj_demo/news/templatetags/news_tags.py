from atexit import register
from django import template
from news.models import Category

register = template.Library()

@register.simple_tag(name='get_list_cats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1="hello"):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1': arg1}