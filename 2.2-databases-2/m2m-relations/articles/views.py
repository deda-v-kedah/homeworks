from django.shortcuts import render
from pprint import pprint
from articles.models import Article, ArticleScope, Tag


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    article = Article.objects.all()


    context = {'object_list': article,
            
            }




    return render(request, template, context)
