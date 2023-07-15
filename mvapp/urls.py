from django.urls import path
from mvapp.views import *

urlpatterns = [
    path('movie/', MovieView),
    path('movie/list/', MovieList, name='movie'),
    path('search/', moviedetails, name='search'),
    path('mvlist/', movieslist, name='mvlist'),

]