import pytest
from api.listing.models import Listing, Offer, Comment
from rest_framework import status

# Test Models

@pytest.mark.django_db
def test_create_listing(user, item):
    listing = Listing.objects.create(user=user, item=item, ask_bells=True, ask_tickets=True, ask_wishlist=True, status="C")
    assert listing.user == user
    assert listing.item == item
    assert listing.ask_bells == True
    assert listing.ask_tickets == True
    assert listing.ask_wishlist == True
    assert listing.status == "C"

@pytest.mark.django_db
def test_create_listing_defaults(user, item):
    listing = Listing.objects.create(user=user, item=item)
    assert listing.user == user
    assert listing.item == item
    assert listing.ask_bells == False
    assert listing.ask_tickets == False
    assert listing.ask_wishlist == False
    assert listing.status == "O"

@pytest.mark.django_db
def test_create_offer(user, listing, item):
    offer = Offer.objects.create(user=user, listing=listing, offer_bells=100, offer_tickets=200, offer_wishlist=item, status="C")
    assert offer.user == user
    assert offer.listing == listing
    assert offer.offer_bells == 100
    assert offer.offer_tickets == 200
    assert offer.offer_wishlist == item
    assert offer.status == "C"

@pytest.mark.django_db
def test_create_offer_defaults(user, listing):
    offer = Offer.objects.create(user=user, listing=listing)
    assert offer.user == user
    assert offer.listing == listing
    assert offer.offer_bells == 0
    assert offer.offer_tickets == 0
    assert offer.offer_wishlist is None
    assert offer.status == "B"

@pytest.mark.django_db
def test_create_comment(user, listing):
    comment = Comment.objects.create(user=user, listing=listing, body="Test comment body")
    assert comment.user == user
    assert comment.listing == listing
    assert comment.body == "Test comment body"
    assert comment.edited == False


# Test ViewSets

class TestListingViewSet:

    endpoint = "/api/listing"

    ###########################################################################
    ########### Authenticated User Tests ######################################
    ###### These tests are only run if the user is authenticated ##############

    @pytest.mark.django_db
    def test_list(self, client, user, listing):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve(self, client, user, listing):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + "/" + str(listing.public_id))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == listing.public_id.hex
        assert response.data["item"] == str(listing.item.pk)
        assert response.data["user"]["id"] == listing.user.public_id.hex

    @pytest.mark.django_db
    def test_create(self, client, user, item):
        client.force_authenticate(user=user)
        data = {"item": item.pk, "user": user.public_id.hex}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["item"] == str(data["item"])
        assert response.data["user"]["id"] == data["user"]

    @pytest.mark.django_db
    def test_update(self, client, user, listing):
        client.force_authenticate(user=user)
        data = {"item": listing.item.pk, "user": user.public_id.hex, "ask_bells": True}
        response = client.put(self.endpoint + "/" + str(listing.public_id.hex), data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["ask_bells"] == data["ask_bells"]

    @pytest.mark.django_db
    def test_delete(self, client, user, listing):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + "/" + str(listing.public_id))
        assert response.status_code == status.HTTP_204_NO_CONTENT

    ###########################################################################
    ########## Testing anonymous user #########################################
    ####### These tests are only run if the user is not authenticated #########

    @pytest.mark.django_db
    def test_list_anonymous(self, client, listing):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve_anonymous(self, client, listing):
        response = client.get(self.endpoint + "/" + str(listing.public_id))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == listing.public_id.hex
        assert response.data["item"] == str(listing.item.pk)
        assert response.data["user"]["id"] == listing.user.public_id.hex

    @pytest.mark.django_db
    def test_create_anonymous(self, client, item):
        data = {"item": item, "user": "test_user"}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_update_anonymous(self, client, listing, item):
        data = {"item": item, "user": "test_user", "ask_bells": 1000}
        response = client.put(self.endpoint + "/" + str(listing.public_id), data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_delete_anonymous(self, client, listing):
        response = client.delete(self.endpoint + "/" + str(listing.public_id))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED