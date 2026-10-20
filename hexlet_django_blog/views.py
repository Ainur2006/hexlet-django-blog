from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View


class IndexView(View):

    def get(self, request):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)


def about(request):
    return render(request, "about.html")