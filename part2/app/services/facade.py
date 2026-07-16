from app.persistence.repository import InMemoryRepository
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.user import User
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User methods
    def create_user(self, user_data):
        email = user_data.get("email")
        if email:
            existing_user = self.get_user_by_email(email)
            if existing_user:
                raise ValueError("Email already registered")

        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        for user in self.user_repo.get_all():
            if user.email == email:
                return user
        return None

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None
        self.user_repo.update(user_id, user_data)
        return user

    # Review methods
    def create_review(self, review_data):
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        user_id = review_data.get("user_id")
        place_id = review_data.get("place_id")

        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")

        review = Review(
            text=review_data.get("text"),
            rating=review_data.get("rating"),
            place=place,
            user=user,
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        all_reviews = self.get_all_reviews()

        matching_reviews = []

        for review in all_reviews:
            if review.place.id == place_id:
                matching_reviews.append(review)

        return matching_reviews

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        review = self.get_review(review_id)

        if not review:
            return None

        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        review = self.get_review(review_id)

        if not review:
            return False

        self.review_repo.delete(review_id)
        return True

    # Place methods
    def create_place(self, place_data: dict):
        owner_id = place_data.pop("owner_id", None)
        if owner_id:
            owner = self.user_repo.get(owner_id)
            if owner:
                new_place = Place(**place_data, owner=owner)
                self.place_repo.add(new_place)
                return new_place
        raise ValueError("Owner is not found or owner_id is missing")

    def get_place(self, place_id: str):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None
        self.place_repo.update(place_id, place_data)
        return place

    # Amenity Methods
    def create_amenity(self, amenity_data):
        """Create a new amenity and store it."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by its unique identifier."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all registered amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an existing amenity's attributes."""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None

        if "name" in amenity_data:
            amenity.name = amenity_data["name"]

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
