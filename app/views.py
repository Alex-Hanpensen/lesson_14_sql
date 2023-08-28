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
