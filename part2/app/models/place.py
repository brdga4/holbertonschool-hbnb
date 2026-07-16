from app.models.baseModel import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        if not isinstance(owner, User):
            raise TypeError("owner must be an instance of User")
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title is required and cannot be empty.")
        if len(value) > 100:
            raise ValueError("Title must not exceed 100 characters.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if not value:
            self._description = None
            return
        if not isinstance(value, str):
            raise TypeError("Description most be String")
        if len(value.strip()) == 0:
            self._description = None
            return
        self._description = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("price most be a positiv number")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value: float):
        if not isinstance(value, (float, int)) or (value < -90 or value > 90):
            raise ValueError("latitude most be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value: float):
        if not isinstance(value, (float, int)) or (value < -180 or value > 180):
            raise ValueError("longitude most be between -180 and 180")
        self._longitude = value

    def add_review(self, review):
        from app.models.review import Review

        """Add a review to the place."""
        if not isinstance(review, Review):
            raise TypeError("review must be an instance of Review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise TypeError("amenity must be an instance of Amenity")
        self.amenities.append(amenity)
