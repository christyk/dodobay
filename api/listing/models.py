from django.db import models
from api.abstract.models import AbstractModel, AbstractManager


class ListingManager(AbstractManager):
    pass

class Listing(AbstractModel):
    STATUS_CHOICES = [
        ('O', 'Open'),
        ('F', 'Fulfilled'),
        ('C', 'Canceled'),
    ]
    user = models.ForeignKey(to="api_user.User", on_delete=models.CASCADE)
    item = models.ForeignKey(to="api_item.Item", on_delete=models.CASCADE)
    ask_bells = models.BooleanField(db_column='ASK_BELLS', default=False)
    ask_tickets = models.BooleanField(db_column='ASK_TICKETS', default=False)
    ask_wishlist = models.BooleanField(db_column='ASK_WISHLIST', default=False)
    status = models.CharField(max_length=1, db_column='STATUS', choices=STATUS_CHOICES, default = 'O')
    edited = models.BooleanField(default=False)

    objects = ListingManager()

    class Meta:
        db_table = 'LISTINGS'

    def get_status_display(self, STATUS_CHOICES):
        return STATUS_CHOICES[self.status]
    
    def __str__(self):
        return 'user:' + self.user + ', item:' + self.item + ', status:' + self.get_status_display()
    

class OfferManager(AbstractManager):
    pass

class Offer(AbstractModel):
    STATUS_CHOICES = [
        ('O', 'Offer Open'),
        ('A', 'Offer Accepted'),
        ('R', 'Offer Rejected'),
        ('F', 'Fulfilled'),
        ('C', 'Canceled'),
    ]
    user = models.ForeignKey(to="api_user.User", on_delete=models.CASCADE)
    listing = models.ForeignKey(to="api_listing.Listing", on_delete=models.CASCADE)
    offer_bells = models.IntegerField(default=0)
    offer_tickets = models.IntegerField(default=0)
    offer_wishlist = models.ForeignKey(to="api_item.Item", on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default = 'O')
    edited = models.BooleanField(default=False)

    objects = OfferManager()

    class Meta:
        db_table = 'OFFERS'

    def get_status_display(self, STATUS_CHOICES):
        return STATUS_CHOICES[self.status]
    
    def __str__(self):
        return 'user:' + self.user.username + ', listing:' + self.listing + ', bells:' + self.offer_bells + ', tickets:' + self.offer_tickets + ', wishlist:' + self.offer_wishlist + ', status:' + self.get_status_display()
    

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    user = models.ForeignKey(to="api_user.User", on_delete=models.CASCADE)
    listing = models.ForeignKey(to="api_listing.Listing", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    class Meta:
        db_table = 'COMMENTS'

    def __str__(self):
        return 'user:' + self.user.username + ', listing:' + self.listing + ', comment:' + self.body