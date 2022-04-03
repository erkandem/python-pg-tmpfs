from django.db import connection


def add(x, y):
    return x + y


def db_add(x, y):
    with connection.cursor() as cursor:
        pass
        cursor.execute(
            "SELECT %s + %s;",
            (x, y,)
        )
        row = cursor.fetchone()[0]
    return row
