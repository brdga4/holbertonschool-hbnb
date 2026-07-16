# HBnB API – Testing & Validation Report

## 1. Overview
Project: HBnB – Part 2 (API Layer). This report documents the testing and validation process for the HBnB API. The goal was to ensure that all CRUD operations for Users, Places, Amenities, and Reviews function correctly and adhere to the validation rules defined in the business logic layer. Testing included: Manual cURL tests, Swagger documentation verification, Automated unit tests using unittest, and Validation of entity relationships.

## 2. Validation Implementation
Validation was implemented at the model level to ensure data integrity.

### User Validation
* first_name, last_name, and email must not be empty.
* Email must follow a valid format.
* Duplicate emails are rejected.

### Place Validation
* title must not be empty.
* price must be non‑negative.
* latitude must be between –90 and 90.
* longitude must be between –180 and 180.
* owner_id must reference an existing user.
* amenities must reference valid amenity IDs.

### Review Validation
* text must not be empty.
* rating must be between 1 and 5.
* user_id and place_id must reference valid entities.

### Amenity Validation
* name must not be empty.

## 3. Black‑Box Testing Using cURL
Manual tests were performed to validate real API behavior.

### 3.1 User Endpoint Tests
Create User – Valid Input: curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{ "first_name": "John", "last_name": "Wick", "email": "john.wick@example.com" }'. Response (201): { "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "first_name": "John", "last_name": "Wick", "email": "john.wick@example.com" }.

Create User – Invalid Input: curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{ "first_name": "", "last_name": "", "email": "invalid-email" }'. Response (400): { "error": "Invalid input data" }.

### 3.2 Place Endpoint Tests
Create Place – Invalid Latitude: curl -X POST "http://127.0.0.1:5000/api/v1/places/" -H "Content-Type: application/json" -d '{ "title": "Bad Place", "price": 50, "latitude": 200, "longitude": 30, "owner_id": "valid-user-id", "amenities": [] }'. Response (400): { "error": "Latitude must be between -90 and 90" }.

Update Place – Success: curl -X PUT "http://127.0.0.1:5000/api/v1/places/<place_id>" -H "Content-Type: application/json" -d '{ "title": "Updated Place", "price": 120, "latitude": 20, "longitude": 30, "owner_id": "valid-user-id", "amenities": ["amenity-id"] }'. Response (200): { "message": "Place updated successfully" }.

### 3.3 Review Endpoint Tests
Create Review – Invalid Rating: curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" -H "Content-Type: application/json" -d '{ "text": "Bad", "rating": 10, "user_id": "valid-user-id", "place_id": "valid-place-id" }'. Response (400): { "error": "Rating must be an integer between 1 and 5" }.

Delete Review – Success: curl -X DELETE "http://127.0.0.1:5000/api/v1/reviews/<review_id>". Response (200): { "message": "Review deleted successfully" }.

## 4. Swagger Documentation Verification
Swagger UI was accessed at: http://127.0.0.1:5000/api/v1/. Verification included: All endpoints appear under their namespaces, Models display correct fields and data types, Example inputs match actual API behavior, and “Try it out” tests succeeded for all endpoints.

## 5. Automated Unit Testing
Automated tests were written using Python’s unittest framework.

### 5.1 User Tests
def test_create_user(self): response = self.client.post('/api/v1/users/', json={ "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com" }); self.assertEqual(response.status_code, 201).
def test_create_user_invalid_data(self): response = self.client.post('/api/v1/users/', json={ "first_name": "", "last_name": "", "email": "invalid-email" }); self.assertEqual(response.status_code, 400).

### 5.2 Place Tests
def test_update_place_success(self): res = self.client.put(f"/api/v1/places/{self.place.id}", json={ "title": "Nice Place", "price": 120, "latitude": 20, "longitude": 30, "owner_id": self.user.id, "amenities": [self.amenity.id] }); self.assertEqual(res.status_code, 200).

### 5.3 Review Tests
def test_create_review_invalid_rating(self): res = self.client.post("/api/v1/reviews/", json={ "text": "Bad", "rating": 10, "user_id": self.user.id, "place_id": self.place.id }); self.assertEqual(res.status_code, 400).

## 6. Status Code Summary
| Status | Meaning | Verified In |
| :--- | :--- | :--- |
| 200 | OK | Successful GET/PUT/DELETE |
| 201 | Created | Successful POST |
| 400 | Bad Request | Validation failure |
| 404 | Not Found | Missing resource |

## 7. Final Results
All endpoints were validated through Model-level validation, Manual cURL testing, Swagger documentation, and Automated unit tests. All tests passed successfully, confirming that the API behaves exactly as required by the project specifications.

## 8. Conclusion
The HBnB API has been fully validated through a combination of automated and manual testing. All endpoints enforce the required validation rules, handle errors correctly, and return consistent HTTP status codes. The API is stable, predictable, and ready for integration with future components. The testing process confirmed correct behavior across all CRUD operations and ensured that relationships between Users, Places, Amenities, and Reviews are handled reliably.
