import sqlite3
import json


def connect_bd():
    with sqlite3.connect('netflix.db') as connection:
        return connection.cursor()


def search_by_title(title: str) -> json:
    sqlite_query = """SELECT title, country, release_year, listed_in, description
                      FROM netflix
                      WHERE title = ?
                      ORDER BY release_year DESC
                      """
    return json.dumps(dict(zip(
        ('title', 'country', 'release_year', 'listed_in', 'description'),
        connect_bd().execute(sqlite_query, (title,)).fetchone()
    ))
    )



def search_by_range(year_1: int, year_2) -> json:
    sqlite_query = """SELECT title, release_year
                      FROM netflix
                      WHERE release_year BETWEEN ? AND ?
                      ORDER BY release_year
                      LIMIT 100
                      """
    return json.dumps({key: value for key, value in connect_bd().execute(sqlite_query, (year_1, year_2)).fetchall()})
