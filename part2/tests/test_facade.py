import unittest
from app.services.facade import HBnBFacade


class TestHBnBFacade(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh Facade and create base entities before each test."""
        self.facade = HBnBFacade()

        self.user = self.facade.create_user(
            {
                "first_name": "John",
                "last_name": "Wick",
                "email": "john.wick@continental.com",
            }
        )

        self.place = self.facade.create_place(
            {
                "title": "The Continental Hotel",
                "description": "Exclusive sanctuary",
                "price": 500.0,
                "latitude": 40.7128,
                "longitude": -74.0060,
                "owner_id": self.user.id,
            }
        )

    def test_create_user_success(self):
        """Test creating a user successfully stores them in the repository."""
        new_user = self.facade.create_user(
            {
                "first_name": "Winston",
                "last_name": "Scott",
                "email": "winston@continental.com",
            }
        )
        self.assertIsNotNone(new_user.id)
        self.assertEqual(new_user.first_name, "Winston")

        fetched_user = self.facade.get_user(new_user.id)
        self.assertEqual(fetched_user.email, "winston@continental.com")
        self.assertEqual(
            self.facade.get_user_by_email("winston@continental.com").id, new_user.id
        )

    def test_create_user_duplicate_email_fails(self):
        """Test that registering an email that already exists raises ValueError."""
        with self.assertRaises(ValueError):
            self.facade.create_user(
                {
                    "first_name": "Imposter",
                    "last_name": "Wick",
                    "email": "john.wick@continental.com",
                }
            )

    def test_update_user_attributes(self):
        """Test updating existing user attributes works correctly."""
        updated = self.facade.update_user(self.user.id, {"first_name": "Jonathan"})
        self.assertEqual(updated.first_name, "Jonathan")
        self.assertEqual(self.facade.get_user(self.user.id).first_name, "Jonathan")

    def test_create_place_success(self):
        """Test creating a place properly links the owner object."""
        self.assertEqual(self.place.title, "The Continental Hotel")
        self.assertEqual(self.place.owner.id, self.user.id)
        self.assertEqual(self.place.owner.email, "john.wick@continental.com")

    def test_create_place_missing_owner_fails(self):
        """Test that creating a place without an owner_id raises ValueError."""
        with self.assertRaises(ValueError):
            self.facade.create_place(
                {
                    "title": "Ownerless House",
                    "price": 100.0,
                    "latitude": 10.0,
                    "longitude": 10.0,
                }
            )

    def test_create_place_invalid_owner_id_fails(self):
        """Test that creating a place with a fake owner UUID raises ValueError."""
        with self.assertRaises(ValueError):
            self.facade.create_place(
                {
                    "title": "Ghost House",
                    "price": 100.0,
                    "latitude": 10.0,
                    "longitude": 10.0,
                    "owner_id": "00000000-0000-0000-0000-000000000000",
                }
            )

    def test_create_review_success(self):
        """Test creating a review successfully links User and Place."""
        review = self.facade.create_review(
            {
                "text": "Impeccable service and strict rules.",
                "rating": 5,
                "user_id": self.user.id,
                "place_id": self.place.id,
            }
        )
        self.assertIsNotNone(review.id)
        self.assertEqual(review.user.id, self.user.id)
        self.assertEqual(review.place.id, self.place.id)

        place_reviews = self.facade.get_reviews_by_place(self.place.id)
        self.assertEqual(len(place_reviews), 1)
        self.assertEqual(place_reviews[0].text, "Impeccable service and strict rules.")

    def test_create_review_invalid_user_fails(self):
        """Test creating a review with a fake user_id raises ValueError."""
        with self.assertRaises(ValueError):
            self.facade.create_review(
                {
                    "text": "Ghost review",
                    "rating": 1,
                    "user_id": "fake-user-uuid",
                    "place_id": self.place.id,
                }
            )

    def test_create_review_invalid_place_fails(self):
        """Test creating a review for a fake place_id raises ValueError."""
        with self.assertRaises(ValueError):
            self.facade.create_review(
                {
                    "text": "Reviewing nowhere",
                    "rating": 1,
                    "user_id": self.user.id,
                    "place_id": "fake-place-uuid",
                }
            )

    def test_delete_review_success(self):
        """Test deleting a review removes it from the repository."""
        review = self.facade.create_review(
            {
                "text": "Temporary review",
                "rating": 3,
                "user_id": self.user.id,
                "place_id": self.place.id,
            }
        )
        self.assertTrue(self.facade.delete_review(review.id))
        self.assertIsNone(self.facade.get_review(review.id))

    def test_amenity_crud_lifecycle(self):
        """Test creating, fetching, and updating an amenity."""
        amenity = self.facade.create_amenity({"name": "High-Speed Wi-Fi"})
        self.assertIsNotNone(amenity.id)
        self.assertEqual(self.facade.get_amenity(amenity.id).name, "High-Speed Wi-Fi")

        updated = self.facade.update_amenity(
            amenity.id, {"name": "Gigabit Fiber Wi-Fi"}
        )
        self.assertEqual(updated.name, "Gigabit Fiber Wi-Fi")
        self.assertIn(updated, self.facade.get_all_amenities())


if __name__ == "__main__":
    unittest.main()
