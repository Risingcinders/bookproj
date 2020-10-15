from django.urls import path
from . import views

urlpatterns = [
    path('', views.booklist),
    path('addbook', views.addbook),
    path('<int:bookid>', views.bookdetail),
    path('<int:bookid>/addfavorite', views.addfavorite),
    path('<int:bookid>/delete', views.bookdelete),
    path('<int:bookid>/update', views.bookupdate),
    path('<int:bookid>/unfavorite', views.unfavorite)
]
