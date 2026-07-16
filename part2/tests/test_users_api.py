import unittest
from app import create_app


class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_success(self):
        response = self.client.post(
            '/api/v1/users/',
            json={
                'first_name': 'John',
                'last_name': 'Wick',
                'email': 'john.wick@continental.com'
            }
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['first_name'], 'John')

    def test_create_user_bad_request_empty_name(self):
        response = self.client.post(
            '/api/v1/users/',
            json={
                'first_name': '',
                'last_name': 'Wick',
                'email': 'john.wick@continental.com'
            }
        )
        self.assertEqual(response.status_code, 400)

    def test_create_user_bad_request_invalid_email(self):
        response = self.client.post(
            '/api/v1/users/',
            json={
                'first_name': 'John',
                'last_name': 'Wick',
                'email': 'invalid-email-format'
            }
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
