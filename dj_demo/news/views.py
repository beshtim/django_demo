from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.urls import  reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = {"title":'Главная'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DeleteView):
    model = News
    # pk_url_kwarg = 'news_id' # пробросить название аргумента из urls
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

    # custom redirect not using get_absolute_url from models.Model
    # success_url: reverse_lazy("home")


# def index(request):
#     news = News.objects.all()    
#     cont = {
#         "news": news,
#         'title': 'Новости',
#         }
#     return render(request, 'news/index.html', cont)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     return render(request, 'news/category.html', {'news': news})

# def view_news(request, pk):
#     # news_item = News.objects.get(pk=pk)
#     news_item = get_object_or_404(News, pk=pk)
#     return render(request, 'news/view_news.html', {'news_item':news_item})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = NewsFormNotConnectedWithDB.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#         return render(request, 'news/add_news.html', {'form': form})