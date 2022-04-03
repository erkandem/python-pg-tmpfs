from uuid import uuid4

from django.db import IntegrityError

from welcome.utils import add, db_add
from random import randint
from logging import getLogger
from django.contrib.auth import get_user_model

logger = getLogger(__name__)


def test_add():
    x, y = 2, 3
    result = add(x, y)
    assert result == x + y


def test_dbadd(db):
    x, y = 2, 3
    result = db_add(x, y)
    assert result == x + y


def test_create_users(db):
    User = get_user_model()
    for i in range(1000):
        User.objects.create(username=str(uuid4()))
    assert User.objects.count() == 1000

def test_create_users_2(db):
    User = get_user_model()
    for i in range(1000):
        User.objects.create(username=str(uuid4()))
    assert User.objects.count() == 1000


def test_create_users_3(db):
    User = get_user_model()
    for i in range(1000):
        User.objects.create(username=str(uuid4()))
    assert User.objects.count() == 1000


def test_create_users_4(db):
    User = get_user_model()
    for i in range(1000):
        User.objects.create(username=str(uuid4()))
    assert User.objects.count() == 1000
