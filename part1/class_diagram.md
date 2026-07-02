<img width="1777" height="872" alt="image" src="https://github.com/user-attachments/assets/6fdc4e26-d2c8-42ef-9210-6198ec9ca8b5" />

# Explanatory Notes

## 1. Entity Descriptions

### BaseModel

**Role:**  
Acts as the parent class for all main entities in the system. It provides common attributes shared by every entity.

**Key Attributes:**

- **ID (UUID4):** Unique identifier for each object.
- **created_at (DateTime):** Records when the object was created.
- **updated_at (DateTime):** Records the last update time.

---

### User

**Role:**  
Represents a user of the HBnB application. A user can own places, write reviews, and may also be an administrator.

**Key Attributes:**

- first_name
- last_name
- email
- password
- is_admin
- role (UserRole)

**Key Methods:**

- register()
- update_profile()
- delete()

---

### Place

**Role:**  
Represents a property listed by a user. It stores the information required to describe the property.

**Key Attributes:**

- title
- description
- price
- latitude
- longitude

**Key Methods:**

- create()
- update()
- delete()

---

### Review

**Role:**  
Represents a user's review for a specific place.

**Key Attributes:**

- rating (RatingValue)
- comment

**Key Methods:**

- create()
- update()
- delete()
- list_by_place()

---

### Amenity

**Role:**  
Represents a feature available in a place, such as Wi-Fi or a swimming pool.

**Key Attributes:**

- name
- description

**Key Methods:**

- create()
- update()
- delete()

---

### Enumerations

#### UserRole

Defines the available roles for users:

- OWNER
- CLIENT
- BOTH

#### RatingValue

Limits review ratings to values from **1** to **5**.

---

# 2. Entity Relationships & Business Logic

## Inheritance

`User`, `Place`, `Review`, and `Amenity` inherit from `BaseModel`.

This allows all entities to share the same ID, creation date, and update date without duplicating these attributes.

---

## User and Place (One-to-Many)

A user can own multiple places.

```text
User "1" --> "*" Place
```

Each place belongs to one owner.

---

## Place and Amenity (Many-to-Many)

A place can have multiple amenities, and an amenity can be associated with multiple places.

```text
Place "*" --> "*" Amenity
```

This avoids creating duplicate amenities for different places.

---

## Review, User, and Place

Each review is linked to:

- One user (the author).
- One place.

```text
Review "*" --> "1" User
Review "*" --> "1" Place
```

This relationship allows the system to retrieve all reviews for a place or all reviews written by a specific user.

---

## Enumerations

The `User` entity uses the `UserRole` enumeration, while the `Review` entity uses the `RatingValue` enumeration.

Using enumerations helps ensure that only valid values are accepted for user roles and review ratings. `User` and `Review` entities rely strictly on `UserRole` and `RatingValue` respectively (`--> : uses`). This prevents invalid data entries at the application logic level before interacting with the database layer.
