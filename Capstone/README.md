#Project_overview
1. "Movie Night" project shows recommendations for the movies and series by showing the popular, top rated, newly released movies and series according to the database of (the movie database (tmdb)).

2. Users can also search for movies using this website to show information like its rate on tmdb, the famous tagline of the work release date, short, description of the work and an official link where the user can visit the homepage of the work .

3. If the user is logged in they can write their own review on the movie/series easily and publish it on the movie page.

4. All Reviews page shows all reviews of all users showing the movie that they mention and a link to visit the movie page with pagination of 5 reviews per page and sorted by the latest.

5. The user can add movies and series that they like to their watchlist then they can remove it anytime.

6. Finally, the front-end is designed in dark mode and the grid of bootstrap and the website is mobile responsive.
--------------------------------------------------------------------------------------------
#urls.py
1. /login : calls login_view function from views.

2. /logout : calls login_view function from views.

3. /register : calls register function from views.

4. /(no parameters)  : loads index by calling index function from views.

5. /type(string) (whether it is a movies or a series) / id(integer) of the movie or series :  which calls GetMovie function and passes type and id as parameters which will be  used in the rendered template to use it in the fetched url from the tmdb API.

6. /CreateReview : calls CreateReview function from views.

7. /All_Reviews : calls AllReviews function from views which renders a page of all reviews of all users.

8. Add/id(integer) of the movie or series/type(string) (whether it is a movies or a series) : calls AddToWatchListFunction function and passes the type and id as parameters to that function in the views which add a movie or series to the watchlist of the user and create its model (watchlistlink) using these parameters.

9. Remove/id(integer) of the movie or series /type(string) (whether it is a movies or a series) : calls RemoveFromWatchListFunction function and passes the type and id as parameters to that function in the views which get the watchlist item which contains that contains the movie or series in that user's watchlist and delete it.

10. /MyWatchlist : which calls the GetWatchList function from views which renders the Watchlist page.

*** more info about function in views.py section in this page ***
--------------------------------------------------------------------------------------------
#views.py
1. index(request) : renders the index.html from the templates.

2. GetMovie (request, Type, MovieId ) : renders MoviePage.html which passes the Type(movie or series) parameter and MovieID parameter as django template variables in that will be used in the URL which is fetched to get data through the tmdb API and also gets the reviews of that movie or series by filtering Review model objest which has that type and id.

3. AllReviews(request) : renders the AllReviews.html and passes the reviews as django template variables but by using pagination so it passes just the required 5 or less reviews.

4. CreateReview(request) : redirects the user to "/Type(movie or series) /id of that movie or series" and it accepts POST method only as it gets the data from the form of creating review in the MoviePage.html and creates Review model object using this data.

5. AddToWatchListFunction(request,,movieId,userName,Type) : It creates a watchListLink model object using the userName is the username of the logged in user, movie id and type(movie or series).

5. RemoveFromWatchListFunction(request,,movieId,userName,Type) : It removes the watchListLink model object whose userName is the username of the logged in user, movie id is the passed id as parameter and type(movie or series).

6. GetWatchList(request) : renders the WatchList.html template passing in it the watchListLink objects of the requesting user.
--------------------------------------------------------------------------------------------
#models.py
1. Review model: which contains publisher name, description, name of the mentioned movie ,the work type whether it is a movie or series and the movie id on tmdb as attributes.

2. User model : besides default attributes of abstract User, Watch list is added as an attribute which is a Foreign Key from watchListLink model.

3. watchListLink model : is just a linkage model which links a user to a movie representing it by its id and it type in order to create a watchlist item.
--------------------------------------------------------------------------------------------
#front-end
1. index.html : It's the home page of the website. It starts with welcome animation then it shows the top 10 movies, most popular movies / series and recent movies . This info is fetched by using fetch statement of javascript from the tmdb API . It includes a search bar that take the input and pass it as a parameter in the URL of fetching the top 10 matching searches and show them in a grid style . The case that the results may be less than 10 is handled as the remaining results will be under the name "no result" with "no photo" sign. The div "Welcome" renders for the first 4 sec then its display becomes none then the "IndexBody" div display becomes block to render the grids of the movies and series and the search bar .  The arrangement of movies are arranged in tens using grid mode .

2. AllReviews.hmtl : It shows all reviews of all users where the reviews is rendered as a bootstrap box its title is the user name, it's subtitle is a link the reviewed movie page and its body is the review . It gets its information from the variable "All_Reviews" passed by the python function in the views as django template variable . It shows the reviews in paginated way 5 per page.

3. WatchList.html : It shows all the listed movies and series by the logged in user . It gets the id, the name, the type of the movie/series through the template variable wls passed from the views function then fetch it to get its info from the API and show them  in an arranged grid mode .

4. MoviePage.html : It shows all the movie/series details by fetching this info from the API the rendering these details which are : the poster, title, the famous tagline of the work, description ,rate of tmdb, release date and the official homepage . It renders all the reviews on that movie/series . It shows the Add/Remove to/from the watchlist .

5. layout.html : The base layout of all the templates of the website which sows a navigation bar to navigate between home, All Reviews, WatchList, login, logout and register.
*** the 3 files : layout.html, register.html and login.html aren't so different from the previous projects except in the dark mode and some other things ***
--------------------------------------------------------------------------------------------
#logout_view
the non logged in user can't write a review and can't add to watchlist but can access all other features.
