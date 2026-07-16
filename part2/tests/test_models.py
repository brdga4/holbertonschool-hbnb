import unittest
from app.models.user import User


class TestUserModel(unittest.TestCase):
    def test_user_creation_success(self):
        user = User(
            first_name="John", last_name="Wick", email="john.wick@continental.com"
        )
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Wick")
        self.assertEqual(user.email, "john.wick@continental.com")
        self.assertFalse(user.is_admin)

    def test_first_name_required(self):
        with self.assertRaises(ValueError) as context:
            User(first_name="", last_name="Wick", email="john.wick@continental.com")
        self.assertIn("First name is required", str(context.exception))

    def test_first_name_too_long(self):
        long_name = "a" * 51
        with self.assertRaises(ValueError) as context:
            User(
                first_name=long_name,
                last_name="Wick",
                email="john.wick@continental.com",
            )
        self.assertIn("First name cannot exceed 50 characters", str(context.exception))

    def test_last_name_required(self):
        with self.assertRaises(ValueError) as context:
            User(first_name="John", last_name="   ", email="john.wick@continental.com")
        self.assertIn("Last name is required", str(context.exception))

    def test_email_invalid_format(self):
        invalid_emails = ["not-an-email", "jwick@", "jwick@com", "@continental.com"]
        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(ValueError) as context:
                    User(first_name="John", last_name="Wick", email=email)
                self.assertIn("Invalid email format", str(context.exception))


if __name__ == "__main__":
    unittest.main()
