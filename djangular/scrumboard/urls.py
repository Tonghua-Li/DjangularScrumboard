from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urls import template_name

from .api import ListApi, CardApi
urlpatterns = [
    url(r'^lists$', ListApi.as_view()), # exactly match list
    url(r'^cards$', ListApi.as_view()),
    url(r'^home$', TemplateView.as_view(template_name="scrumboard/home.html")),
]