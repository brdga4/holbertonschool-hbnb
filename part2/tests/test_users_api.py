import unittest
import uuid
from app import create_app


class TestUsersAPI(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh Flask test client before each test."""
        self.app = create_app()
        self.client = self.app.test_client()

        self.base_email = f"alice_{uuid.uuid4()}@example.com"
        payload = {
            "first_name": "Alice",
            "last_name": "Smith",
            "email": self.base_email,
        }
        res = self.client.post("/api/v1/users/", json=payload)
        self.assertEqual(res.status_code, 201, f"User setup failed: {res.data}")
        self.base_user_id = res.get_json()["id"]

    def test_create_user_success(self):
        """Test creating a valid user returns HTTP 201 Created."""
        payload = {
            "first_name": "Bob",
            "last_name": "Jones",
            "email": f"bob_{uuid.uuid4()}@example.com",
        }
        res = self.client.post("/api/v1/users/", json=payload)
        self.assertEqual(res.status_code, 201)

        data = res.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["first_name"], "Bob")

    def test_create_user_duplicate_email(self):
        """Test creating a user with an already registered email returns HTTP 400 Bad Request."""
        payload = {
            "first_name": "Imposter",
            "last_name": "Smith",
            "email": self.base_email,
        }
        res = self.client.post("/api/v1/users/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_user_invalid_email_format(self):
        """Test creating a user with a malformed email string returns HTTP 400 Bad Request."""
        payload = {
            "first_name": "Charlie",
            "last_name": "Brown",
            "email": "not-a-valid-email",
        }
        res = self.client.post("/api/v1/users/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_create_user_missing_required_fields(self):
        """Test creating a user with empty first_name returns HTTP 400 Bad Request."""
        payload = {
            "first_name": "",
            "last_name": "Brown",
            "email": f"charlie_{uuid.uuid4()}@example.com",
        }
        res = self.client.post("/api/v1/users/", json=payload)
        self.assertEqual(res.status_code, 400)

    def test_get_all_users(self):
        """Test retrieving all users returns HTTP 200 OK and a list."""
        res = self.client.get("/api/v1/users/")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_get_user_by_id_success(self):
        """Test retrieving a valid user by UUID returns HTTP 200 OK."""
        res = self.client.get(f"/api/v1/users/{self.base_user_id}")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["id"], self.base_user_id)
        self.assertEqual(data["email"], self.base_email)

    def test_get_user_by_id_not_found(self):
        """Test requesting a non-existent UUID returns HTTP 404 Not Found."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        res = self.client.get(f"/api/v1/users/{fake_id}")
        self.assertEqual(res.status_code, 404)

    def test_update_user_success(self):
        """Test updating a user returns HTTP 200 OK when providing a complete valid payload."""
        payload = {
            "first_name": "Alicia",
            "last_name": "Smith",
            "email": self.base_email,
        }
        res = self.client.put(f"/api/v1/users/{self.base_user_id}", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["first_name"], "Alicia")

    def test_update_user_not_found(self):
        """Test updating a non-existent user returns HTTP 404 Not Found."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        payload = {
            "first_name": "Ghost",
            "last_name": "Person",
            "email": f"ghost_{uuid.uuid4()}@example.com",
        }
        res = self.client.put(f"/api/v1/users/{fake_id}", json=payload)
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
