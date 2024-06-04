from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns=[
  path('create-book/', views.createRSBook, name='createbook'),
  path('create-author/', views.createRSAuthor, name='createauthor'),
  path('list-books/', views.listBooks, name='listbooks'),
  path('details/<int:book_id>/', views.bookDetails, name='bookdetails'),
  path('delete/<int:book_id>/', views.deleteBook, name='deletebook'),
  path('update/<int:book_id>/', views.updateBook, name='updatebook'),
  path('search-book/', views.searchBook, name='searchbook'),
  path('', views.main, name='main'),
  path('ddauthor/', views.author, name='author'),
  path('real-story-book/', views.realstoryBook, name='real_story_books'),
  path('fiction-book/', views.fictionBook, name='fictional_story_books'),
  path('search/realstory/', views.real_story_books, name='search_real'),
  path('search/fiction/', views.fiction_books, name='search_fiction'),
  path('genres/', views.genre, name='genres'),
  path('genre-comedy/', views.comedy, name='genre_comedy'),
  path('genre-action/', views.action, name='genre_action'),
  path('genre-crime/', views.crime, name='genre_crime'),
  path('genre-horror/', views.horror, name='genre_horror'),
  path('genre-romance/', views.romance, name='genre_romance'),
  path('genre-adventure/', views.adventure, name='genre_adventure'),
  path('genre-thriller/', views.thriller, name='genre_thriller'),
  path('genre-sports/', views.sports, name='genre_sports'),
  path('genre-inspirational/', views.inspirational, name='genre_inspirational'),

]

