from django.shortcuts import render

from categories.models import Category


def index(request):
    category_all = Category.objects.all()

    return render(request, 'index.html', locals())


def category_detail(request, id):
    category = Category.objects.get(id=id)

    return render(request, 'detail.html', locals())
