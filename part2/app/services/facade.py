from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    # ==========================================
    # Your Amenity Methods (Added safely below)
    # ==========================================

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

        if 'name' in amenity_data:
            amenity.name = amenity_data['name']

        self.amenity_repo.update(amenity_id, amenity)
        return amenity
