from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Doctor(models.Model):
    doctor_name = models.CharField(verbose_name=_('ФИО доктора'), max_length=100)

    def __str__(self):
        return self.doctor_name

    class Meta:
        verbose_name = _('Доктор')
        verbose_name_plural = _('Врачи')


class Registry(models.Model):
    time = models.TimeField(verbose_name=_('Время'))
    date = models.DateField(verbose_name=_('День'), default=timezone.now)
    doctor = models.ForeignKey(Doctor, verbose_name=_('Доктор'))
    patient_name = models.CharField(verbose_name=_('ФИО'), max_length=100)

    class Meta:
        verbose_name = _('Регистрация')
        verbose_name_plural = _('Регистратура')
        unique_together = ['time', 'date', 'patient_name']
