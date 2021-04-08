from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import our models
from .models import Artist

# import our forms
from .forms import ArtistForm

# Create your views here.
class ArtistList(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "tunr/artist_list.html"

class ArtistDetail(DetailView):
    model = Artist
    context_object_name = "artist"
    template_name = "tunr/artist_detail.html"

class ArtistCreate(CreateView):
    model = Artist
    context_object_name = 'artist'
    template_name = "tunr/artist_form.html"
    fields = ['name', 'bio']

class ArtistEdit(UpdateView):
    model = Artist
    context_object_name = 'artist'
    template_name = "tunr/artist_form.html"
    fields = ['name', 'bio']

class ArtistDelete(DeleteView):
    model = Artist
    context_object_name = 'artist'
    success_url = reverse_lazy('artist_list')
