from django.db import models
from django import forms
from django.urls import reverse

from app.models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
