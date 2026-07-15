import re
from app.models.baseModel import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("First name must be 50 characters or less.")
        self.first_name = first_name

        if not last_name or len(last_name) > 50:
            raise ValueError("Last name must be 50 characters or less.")
        self.last_name = last_name

        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not email or not re.match(email_regex, email):
            raise ValueError("Invalid email format.")
        self.email = email

        self.is_admin = is_admin
