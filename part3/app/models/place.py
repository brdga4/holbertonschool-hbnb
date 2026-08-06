from app import db
from app.models.base import BaseModel
from sqlalchemy.orm import validates


class Place(BaseModel):
    __tablename__ = "places"

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title, price, latitude, longitude, description=None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @validates("title")
    def validate_title(self, key, title):
        if not title or not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        return title.strip()

    @validates("price")
    def validate_price(self, key, price):
        if price is None or price <= 0:
            raise ValueError("Price must be a positive number.")
        return float(price)

    @validates("latitude")
    def validate_latitude(self, key, latitude):
        if latitude is None or not (-90.0 <= float(latitude) <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        return float(latitude)

    @validates("longitude")
    def validate_longitude(self, key, longitude):
        if longitude is None or not (-180.0 <= float(longitude) <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        return float(longitude)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
