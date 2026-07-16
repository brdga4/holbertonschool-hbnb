import unittest
from app.services.facade import HBnBFacade


class TestFacade(unittest.TestCase):

    def setUp(self):
        self.facade = HBnBFacade()

        self.user = self.facade.create_user({
            "first_name": "John",
            "last_name": "Wick",
            "email": "john.wick@continental.com"
        })

        self.amenity = self.facade.create_amenity({"name": "Gold Coins"})

    def test_create_user_duplicate_email(self):
        with self.assertRaises(ValueError):
            self.facade.create_user({
                "first_name": "Helen",
                "last_name": "Wick",
                "email": "john.wick@continental.com"
            })

    def test_create_place_invalid_owner(self):
        data = {
            "title": "The Continental",
            "price": 500,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": "invalid-owner-id",
            "amenities": []
        }
        with self.assertRaises(ValueError):
            self.facade.create_place(data)

    def test_create_place_invalid_amenity(self):
        data = {
            "title": "The Continental",
            "price": 500,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.user.id,
            "amenities": ["bad-amenity-id"]
        }
        with self.assertRaises(ValueError):
            self.facade.create_place(data)


if __name__ == "__main__":
    unittest.main()
