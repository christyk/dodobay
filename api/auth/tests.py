import pytest
from rest_framework import status

class TestAuthenticationViewSet:
    endpoint = "/api/auth/"

    @pytest.mark.django_db
    def test_login(self, client, user):
        data = {"email": user.email, "password": "test_password"}
        response = client.post(self.endpoint + "login", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
        assert response.data["user"]["id"] == user.public_id.hex
        assert response.data["user"]["username"] == user.username
        assert response.data["user"]["email"] == user.email

    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "test_user",
            "email": "test@gmail.com",
            "villager_name": "test_villager",
            "island_name": "test_island",
            "hemisphere": "N",
            "friend_code": "0000-0000-0000",
            "password": "test_password"
        }

        response = client.post(self.endpoint + "register", data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_refresh(self, client, user):
        data = {"email": user.email, "password": "test_password"}
        response = client.post(self.endpoint + "login", data)

        assert response.status_code == status.HTTP_200_OK

        data_refresh = {"refresh": response.data["refresh"]}

        response = client.post(self.endpoint + "refresh", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]

    def test_logout(self, client, user):
        data = {"email": user.email, "password": "test_password"}

        response = client.post(self.endpoint + "login", data)

        assert response.status_code == status.HTTP_200_OK

        client.force_authenticate(user=user)

        data_refresh = {"refresh": response.data["refresh"]}

        response = client.post(self.endpoint + "logout", data_refresh)
        assert response.status_code == status.HTTP_204_NO_CONTENT