from django.shortcuts import render, redirect
from django.views import View

# import our models
from .models import Artist

# import our forms
from .forms import ArtistForm

# Create your views here.
class ArtistList(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'tunr/artist_list.html', {'artists': artists})

class ArtistCreate(View):
    def get(self, request):
        form = ArtistForm()
        return render(request, 'tunr/artist_form.html', {'form': form})

    def post(self, request):
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
        else:
            return render(request, 'tunr/artist_form.html', {'form': form})

class ArtistDetail(View):
    def get(self, request, pk):
        artist = Artist.objects.get(id=pk)
        return render(request, 'tunr/artist_detail.html', {'artist': artist})

class ArtistEdit(View):
    def get(self, request, pk):
        artist = Artist.objects.get(id=pk)
        form = ArtistForm(instance=artist)
        return render(request, 'tunr/artist_form.html', {'form': form})
    def post(self, request, pk):
        artist = Artist.objects.get(id=pk)
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
        else:
            form = ArtistForm(instance=artist)
            return render(request, 'tunr/artist_form.html', {'form': form})

class ArtistDelete(View):
    def get(self, request, pk):
        artist = Artist.objects.get(id=pk)
        artist.delete()
        return redirect('artist_list')
