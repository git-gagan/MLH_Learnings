#Python Script for Movie Recommendation
import requests
import random

def get_movie():
    while True:  
        id = random.randint(1000000,3999999)
        data = requests.get(f"http://www.omdbapi.com/?i=tt{id}&apikey=#myprivatekey").json()
        if data['Response'] == "True":
            if data["Year"] == "N\A" or "Episode" in data["Title"]:
                continue
            break
    return data

if __name__ == "__main__":
    print(f"\nHey Visitor, Nice to meet ya! Welcome to Movie Recommender script!\n")
    movie = get_movie()
    print("|---------------------------Fetching your movie-----------------------------|\n")
    print(f"I will recommend you to watch:- \"{movie['Title']}\" released in year:- {movie['Year']}\n")
