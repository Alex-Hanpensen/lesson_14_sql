from flask import render_template
from . import movie_controller
from app import app
import json


@app.route('/movie/<title>')
def get_movie(title):
    data = json.loads(movie_controller.search_by_title(title))
    return render_template('movie.html', movie=data.values())


@app.route('/movie/<year_1>/to/<year_2>')
def get_range(year_1, year_2):
    data = json.loads(movie_controller.search_by_range(year_1, year_2))
    return render_template('movie.html', movie=data.items())


@app.route('/rating/<children>')
def get_rating_child(children):
    data = json.loads(movie_controller.search_by_rating(children))
    return render_template('movie.html', movie=data)


@app.route('/rating/<family>')
def get_rating_family(family):
    data = json.loads(movie_controller.search_by_rating(family))
    return render_template('movie.html', movie=data)


@app.route('/rating/<adult>')
def get_rating_adult(adult):
    data = json.loads(movie_controller.search_by_rating(adult))
    return render_template('movie.html', movie=data)


@app.route('/genre/<genre>')
def get_genre(genre):
    data = json.loads(movie_controller.search_by_genre(genre))
    return render_template('movie.html', movie=data)
