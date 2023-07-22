from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("",views.index,name="index"),
    path("<str:Type>/<int:MovieId>",views.GetMovie,name="MoviePage"),
    path("CreateReview", views.CreateReview, name="CreateReview"),
    path("All_Reviews", views.AllReviews, name="All_Reviews"),
    path("Add/<int:movieId>/<str:Type>",views.AddToWatchListFunction,name="WatchList"),
    path("Remove/<int:movieId>/<str:Type>",views.RemoveFromWatchListFunction,name="WatchList"),
    path("MyWatchlist",views.GetWatchList,name="GetWatchList"),
    ]
