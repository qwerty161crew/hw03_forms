from django.views.generic.base import TemplateView


class Author(TemplateView):
    template_name = 'posts/author.html'


class Stack(TemplateView):
    template_name = 'posts/stack.html'
