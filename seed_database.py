"""Script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings-omo")
os.system("createdb ratings-omo")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


# TODO: get the title, overview, and poster_path from the movie
# dictionary. Then, get the release_date and convert it to a
# datetime object with datetime.strptime

movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (movie["title"], 
    movie["overview"], 
    movie["poster_path"]
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    # TODO: create a movie here and append it to movies_in_db
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for x in range(10):
        rand_movie = choice(movies_in_db)
        rand_score = randint(1, 5)

        rating = crud.create_rating(user, rand_movie, rand_score)
        model.db.session.add(rating)

model.db.session.commit()

