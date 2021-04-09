from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist-list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist-detail'),
    path('albums/', views.AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>', views.AlbumDetail.as_view(), name='album-detail')
]

