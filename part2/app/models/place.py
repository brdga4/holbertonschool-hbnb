from app.models.baseModel import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    def __init__(self, **kwargs):
        self.title = kwargs.pop("title", None)
        self.description = kwargs.pop("description", None)
        self.price = kwargs.pop("price", None)
        self.latitude = kwargs.pop("latitude", None)
        self.longitude = kwargs.pop("longitude", None)
        self.owner = kwargs.pop("owner", None)

        kwargs.pop("amenities", None)
        kwargs.pop("reviews", None)

        super().__init__(**kwargs)

        if self.owner and not isinstance(self.owner, User):
            raise TypeError("owner must be an instance of User")

        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title is required and cannot be empty.")
        if len(value) > 100:
            raise ValueError("Title must not exceed 100 characters.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            self._description = None
            return
        if not isinstance(value, str):
            raise TypeError("Description must be a String")
        if len(value.strip()) == 0:
            self._description = None
            return
        self._description = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("price must be a positive number")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (float, int)) or (value < -90 or value > 90):
            raise ValueError("latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (float, int)) or (value < -180 or value > 180):
            raise ValueError("longitude must be between -180 and 180")
        self._longitude = value

    def add_review(self, review):
        """Add a review to the place."""
        from app.models.review import Review

        if not isinstance(review, Review):
            raise TypeError("review must be an instance of Review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise TypeError("amenity must be an instance of Amenity")
        self.amenities.append(amenity)
