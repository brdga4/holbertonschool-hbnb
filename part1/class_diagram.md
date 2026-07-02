<img width="1777" height="872" alt="image" src="https://github.com/user-attachments/assets/6fdc4e26-d2c8-42ef-9210-6198ec9ca8b5" />

# Explanatory Notes

## 1. Entity Descriptions

### BaseModel

**Role:** Acts as the parent class for all main entities in the project. It provides a common ID and timestamps for every entity.

**Key Attributes:** ID (UUID4), created_at, updated_at.

---

### User

**Role:** Represents a user in the HBnB project. A user can own places, write reviews, and may also be an administrator.

**Key Attributes:** first_name, last_name, email, password, is_admin, role (UserRole).

**Key Methods:** register(), update_profile(), delete().

---

### Place

**Role:** Represents a property listed by a user.

**Key Attributes:** title, description, price, latitude, longitude.

**Key Methods:** create(), update(), delete().

---

### Review

**Role:** Represents a user's review for a place.

**Key Attributes:** rating (RatingValue), comment.

**Key Methods:** create(), update(), delete(), list_by_place().

---

### Amenity

**Role:** Represents a feature available in a place, such as Wi-Fi or a swimming pool.

**Key Attributes:** name, description.

**Key Methods:** create(), update(), delete().

---

### Enumerations

**UserRole:** Defines the available user roles (OWNER, CLIENT, BOTH).

**RatingValue:** Limits review ratings to values from 1 to 5.

---

## 2. Entity Relationships & Business Logic

### Inheritance

User, Place, Review, and Amenity inherit from BaseModel, allowing them to share the same ID and timestamps.

### User & Place (One-to-Many)

A user can own multiple places, while each place belongs to one user.

### Place & Amenity (Many-to-Many)

A place can have multiple amenities, and an amenity can belong to multiple places.

### Review, User & Place

Each review is written by one user and belongs to one place. This relationship allows the project to retrieve reviews for a specific place or by a specific user.

### Enumerations

The User entity uses the UserRole enumeration, while the Review entity uses the RatingValue enumeration to ensure only valid values are accepted.
