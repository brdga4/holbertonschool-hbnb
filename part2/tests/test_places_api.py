import unittest
from app import create_app


class TestPlaceAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        user_res = self.client.post(
            '/api/v1/users/',
            json={
                'email': 'john.wick@continental.com',
                'first_name': 'John',
                'last_name': 'Wick'
            }
        )
        self.owner_id = user_res.get_json()['id']

    def test_create_place_success(self):
        response = self.client.post(
            '/api/v1/places/',
            json={
                'title': 'The Continental',
                'description': 'Strictly professional sanctuary hotel',
                'price': 500.0,
                'latitude': 40.7128,
                'longitude': -74.0060,
                'owner_id': self.owner_id
            }
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['title'], 'The Continental')

    def test_create_place_invalid_price(self):
        response = self.client.post(
            '/api/v1/places/',
            json={
                'title': 'The Continental',
                'price': -100.0,
                'owner_id': self.owner_id
            }
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
