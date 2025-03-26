#Assumption: all strings from input are in the expected case

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
        }

def add_to_watched(user_data, movie):
    # assume user_data has key 'watched'
    if movie not in user_data["watched"]: # check if duplicate exists, all 3 key values must match to be a duplicate
        user_data["watched"].append(movie) # access this if the movie is NOT a duplicate
    return user_data 

def add_to_watchlist(user_data, movie):
    if movie not in user_data["watchlist"]: # if not a duplicate
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]: # do we need to be concerned about modifying list as we're iterating?
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # for empty list
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0.0
    # iterate through list to add up all ratings
    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
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
    # write a test later for same title movie, different rating
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
    # In most frequently watched genre, find list of reccomended movies.
    # Add to reccomended if:
    #   - User has not watched
    #   - One of friends have watched
    #   - Genre of movie = user's most freq. watched
    # Return list of reccomended movies
    pass

def get_rec_from_favorites(user_data):
    # user_data["favorites"] = list of movies (dictionaries)
    # Get list of reccomended movies if:
    #   - movie in user's "favorites"
    #   - user's friends have NOT watched (get_unique_watched)
    # Return list of reccomended movies
    pass