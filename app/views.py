from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from app.forms import ArtistForm
from app.models import Artist


class IndexView(TemplateView):
    template_name = 'index.html'


class ArtistCreateView(CreateView):
    form_class = ArtistForm
    template_name = 'artisteCreate.html'


class OrganizerCreateView(TemplateView):
    template_name = 'organizerCreate.html'
