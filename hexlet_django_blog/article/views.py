from django.shortcuts import render
from django.views.generic.base import View

class IndexView(View):
    def get(self, request, tags: str, article_id: int):
        return render(
            request,
            'articles/index.html',
            context = {
                'tags': tags,
                'article_id': article_id,
            }
        )