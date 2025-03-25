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

    if movie in user_data['watched']: # duplicate exists, all 3 key value matches
        return user_data
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie in user_data['watchlist']:
        return user_data
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie["title"] == title:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
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
    #check if watched list is empty
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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

