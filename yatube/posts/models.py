from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Group(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.TextField(_('description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')


class Post(models.Model):
    text = models.TextField(_('text'))
    pub_date = models.DateTimeField(_('pub_date'), auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
