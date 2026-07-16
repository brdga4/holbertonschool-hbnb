from app.persistence.repository import InMemoryRepository
from app.models.place import Place


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
        if place_id:
            place = self.place_repo.get(place_id)
            if place:
                return place
        raise ValueError("there is no plase with this id")

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        self.place_repo.update(place_id, place_data)
        return place
