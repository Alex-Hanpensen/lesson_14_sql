import sqlite3
import json


def connect_db():
    with sqlite3.connect('netflix.db') as connection:
        return connection.cursor()


def check_rating(check: str) -> str | tuple:
    match check:
        case 'children':
            return 'G'
        case 'family':
            return 'G', 'PG', 'PG-13'
        case 'adult':
            return 'R', 'NC-17'


def search_by_title(title: str) -> json:
    sqlite_query = """SELECT title, country, release_year, listed_in, description
                      FROM netflix
                      WHERE title = ?
                      ORDER BY release_year DESC
                      """

    return json.dumps(dict(zip(
        ('title', 'country', 'release_year', 'listed_in', 'description'),
        connect_db().execute(sqlite_query, (title,)).fetchone()
    ))
    )


def search_by_range(year_1: int, year_2) -> json:
    sqlite_query = """SELECT title, release_year
                      FROM netflix
                      WHERE release_year BETWEEN ? AND ?
                      ORDER BY release_year
                      LIMIT 100
                      """
    return json.dumps([{key: value for key, value in connect_db().execute(sqlite_query, (year_1, year_2)).fetchall()}])


def search_by_rating(check: str) -> json:
    res = ', '.join(len(check_rating(check)) * '?')
    sqlite_query = f"""SELECT title, rating, description
                      FROM netflix
                      WHERE rating IN ({res})
                      """
    return json.dumps([dict(zip(('title', 'rating', 'description'), i)) for i in
                       connect_db().execute(sqlite_query, check_rating(check)).fetchall()])


def search_by_genre(genre: str) -> json:
    sqlite_query = """SELECT title, listed_in, description, release_year
                      FROM netflix
                      WHERE listed_in = ?
                      ORDER BY release_year DESC
                      LIMIT 10
                      """
    return json.dumps([dict(zip(('title', 'listed_in', 'description', 'release_year'), i)) for i in
                       connect_db().execute(sqlite_query, (genre,)).fetchall()])


def get_actors(actor_1, actor_2):
    sqlite_query = f"""SELECT "cast" as new_cast 
                       FROM netflix
                       WHERE new_cast LIKE "%{actor_1}%" OR "%{actor_2}%"
                       GROUP BY new_cast
                       """
    gen_obj = (actor.split(', ') for actors in connect_db().execute(sqlite_query).fetchall() for actor in actors)
    result = []
    for actors in gen_obj:
        result.extend(actors)

    return list(set(filter(lambda x: result.count(x) > 1, result)))


def get_a_selection(tv_type: str, year: int, genre: str):
    sqlite_query = f"""SELECT type, release_year, listed_in
                       FROM netflix
                       WHERE type = ?
                       AND release_year = ?
                       AND listed_in LIKE "%{genre}%"
                       GROUP BY type, release_year, listed_in
                       """
    return json.dumps([row for row in connect_db().execute(sqlite_query, (tv_type, year)).fetchall()])
