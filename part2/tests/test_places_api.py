import unittest
import uuid
from app import create_app


class TestPlacesAPI(unittest.TestCase):
    def setUp(self):
        """Initialize test client and pre-create a valid user to act as a Place owner."""
        self.app = create_app()
        self.client = self.app.test_client()

        user_payload = {
            "first_name": "Arthur",
            "last_name": "Pendelton",
            "email": f"arthur_{uuid.uuid4()}@hbnb.io",
        }
        user_res = self.client.post("/api/v1/users/", json=user_payload)
        self.assertEqual(
            user_res.status_code, 201, f"User setup failed: {user_res.data}"
        )
        self.owner_id = user_res.get_json()["id"]

        place_payload = {
            "title": f"Grand Seaside Villa {uuid.uuid4()}",
            "description": "Panoramic ocean views with private beach access",
            "price": 350.0,
            "latitude": 34.0259,
            "longitude": -118.7798,
            "owner_id": self.owner_id,
        }
        place_res = self.client.post("/api/v1/places/", json=place_payload)
        self.assertEqual(
            place_res.status_code, 201, f"Place setup failed: {place_res.data}"
        )
        self.base_place_id = place_res.get_json()["id"]

    def test_create_place_success(self):
        """Test creating a valid place returns HTTP 201 Created."""
        payload = {
            "title": "Mountain Cabin Retreat",
            "description": "Cozy cabin nestled in the pine trees",
            "price": 180.0,
            "latitude": 39.5501,
            "longitude": -105.7821,
            "owner_id": self.owner_id,
        }
        res = self.client.post("/api/v1/places/", json=payload)
        self.assertEqual(res.status_code, 201)

        data = res.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Mountain Cabin Retreat")
        self.assertEqual(data["price"], 180.0)

    def test_create_place_latitude_out_of_bounds(self):
        """Test creating a place with latitude > 90 returns HTTP 400 Bad Request."""
        payload = {
            "title": "North Pole Station",
            "price": 100.0,
            "latitude": 95.5000,
            "longitude": 0.0000,
            "owner_id": self.owner_id,
        }
        res = self.client.post("/api/v1/places/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_place_longitude_out_of_bounds(self):
        """Test creating a place with longitude < -180 returns HTTP 400 Bad Request."""
        payload = {
            "title": "Edge of the World",
            "price": 100.0,
            "latitude": 0.0000,
            "longitude": -190.0000,
            "owner_id": self.owner_id,
        }
        res = self.client.post("/api/v1/places/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_place_negative_price(self):
        """Test creating a place with a negative price returns HTTP 400 Bad Request."""
        payload = {
            "title": "Subsidized Housing",
            "price": -50.0,
            "latitude": 10.0000,
            "longitude": 10.0000,
            "owner_id": self.owner_id,
        }
        res = self.client.post("/api/v1/places/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_place_invalid_owner_id(self):
        """Test creating a place with a non-existent owner UUID returns HTTP 400 Bad Request."""
        payload = {
            "title": "Ghost Property",
            "price": 200.0,
            "latitude": 20.0000,
            "longitude": -80.0000,
            "owner_id": "00000000-0000-0000-0000-000000000000",
        }
        res = self.client.post("/api/v1/places/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_get_all_places(self):
        """Test retrieving all places returns HTTP 200 OK and a list."""
        res = self.client.get("/api/v1/places/")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_get_place_by_id_success(self):
        """Test retrieving a valid place by UUID returns HTTP 200 OK."""
        res = self.client.get(f"/api/v1/places/{self.base_place_id}")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["id"], self.base_place_id)

    def test_get_place_by_id_not_found(self):
        """Test requesting a non-existent place UUID returns HTTP 404 Not Found."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        res = self.client.get(f"/api/v1/places/{fake_id}")
        self.assertEqual(res.status_code, 404)

    def test_update_place_success(self):
        """Test updating a place returns HTTP 200 OK when providing a complete valid payload."""
        payload = {
            "title": "Grand Seaside Estate (Renovated)",
            "description": "Panoramic ocean views with private beach access",
            "price": 450.0,
            "latitude": 34.0259,
            "longitude": -118.7798,
            "owner_id": self.owner_id,
        }
        res = self.client.put(f"/api/v1/places/{self.base_place_id}", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["title"], "Grand Seaside Estate (Renovated)")
        self.assertEqual(data["price"], 450.0)

    def test_update_place_not_found(self):
        """Test updating a non-existent place returns HTTP 404 Not Found."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        payload = {
            "title": "Ghost House",
            "description": "Nowhere",
            "price": 100.0,
            "latitude": 10.0,
            "longitude": 10.0,
            "owner_id": self.owner_id,
        }
        res = self.client.put(f"/api/v1/places/{fake_id}", json=payload)
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
