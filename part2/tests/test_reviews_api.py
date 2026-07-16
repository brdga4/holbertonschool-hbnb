import unittest
import uuid
from app import create_app


class TestReviewAPI(unittest.TestCase):
    def setUp(self):
        """Initialize test client and pre-create a unique User and Place for reviews."""
        self.app = create_app()
        self.client = self.app.test_client()

        unique_email = f"john_{uuid.uuid4()}@continental.com"
        user_payload = {
            "first_name": "John",
            "last_name": "Wick",
            "email": unique_email,
        }
        user_res = self.client.post("/api/v1/users/", json=user_payload)
        self.assertEqual(
            user_res.status_code, 201, f"User setup failed: {user_res.data}"
        )
        self.user_id = user_res.get_json()["id"]

        place_payload = {
            "title": f"The Continental {uuid.uuid4()}",
            "description": "Exclusive sanctuary for assassins",
            "price": 500.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.user_id,
        }
        place_res = self.client.post("/api/v1/places/", json=place_payload)
        self.assertEqual(
            place_res.status_code, 201, f"Place setup failed: {place_res.data}"
        )
        self.place_id = place_res.get_json()["id"]

    def test_create_review_success(self):
        """Test creating a valid review returns HTTP 201 Created."""
        payload = {
            "text": "Behold, excellent service and strict rules.",
            "rating": 5,
            "user_id": self.user_id,
            "place_id": self.place_id,
        }
        res = self.client.post("/api/v1/reviews/", json=payload)
        self.assertEqual(res.status_code, 201)

        data = res.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["text"], "Behold, excellent service and strict rules.")

    def test_create_review_invalid_rating(self):
        """Test that a rating out of bounds (> 5 or < 1) returns HTTP 400 Bad Request."""
        payload = {
            "text": "The rating is out of bounds",
            "rating": 6,
            "user_id": self.user_id,
            "place_id": self.place_id,
        }
        res = self.client.post("/api/v1/reviews/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_review_empty_text(self):
        """Test that an empty review text returns HTTP 400 Bad Request."""
        payload = {
            "text": "",
            "rating": 4,
            "user_id": self.user_id,
            "place_id": self.place_id,
        }
        res = self.client.post("/api/v1/reviews/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_review_invalid_user_or_place(self):
        """Test that referencing a non-existent user_id or place_id returns HTTP 400/404."""
        payload = {
            "text": "Ghost review",
            "rating": 3,
            "user_id": "00000000-0000-0000-0000-000000000000",
            "place_id": self.place_id,
        }
        res = self.client.post("/api/v1/reviews/", json=payload)
        self.assertIn(res.status_code, [400, 404])

    def test_get_all_reviews(self):
        """Test retrieving all reviews returns HTTP 200 OK."""
        res = self.client.get("/api/v1/reviews/")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    def test_delete_review_success(self):
        """Test creating and then deleting a review returns HTTP 200 OK."""
        payload = {
            "text": "Temporary review to be deleted.",
            "rating": 2,
            "user_id": self.user_id,
            "place_id": self.place_id,
        }
        create_res = self.client.post("/api/v1/reviews/", json=payload)
        review_id = create_res.get_json()["id"]

        del_res = self.client.delete(f"/api/v1/reviews/{review_id}")
        self.assertEqual(del_res.status_code, 200)

        get_res = self.client.get(f"/api/v1/reviews/{review_id}")
        self.assertEqual(get_res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
