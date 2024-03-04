# dodobay API Endpoints

# User Registration and Authentication
/api/auth/register
    post: all

/api/auth/login
    post: all

/api/auth/refresh
    post: all

/api/auth/logout
    post: authenticated user

# User Data
/api/user
    get: self, superuser: all fields
    get: others including anonymous user: limited fields

/api/user/{userId}
    get: self, admin: all fields
    get: others including anonymous user: limited fields
    patch: self, superuser

/api/user/{userId}/listing
    get: all

/api/user/{userId}/comment
    get: self, superuser

/api/user/{userId}/offer
    get: self, superuser

# Item Data
/api/category
    get: all

/api/category/{categoryId}
    get: all

/api/item
    get: all

/api/item/{itemId}
    get: all

/api/item/{itemId}/wish
    post: authenticated user

/api/item/{itemId}/remove_wish
    post: authenticated user

/api/item-detail/{itemId}
    get: all

# Listing
/api/listing
    get: all
    post: authenticated user

/api/listing/{listingId}
    get: all
    patch: listing owner
    delete: listing owner, superuser

/api/listing/{listingId}/watch
    post: authenticated user

/api/listing/{listingId}/remove_watch
    post: authenticated user

/api/listing/{listingId}/fulfill
    post: listing owner

/api/listing/{listingId}/cancel
    post: listing owner

# Listing Comment
/api/listing/{listingId}/comment
    get: all
    post: authenticated user

/api/listing/{listingId}/comment/{commentId}
    get: all
    patch: comment owner
    delete: comment owner, superuser

# Listing Offer
/api/listing/{listingId}/offer
    get: own, listing user
    post: authenticated user

/api/listing/{listingId}/offer/{offerId}
    get: offer owner, listing owner, superuser
    patch: offer owner
    delete: offer owner, superuser

/api/listing/{listingId}/offer/{offerId}/accept
    post: listing owner

/api/listing/{listingId}/offer/{offerId}/reject
    post: listing owner

/api/listing/{listingId}/offer/{offerId}/fulfill
    post: offer owner, listing owner

/api/listing/{listingId}/offer/{offerId}/cancel
    post: offer owner