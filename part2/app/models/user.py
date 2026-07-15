import re
from app.models.baseModel import BaseModel


class User(BaseModel):
    """
    User class representing application users.
    Uses properties to ensure validation rules are always enforced.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        is_admin: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("First name is required and must be a non-empty string.")
        if len(value) > 50:
            raise ValueError("First name cannot exceed 50 characters.")
        self._first_name = value.strip()

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError("Last name is required and must be a non-empty string.")
        if len(value) > 50:
            raise ValueError("Last name cannot exceed 50 characters.")
        self._last_name = value.strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Email is required.")

        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, value.strip()):
            raise ValueError("Invalid email format.")

        self._email = value.strip()
