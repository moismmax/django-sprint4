"""Представления для приложения blog."""

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def index(request):
    """Возвращает главную страницу с последними публикациями."""
    template = 'blog/index.html'

    # Получаем все опубликованные посты, дата публикации не в будущем,
    # и категория которых тоже опубликована.
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    """Возвращает страницу с подробным описанием публикации."""
    template = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.select_related('category').filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        ),
        pk=id
    )

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Возвращает страницу категории с её публикациями."""
    template = 'blog/category.html'

    # Ищем категорию по слагу. Если она не опубликована — вернется 404.
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    # Получаем посты этой категории с учетом флагов и даты.
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
