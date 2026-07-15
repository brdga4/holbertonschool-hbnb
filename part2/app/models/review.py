from app.models.baseModel import BaseModel
from app.models.place import Place
from app.models.user import User
from enum import Enum


class RatingValue(Enum):
    """
    Enum class for rating values so that no value can be less than 1 or greater than 5.
    """

    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5


class Review(BaseModel):
    """
    Review class that represents a review for a place.
    """

    def __init__(self, text, rating, place, user):
        super().__init__()

        if not isinstance(text, str) or not text.strip():
            raise ValueError("Review text must be a non-empty string.")
        self.text = text.strip()

        if isinstance(rating, RatingValue):
            self.rating = rating
        else:
            try:
                self.rating = RatingValue(int(rating))
            except (ValueError, TypeError):
                raise ValueError("Rating must be an integer between 1 and 5")

        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of the Place class.")
        self.place = place

        if not isinstance(user, User):
            raise ValueError("User must be an instance of the User class.")
