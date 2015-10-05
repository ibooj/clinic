import json

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.utils.formats import date_format, time_format

from .forms import RegistryForm, make_time_choices


class RegistryView(CreateView):
    template_name = 'registry.html'
    form_class = RegistryForm
    success_url = '/done/'

    def form_valid(self, form):
        messages.success(self.request,
                         _('Вы записаны к доктору %s на %s часов.' % (
                            date_format(form.cleaned_data['date']), time_format(form.cleaned_data['time']))))
        return super(RegistryView, self).form_valid(form)


class DoneView(TemplateView):
    template_name = 'done.html'


def get_times(request, date, doctor):
    return HttpResponse(json.dumps(list(map(lambda x: x[0], make_time_choices(date, doctor)))),
                        content_type="application/json")
