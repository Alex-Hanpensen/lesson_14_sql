# import sqlite3
# import prettytable
#
# with sqlite3.connect('netflix.db') as connect:
#     cursor = connect.cursor()
#
#
#     def search_by_title(find: str):
#         sqlite_query = f"""
#                        SELECT title, country, release_year, listed_in, description
#                        FROM netflix
#                        WHERE title = '{find}'
#                        ORDER BY release_year DESC
#                        """
#         return sqlite_query
#
#
#     result = cursor.execute(search_by_title("1920"))
#
#     # mytable = prettytable.from_db_cursor(result)
#     # mytable.max_width = 30
#
# if __name__ == '__main__':
#     ...





