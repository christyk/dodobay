import pytest
from api.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@gmail.com",
    "villager_name": "test_villager",
    "island_name": "test_island",
    "hemisphere": "N",
    "friend_code": "0000-0000-0000",
    "password": "test_password"
}

@pytest.mark.django_db
def test_creat_user():
    user = User.objects.create_user(**data_user)
    assert user.username == data_user["username"]
    assert user.email == data_user["email"]
    assert user.villager_name == data_user["villager_name"]
    assert user.island_name == data_user["island_name"]
    assert user.hemisphere == data_user["hemisphere"]
    assert user.friend_code == data_user["friend_code"]


data_superuser = {
    "username": "test_superuser",
    "email": "testsuperuser@gmail.com",
    "villager_name": "testsuperuser_villager",
    "island_name": "testsuperuser_island",
    "hemisphere": "N",
    "friend_code": "1111-1111-1111",
    "password": "testsuperuser_password"
}

@pytest.mark.django_db
def test_creat_superuser():
    user = User.objects.create_superuser(**data_superuser)
    assert user.username == data_superuser["username"]
    assert user.email == data_superuser["email"]
    assert user.villager_name == data_superuser["villager_name"]
    assert user.island_name == data_superuser["island_name"]
    assert user.hemisphere == data_superuser["hemisphere"]
    assert user.friend_code == data_superuser["friend_code"]
    assert user.is_superuser == True
    assert user.is_staff == True