#coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class Slide(models.Model):
    text = models.TextField(_(u"Текст"))

    class Meta:
        verbose_name = _(u"Слайд")
        verbose_name_plural = _(u"Слайды")

    def __unicode__(self):
        return "%s %s" % (self.id, self.text)


class Variant(models.Model):
    variantId = models.IntegerField(_(u"Вариант ответа"))
    slide = models.ForeignKey(Slide, verbose_name=_(u"Слайд"), related_name='variants', blank=True, null=True)
    points = models.IntegerField(_(u"Очки"))
    text = models.TextField(_(u"Текст"))
    comment = models.TextField(_(u"Комментарий"))
    nextId = models.IntegerField(_(u"Следующий слайд"), blank=True, null=True)

    class Meta:
        verbose_name = _(u"Вариант")
        verbose_name_plural = _(u"Варианты")

    def __unicode__(self):
        return "%s %s" % (self.slide, self.variantId)


class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Пользователь"))
    points = models.IntegerField(_(u"Очки"))

    class Meta:
        verbose_name = _(u"Попытка")
        verbose_name_plural = _(u"Попытки")

    def __unicode__(self):
        return "%s %s" % (self.user, self.points)
