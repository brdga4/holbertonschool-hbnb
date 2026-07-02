```mermaid
---
config:
  layout: elk
---
classDiagram
direction LR
    class UserRole {
        <<enumeration>>
        OWNER
        CLIENT
        BOTH
    }

    class Review {
        +Int rating
        +String comment
        +UUID4 user_id
        +UUID4 place_id
        +list_by_place()
        +create()
        +update()
        +delete()
    }

	class RatingValue {
        <<enumeration>>
        1
		2
		3
		4
		5
    }

    class BaseModel {
        +UUID4 ID
        +DateTime created_at
        +DateTime updated_at
    }

    class User {
        +String first_name
        +String last_name
        +String email
        +String password
        +UserRole role
		+boolean is_admin
        +register()
        +update_profile()
        +delete()
    }

    class Place {
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +UUID4 owner_id
        +create()
        +update()
        +delete()
    }

    class Amenity {
        +String name
        +String description
        +create()
        +update()
        +delete()
    }

    User --|> BaseModel : inherits
    User --> UserRole : uses
    User "1" --> "*" Place : owns
    Place --|> BaseModel : inherits
    Place "*" --> "*" Amenity : has
    Review --|> BaseModel : inherits
    Review "*" --> "1" User : written_by
    Review "*" --> "1" Place : reviews
    Review --> RatingValue : uses
    Amenity --|> BaseModel : inherits
