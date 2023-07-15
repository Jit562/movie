from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
import requests

from .models import MovieModel
from django.core.paginator import Paginator

from django.views.generic import ListView


# Create your views here.

def MovieView():
   
    URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key=ff08342fc25547b019039b0b077c0710&language=en-US&page=1'

    response = requests.get(URL)
    results = response.json()['results']
  
    for movie in results:

        if not MovieModel.objects.filter(
            title =movie["title"],
            vote_average=movie["vote_average"],
            vote_count=movie["vote_count"],
            release_date=movie["release_date"],
            overview=movie["overview"],
            popularity=movie["popularity"],
            poster_path=movie["poster_path"]
            ).exists():

            MovieModel.objects.create(
                title =movie["title"],
                vote_average=movie["vote_average"],
                vote_count=movie["vote_count"],
                release_date=movie["release_date"],
                overview=movie["overview"],
                popularity=movie["popularity"],
                poster_path=movie["poster_path"]
            )

            print("saved")

        else:
            print("Data already exists")

           
def MovieList(request): 
    movies = MovieModel.objects.all().order_by('title')
    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    get_page = paginator.get_page(page_number)
    total_page = get_page.paginator.num_pages

    context = {
        'get_page':get_page,
        'lastpage': total_page,
        'totalpagelist':[n+1 for n in range(total_page)]
    }

    return render(request, 'movie.html', context)   

def moviedetails(request):
    if 'q' in request.GET:
        q = request.GET['q']
        movies = MovieModel.objects.filter(title__icontains=q)
    else:
        movies = MovieModel.objects.all()

    context = {
        'movies':movies,
    }    
    return render(request, 'index.html', context)


def movieslist(request):
    URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key=ff08342fc25547b019039b0b077c0710&language=en-US&page=2'

    response = requests.get(URL)
    results = response.json()['results']

    context = {
        'results':results
    }
    return render(request, 'home.html', context)

        

    

