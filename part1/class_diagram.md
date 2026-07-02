<img width="1777" height="872" alt="image" src="https://github.com/user-attachments/assets/6fdc4e26-d2c8-42ef-9210-6198ec9ca8b5" />

## Explanatory Notes

### 1. Entity Descriptions

*   **`BaseModel`**
    *   **Role:** Acts as the foundational parent class for all primary entities in the system. It ensures that every object shares a consistent identification and auditing mechanism.
    *   **Key Attributes:** `ID` (UUID4) for unique identification, `created_at` (DateTime) for tracking creation time, and `updated_at` (DateTime) for tracking modifications.

*   **`User`**
    *   **Role:** Represents the individuals interacting with the platform. A user can act as a client, an owner, or both, managed securely through role-based enumeration.
    *   **Key Attributes:** `first_name`, `last_name`, `email`, `password`, `is_admin` (Boolean), and `role` (using the `UserRole` Enum).
    *   **Key Methods:** `register()`, `update_profile()`, `delete()`.

*   **`Place`**
    *   **Role:** The central operational entity representing a property listed for rent. It holds all descriptive and geographical data required for listing and booking.
    *   **Key Attributes:** `title`, `description`, `price` (Float), `latitude` (Float), and `longitude` (Float).
    *   **Key Methods:** `create()`, `update()`, `delete()`.

*   **`Review`**
    *   **Role:** Represents user feedback for specific places. It strictly enforces rating boundaries to maintain data integrity.
    *   **Key Attributes:** `comment` (String) and `rating` (using the restricted `RatingValue` Enum).
    *   **Key Methods:** `create()`, `update()`, `delete()`, and `list_by_place()` (a query method to retrieve all reviews for a specific property).

*   **`Amenity`**
    *   **Role:** Represents individual features or facilities offered by a place (e.g., Wi-Fi, Pool).
    *   **Key Attributes:** `name` and `description`.
    *   **Key Methods:** `create()`, `update()`, `delete()`.

*   **Enumerations (Enums)**
    *   **`UserRole`:** Defines strict roles (`OWNER`, `CLIENT`, `BOTH`) to manage user capabilities dynamically without complex database schemas.
    *   **`RatingValue`:** Restricts review ratings strictly to numerical values from 1 to 5, providing structural defensive programming.

---

### 2. Entity Relationships & Business Logic

The interactions between these entities define the core operations of the HBnB application:

*   **Inheritance (Generalization):**
    *   `User`, `Place`, `Review`, and `Amenity` all inherit (`--|>`) from `BaseModel`. This ensures adherence to the DRY (Don't Repeat Yourself) principle, automatically propagating the `ID` and timestamp attributes to all child entities.

*   **User & Place (1-to-Many Association):**
    *   A `User` can own multiple `Places` (`User "1" --> "*" Place : owns`). This establishes the core host-property dynamic, where an owner manages a portfolio of listings.

*   **Place & Amenity (Many-to-Many Association):**
    *   A `Place` can feature multiple `Amenities`, and a specific `Amenity` can be present across multiple `Places` (`Place "*" --> "*" Amenity : has`). This optimizes the system by creating amenities only once globally and linking them dynamically to properties.

*   **Review & User/Place (Many-to-1 Association):**
    *   A `Review` is intrinsically tied to two entities: the author and the target property. 
    *   It is written by one `User` (`Review "*" --> "1" User : written_by`).
    *   It targets exactly one `Place` (`Review "*" --> "1" Place : reviews`). 
    *   *Business Logic Value:* This structure allows the system to easily fetch all reviews written by a specific user, or calculate the average rating for a specific place.

*   **Dependency on Enums:**
    *   The `User` and `Review` entities rely strictly on `UserRole` and `RatingValue` respectively (`--> : uses`). This prevents invalid data entries at the application logic level before interacting with the database layer.
