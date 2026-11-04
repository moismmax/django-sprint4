"""Представления для статических страниц приложения pages."""

from django.shortcuts import render


def about(request):
    """Возвращает страницу 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """Возвращает страницу 'Наши правила'."""
    return render(request, 'pages/rules.html')
