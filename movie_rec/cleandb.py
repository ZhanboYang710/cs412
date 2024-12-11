from django.db import connection

def drop_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

# Drop specific tables

drop_table('movie_rec_userprofile')