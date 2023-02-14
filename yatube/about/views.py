from django.views.generic.base import TemplateView


class Author(TemplateView):
    template_name = 'posts/author.html'


class Tech(TemplateView):
    template_name = 'posts/tech.html'
