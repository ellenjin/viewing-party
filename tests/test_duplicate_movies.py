import pytest
from viewing_party.party import *
from tests.test_constants import *

def test_duplicate_identical_add_to_watched():
    user_data_test = {"watched": [{
                            "title": "Title A",
                            "genre": "Horror",
                            "rating": 3.5
                            }, 
                            {
                            "title": "Title B",
                            "genre": "Comedy",
                            "rating": 4
                            }]}
    movie_add = {
                "title": "Title B",
                "genre": "Comedy",
                "rating": 4
                }
    
    result = add_to_watched(dict(user_data_test), movie_add)
    print(result)
    print(user_data_test)
    assert result == user_data_test

