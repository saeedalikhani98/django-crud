from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Movie


def index(request):
    movies = Movie.objects.all()

    context = { 'movies': movies }

    if 'edit_id' in request.GET:
        context = { **context, 'message': 'edit', 'message_id': request.GET['edit_id'] }
    
    if 'delete_id' in request.GET:
        context = { **context, 'message': 'delete', 'message_id': request.GET['delete_id'] }


    return render(request, "movies/index.html", context)


def create_new(request):

    if request.method == 'POST':
        movie = Movie(
            title=request.POST['title'],
            synopsis=request.POST['synopsis'],
            actors=request.POST['actors'],
            genre=request.POST['genre'],
            duration=request.POST['duration']
        )
        movie.save()
        return HttpResponseRedirect(reverse('movies_index') + '?edit_id=' + str(movie.id))

    context = {}
    template = loader.get_template('movies/create.html')
    return HttpResponse(template.render(context, request))


def view(request, movie_id=None):
    movie = Movie.objects.filter(id=movie_id).first()
    context = { 'movie': movie }
    return render(request,"movies/view.html",context)


def edit(request, movie_id=None):
    movie = Movie.objects.filter(id=movie_id).first()

    if request.method == 'POST':
        movie.title=request.POST['title']
        movie.synopsis=request.POST['synopsis']
        movie.actors=request.POST['actors']
        movie.genre=request.POST['genre']
        movie.duration=request.POST['duration']
        movie.save()
        return HttpResponseRedirect(reverse('movies_index') + '?edit_id=' + str(movie.id))

    context = { 'movie': movie }
    return render(request, "movies/edit.html", context)


def delete(request, movie_id=None):
    movie = Movie.objects.filter(id=movie_id).first()

    if request.method == 'POST':
        movie = Movie.objects.filter(id=movie_id)
        movie.delete()
        return HttpResponseRedirect(reverse('movies_index') + '?delete_id=' + str(movie_id))

    context = { 'movie': movie }
    return render(request,"movies/delete.html",context)