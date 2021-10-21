from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import *

# Create your views here.
class IndexPage(TemplateView):
    template_name = "index.html"

    def get(self , request, **kwargs) :
        article_data = []
        alt_articles =Article.objects.all().order_by("-created_at")[:9]
        for  article in alt_articles :
            article_data.append({
                "title":article.title,
                "cover":article.cover.url,
                "category":article.category.title,
                "created_at":article.created_at.date(),

            })

        context ={
            "article_data":article_data ,
        }

        return render(request , "index.html", context)