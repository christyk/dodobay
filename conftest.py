import pytest
import uuid
from api.user.models import User
from api.item.models import Category, Item
from api.listing.models import Listing
from rest_framework.test import APIClient


data_user = {
    "username": "test_user",
    "email": "test@gmail.com",
    "villager_name": "test_villager",
    "island_name": "test_island",
    "hemisphere": "N",
    "friend_code": "0000-0000-0000",
    "password": "test_password"
}


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)

@pytest.fixture
def category(db):
    return Category.objects.create(name = "TestCategoryName")

@pytest.fixture
def item(db, category) -> Item:
    return Item.objects.create(unique_entry_id = uuid.uuid4, name = "Test Item Name", image = "Test Image URL", category = category, color_1 = "Test Color1", color_2 = "Test Color2")

@pytest.fixture
def listing(db, user, item):
    return Listing.objects.create(user=user, item=item)

@pytest.fixture
def client():
    return APIClient()