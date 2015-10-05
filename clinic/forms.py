from django.utils.formats import date_format
from django.utils import timezone
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Registry


def make_time_choices(date=None or timezone.now().date(), doctor=None):
    if isinstance(date, str):
        date = timezone.datetime.strptime(date, "%d.%m.%Y").date()

    time_sheet = ['%s:00' % t for t in range(9, 19)]
    registry_sheet = list(map(lambda x: '%s:00' % x['time'].hour,
                              Registry.objects.filter(time__in=time_sheet, date=date, doctor=doctor).values('time')))

    return [(t, t) for t in list(filter(lambda x: x not in registry_sheet, time_sheet))]


class RegistryForm(forms.ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        super(RegistryForm, self).__init__(data, *args, **kwargs)
        if data:
            self.fields['time'].widget = forms.RadioSelect(
                choices=make_time_choices(data.get('date', None), data.get('doctor', None)))

    def clean_date(self):
        date = self.cleaned_data['date']
        if date.weekday() >= 5:
            raise forms.ValidationError(
                _('%s поликлиника не работает, суббота и воскресенье выходной.' % date_format(date)))
        if date < timezone.now().date():
            raise forms.ValidationError(
                _('Нельзя запланировать дату из прошлого.'))
        return date

    class Meta:
        model = Registry
        fields = ['date', 'doctor', 'time', 'patient_name']
        widgets = {
            'time': forms.RadioSelect(choices=make_time_choices())
        }