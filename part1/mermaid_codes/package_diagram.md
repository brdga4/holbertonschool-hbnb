---
config:
  layout: elk
---
classDiagram
direction TB
    namespace PresentationLayer {
        class API {
        }

    }
    namespace BusinessLogicLayer {
        class HBnBFacade {
        }

        class User {
        }

        class Place {
        }

        class Review {
        }

        class Amenity {
        }

        class BaseModel {
        }

        class UserRole {
            <<enumeration>>
        }

        class RatingValue {
            <<enumeration>>
        }
    }
    namespace PersistenceLayer {
        class RepositoryInterface {
        }

        class InMemoryRepository {
        }

        class SQLRepository {
        }

    }
    User --|> BaseModel
    Place --|> BaseModel
    Review --|> BaseModel
    Amenity --|> BaseModel

    API --> HBnBFacade : Facade Pattern
    HBnBFacade --> User
    HBnBFacade --> Place
    HBnBFacade --> Review
    HBnBFacade --> Amenity
    User --> RepositoryInterface : Database Operations
    User --> UserRole
    Place --> RepositoryInterface : Database Operations
    Review --> RepositoryInterface : Database Operations
    Review --> RatingValue
    Amenity --> RepositoryInterface : Database Operations
    InMemoryRepository ..|> RepositoryInterface : Implements
    SQLRepository ..|> RepositoryInterface : Implementsgits