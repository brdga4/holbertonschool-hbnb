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
    Uses properties to ensure validation rules are permanently enforced.
    """

    def __init__(self, text: str, rating, place: Place, user: User, **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Review text must be a non-empty string.")
        self._text = value.strip()

    @property
    def rating(self) -> RatingValue:
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, RatingValue):
            self._rating = value
        else:
            try:
                self._rating = RatingValue(int(value))
            except (ValueError, TypeError):
                raise ValueError("Rating must be an integer between 1 and 5")

    @property
    def place(self) -> Place:
        return self._place

    @place.setter
    def place(self, value: Place):
        if not isinstance(value, Place):
            raise ValueError("Place must be an instance of the Place class.")
        self._place = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User):
        if not isinstance(value, User):
            raise ValueError("User must be an instance of the User class.")
        self._user = value
