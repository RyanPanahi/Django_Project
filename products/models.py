from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categorise')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    updated_time = models.DateTimeField(('create_time'), auto_now=True)

    class Product(models.Model):
        title = models.CharField(_('title'), max_length=50)
        description = models.TextField(_("description"), blank=True)
        avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
        categories = models.ManyToManyField('Category', verbose_name=_('categories'),blank=True)
        is_enable = models.BooleanField(_('is_enable'), default=True)
        create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
        updated_time = models.DateTimeField(('create_time'), auto_now=True)

    class Meta :
        db_table = _('categories')
        verbose_name = _('Category')
        verbose_name = _('categories')

class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('Product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    updated_time = models.DateTimeField(('create_time'), auto_now=True)
