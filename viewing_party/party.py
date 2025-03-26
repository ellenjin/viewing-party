# Assumption: all strings from input are in the expected case
# Assumption: the movie 'rating' is an overall public rating, not personal (will be same for user/friend)

# ------------- WAVE 1 --------------------
#TC: O(1) ; SC: O(1) 
def create_movie(title, genre, rating):
    """
    create a movie dict with three fields provided;
    Parameters: title(str), genere(str), and rating(int);
    Return dict
    """
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
        }
#TC: O(n) (search for value in a list); SC: O(1)
def add_to_watched(user_data, movie):
    """
    Add a movie to user's watched list;
    Parameter: user_data (dict), movie(dict);
    Return user_data(dict)
    """
    if movie not in user_data["watched"]: 
        user_data["watched"].append(movie) 
    return user_data 

#TC: O(n) (search for value in a list); SC: O(1)
def add_to_watchlist(user_data, movie):
    """
    Add a movie to user's watchlist;
    Parameter: user_data (dict), movie(dict);
    Return user_data(dict)
    """
    if movie not in user_data["watchlist"]: 
        user_data["watchlist"].append(movie)
    return user_data

# TC: O(n^2) (O(n) for "in" operator; O(n) for .remove() method); SC: O(n)
# n: length of user's watchlist
def watch_movie(user_data, title):
    """
    Move a movie with a given title from user's watchlist to watched list; 
    Parameter: user_data(dict), title(str)
    Return: user_data(dict)    
    """
    for movie in list(user_data["watchlist"]):
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# TC: O(n) (check presence of movie in a list); SC: O(1)
def get_watched_avg_rating(user_data):
    """
    Find average rating for all movies in user's watched movie list
    Parameters: user_data(dict)
    Return: Average rating (float)
    """
    # for empty list
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0.0
    # iterate through list to add up all ratings
    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    return total_rating / len(user_data["watched"])

#TC: O(n) (iterate through watchedlist) n - length of user's watchedlist;
#SC: O(k) k - size of the genre_count dictionary
def get_most_watched_genre(user_data):
    """
    Find the most watched genre in user's watched movie list;
    Parameter: user_data(dict);
    Return: most_watched_genre(str)
    """
    # check if watched list is empty
    if not user_data["watched"]:
        return None
    # create a dictionary to store genre and counts. 
    genre_count = {}
    highest_count = 0
    most_common_genre = ""
    # assumption: for multiple genres with same highest_count, just return 1st appearance
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
            if genre_count[movie["genre"]] > highest_count:
                highest_count = genre_count[movie["genre"]]
                most_common_genre = movie["genre"]
        else: 
            genre_count[movie["genre"]] = 1
    return most_common_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    copy_of_user_data_watched = list(user_data['watched'])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in copy_of_user_data_watched:
                copy_of_user_data_watched.remove(movie)
    return copy_of_user_data_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    if not user_data["friends"]:
        return friends_unique_watched
    
    for friend in user_data["friends"]:
        if not friend["watched"]:
            continue
        for movie in friend["watched"]:
            if not user_data["watched"] or \
                (movie not in user_data["watched"] and movie not in friends_unique_watched):
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movies = get_friends_unique_watched(user_data)
    movies_copy = list(movies)
    print(movies)
    for movie in movies:
        if movie["host"] not in user_data["subscriptions"]:
            print(movie, movie["host"])
            movies_copy.remove(movie)
        
    return movies_copy

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # get a list of movies that only friends watched
    movies = get_friends_unique_watched(user_data)
    genre = get_most_watched_genre(user_data)
    rec_movies = []

    for movie in movies:
        if movie["genre"] == genre:
            rec_movies.append(movie)
    return rec_movies

def get_rec_from_favorites(user_data):
    # get user's unique watched movies
    # Assumption: if a movie is in user's favorites, must also be in their 'watched'
    user_unique_movies = get_unique_watched(user_data)
    rec_movies = []

    for movie in user_data["favorites"]:
        if movie in user_unique_movies:
            rec_movies.append(movie)
    return rec_movies
