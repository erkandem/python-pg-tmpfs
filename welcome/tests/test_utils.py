from welcome.utils import add, db_add


def test_add():
    x, y = 2, 3
    result = add(x, y)
    assert result == x + y


def test_dbadd(db):
    x, y = 2, 3
    result = db_add(x, y)
    assert result == x + y
