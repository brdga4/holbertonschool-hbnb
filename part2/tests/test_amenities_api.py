import unittest
from app import create_app


class TestAmenityAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity_success(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json={'name': 'Gold Coins'}
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['name'], 'Gold Coins')

    def test_create_amenity_invalid_name(self):
        response = self.client.post(
            '/api/v1/amenities/',
            json={'name': ''}
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all_amenities(self):
        self.client.post('/api/v1/amenities/', json={'name': 'Tactical Suit'})
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
