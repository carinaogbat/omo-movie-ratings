"""CRUD Operations"""
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, 
        overview=overview, 
        release_date=release_date, 
        poster_path=poster_path)

    return movie

def get_movie_by_id(movie_id):
    """Returns movie by ID"""

    return Movie.query.get(movie_id)

def get_user_by_id(user_id):
    """Returns user by ID"""

    return User.query.get(user_id)


def get_movies():
    """Returns all movies in database"""

    return Movie.query.all()

def get_users():
    """Returns all users"""

    return User.query.all()

def create_rating(user, movie, score):

    rating = Rating(user=user, 
        movie=movie, 
        score=score)

    return rating






if __name__ == '__main__':
    from server import app
    connect_to_db(app)