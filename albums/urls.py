from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
    path('artists/<int:pk>/edit', views.ArtistEdit.as_view(), name='artist_edit'),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist_delete')
]
