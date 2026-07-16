import unittest
from app import create_app


class TestReviewAPI(unittest.TestCase):

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
        self.user_id = user_res.get_json()['id']

        place_res = self.client.post(
            '/api/v1/places/',
            json={
                'title': 'The Continental',
                'price': 500.0,
                'owner_id': self.user_id
            }
        )
        self.place_id = place_res.get_json()['id']

    def test_create_review_success(self):
        response = self.client.post(
            '/api/v1/reviews/',
            json={
                'text': 'Behold, excellent service and strict rules.',
                'rating': 5,
                'user_id': self.user_id,
                'place_id': self.place_id
            }
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['rating'], 5)

    def test_create_review_invalid_rating(self):
        response = self.client.post(
            '/api/v1/reviews/',
            json={
                'text': 'The rating is out of bounds',
                'rating': 6,
                'user_id': self.user_id,
                'place_id': self.place_id
            }
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
