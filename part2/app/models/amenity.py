from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that represents property amenities (e.g., Wi-Fi, Pool).
    Inherits from BaseModel to reuse common attributes.
    """
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    @property
    def name(self) -> str:
        """Getter for the amenity name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter for the amenity name with validation rules."""
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError(
                "Amenity name is required and must be a non-empty string"
            )

        if len(value) > 50:
            raise ValueError("Amenity name cannot exceed 50 characters")

        self._name = value.strip()
