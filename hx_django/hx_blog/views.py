from django.shortcuts import render

from django.http import Http404
from .models import Album


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'hx_blog/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist as e:
        raise Http404('album not exit')
    return render(request, 'hx_blog/detail.html', {'album': album})
