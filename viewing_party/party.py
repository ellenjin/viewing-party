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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

