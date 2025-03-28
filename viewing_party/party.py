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

    Assumption: for multiple genres with same highest_count, return 1st appearance.
    """
    if not user_data["watched"]:
        return None
    genre_count = {} # dictionary to store genre and counts.
    highest_count = 0
    most_common_genre = ""
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

# TC: O(n*f*m)
# n -- length of user['watched']
# f -- number of friends
# m -- average number of movies watched by each friend
# SC: O(k) length of unique movies watched by user, worst case O(n)
def get_unique_watched(user_data): 
    """
    Get the movies which the user has watched but their friends have not.
    Parameter: user_data(dict)
    Return: List of user's unique movies(list)
    """
    """
    # older version:
    copy_of_user_data_watched = list(user_data['watched'])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in copy_of_user_data_watched:
                copy_of_user_data_watched.remove(movie)
    return copy_of_user_data_watched
    """
    #updated code 
    # edge cases: empty watched list for user, or no friends;
    if not user_data["watched"]:
        return []
    if not user_data["friends"]:
        return user_data["watched"]
    user_unique_watched = []
    for movie in user_data["watched"]:
        is_unique = True        
        for friend in user_data["friends"]:
            if not friend["watched"]:
                continue
            if movie in friend["watched"]:
                is_unique = False
                break
        if is_unique:
            user_unique_watched.append(movie) 
    return user_unique_watched

# TC: O(f * m * (n + k))
# SC: O(k)
# f -- number of friends
# m -- average number of movies watched by each friend
# n -- length of user['watched']
# k -- length of friends_unque_watched_movie

def get_friends_unique_watched(user_data):
    """
    Get the movies which the friends have watched, but user has not.
    Parameter: user_data(dict)
    Return: List of friends' unique movies(list)
    """
    friends_unique_watched = []
    if not user_data["friends"]:
        return []
    
    for friend in user_data["friends"]:
        if not friend["watched"]:
            continue
        for movie in friend["watched"]:
            if movie in friends_unique_watched:
                continue
            if not user_data["watched"] or movie not in user_data["watched"]:
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# TC: O(f * m * (n + k)) + O(k * l)
# SC: O(k)
# f -- number of friends
# m -- average number of movies watched by each friend
# n -- length of user['watched']
# k -- length of friends_unque_watched_movie
# l -- length of user_data's subscription list;
def get_available_recs(user_data):
    """
    Get a list of reccomended movies that that the user has not watched but a friend has. 
    This movie must be hosted on one of the user's subscription services.
    Parameters: user_data(dict)
    Return: list of reccomended movies(list)
    """
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
    """
    Get movies from the user's most frequently watched genre which the user has not watched,
    but a friend has watched.
    Parameters: user_data(dict)
    Return: List of reccomended movies(list)
    """
    movies = get_friends_unique_watched(user_data) # movies that only friends watched
    genre = get_most_watched_genre(user_data)
    rec_movies = []

    for movie in movies:
        if movie["genre"] == genre:
            rec_movies.append(movie)
    return rec_movies

def get_rec_from_favorites(user_data):
    """
    Get movies from the user's favorite movies that have not been watched by any friends. 
    Parameters: user_data(dict)
    Return: List of reccomended movies(list)

    Assumption: if a movie is in user's favorites, must also be in their watched (user_data["watched"])
    """
    user_unique_movies = get_unique_watched(user_data) # user's unique watched movies
    rec_movies = []

    for movie in user_data["favorites"]:
        if movie in user_unique_movies:
            rec_movies.append(movie)
    return rec_movies
