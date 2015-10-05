"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from .views import RegistryView, DoneView, get_times


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RegistryView.as_view(), name='home'),
    url(r'^done/$', DoneView.as_view(), name='registry_done'),
    url(r'^get_times/(?P<date>[\d{2}\.\d{2}\.d\{4}]+)/(?P<doctor>[0-9]+)/$', get_times, name='get_times')

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
