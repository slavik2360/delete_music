# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import (
    HttpResponse,
    JsonResponse
)
from django.shortcuts import render
from django.views import View

# First party
from abstracts.utils import get_object_or_404

# Local
from .models import (
    Album,
    Song
)


#-------------------------------------------------
# Example of Function Based View (FBV)
#
# def index(request: WSGIRequest) -> HttpResponse:
#     albums: QuerySet[Album] = Album.objects.all()
#     context: dict[str, QuerySet[Any]] = {
#         'albums': albums
#     }
#     return render(
#         request,
#         'main/index.html',
#         context
#     )


class IndexView(View):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, QuerySet[Any]]:
        albums: QuerySet[Album] = Album.objects.all()
        context: dict[str, QuerySet[Any]] = {
            'albums': albums
        }
        return context

    def get(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data()
        return render(
            request,
            self.template_name,
            context
        )


class DetailView(View):
    template_name = 'main/detail.html'

    def get_context_data(
        self,
        album_id: int,
        **kwargs: Any
    ) -> dict[str, QuerySet[Any]]:
        album: Album = get_object_or_404(
            Album,
            album_id
        )
        user: User = self.request.user
        context: dict[str, Any] = {
            'album': album,
            'user': user
        }
        return context

    def get(
        self,
        request: WSGIRequest,
        album_id: int,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data(
            album_id
        )
        return render(
            request,
            self.template_name,
            context
        )


class DeleteView(View):
    template_name = 'main/detail.html'

    def get_context_data(
        self,
        album_id: int,
        **kwargs: Any
    ) -> dict[str, QuerySet[Any]]:
        album: Album = get_object_or_404(
            Album,
            album_id
        )
        context: dict[str, QuerySet[Any]] = {
            'album': album
        }
        return context

    def post(
        self,
        request: WSGIRequest,
        album_id: int,
        song_id: int,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data(
            album_id
        )
        song: Song = context['album'].song_set.get(
            id=song_id
        )
        song.delete()

        return render(
            request,
            self.template_name,
            context
        )


def create_song(
    request: WSGIRequest,
    album_id: int
) -> HttpResponse:
    pass


def favorite(
    request: WSGIRequest,
    song_id: int
) -> JsonResponse:
    song: Song = get_object_or_404(
        Song,
        song_id
    )
    try:
        song.is_favorite = True if song.is_favorite is False else False
        song.save(update_fields=('is_favorite',))
    except (
        KeyError,
        Song.DoesNotExist
    ):
        return JsonResponse({'success': False})
    return JsonResponse({'success': True})
