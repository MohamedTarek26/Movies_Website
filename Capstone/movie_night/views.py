from __future__ import print_function
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect ,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import sys
# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movie_night/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movie_night/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("register"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "movie_night/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movie_night/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movie_night/register.html")

def index(request):

    return render(request,"movie_night/index.html")

def GetMovie(request,Type,MovieId):
    return render(request,"movie_night/MoviePage.html",{"MovieId":MovieId,"Type":Type,"REVIEWS":Review.objects.filter(movieId=MovieId)})

def AllReviews(request):
    R=Review.objects.all().order_by('id').reverse()
    p = Paginator(R, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request,"movie_night/AllReviews.html",{"ALL_REVIEWS":page_obj})
@csrf_exempt
def CreateReview(request):
    if(request.method=="POST"):
        CONTENT=request.POST["Post_Content"]
        MOVIENAME=request.POST["movieName"]
        MOVIEID=request.POST["movieId"]
        MOVIETYPE=request.POST["movieType"]
        new=Review(publisher=request.user,Post_text=CONTENT,movieName=MOVIENAME,movieId=MOVIEID,movieType=MOVIETYPE)
        new.save()
        return HttpResponseRedirect(reverse('MoviePage', args=[MOVIETYPE,MOVIEID]))
    else:
        return HttpResponse("SORRY POST METHOD ONLY")
@login_required
def AddToWatchListFunction(request,movieId,Type):

    u= request.user
    USER=User.objects.get(username=u)
    new=watchListLink(p=USER,m=movieId,t=Type)
    new.save()
    return HttpResponse("ADDED")
@login_required
def RemoveFromWatchListFunction(request,movieId,Type):
    u= request.user
    USER=User.objects.get(username=u)
    new=watchListLink.objects.get(p=USER,m=movieId,t=Type)
    new.delete()
    return HttpResponse("REMOVED")

def GetWatchList(request):
    print(watchListLink.objects.all().count(), file=sys.stderr)
    return render(request,"movie_night\WatchList.html",{"WATCHLIST":watchListLink.objects.filter(p=request.user)})
