from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("reviews", description="Review operations")

review_model = api.model(
    "Review",
    {
        "text": fields.String(required=True, description="Text of the review"),
        "rating": fields.Integer(
            required=True, description="Rating of the place (1-5)"
        ),
        "user_id": fields.String(
            required=True, description="ID of the user writing the review"
        ),
        "place_id": fields.String(
            required=True, description="ID of the place being reviewed"
        ),
    },
)


@api.route("/")
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @api.response(201, "Review successfully created")
    @api.response(400, "Invalid input data or missing user/place")
    def post(self):
        """Register a new review"""
        try:
            new_review = facade.create_review(api.payload)

            rating_value = (
                new_review.rating.value
                if hasattr(new_review.rating, "value")
                else new_review.rating
            )

            return {
                "id": new_review.id,
                "text": new_review.text,
                "rating": rating_value,
                "user_id": new_review.user.id,
                "place_id": new_review.place.id,
            }, 201
        except ValueError as error:
            return {"error": str(error)}, 400

    @api.response(200, "List of reviews retrieved successfully")
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [
            {
                "id": rev.id,
                "text": rev.text,
                "rating": rev.rating.value
                if hasattr(rev.rating, "value")
                else rev.rating,
            }
            for rev in reviews
        ], 200


@api.route("/<review_id>")
class ReviewResource(Resource):
    @api.response(200, "Review details retrieved successfully")
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        rating_value = (
            review.rating.value if hasattr(review.rating, "value") else review.rating
        )

        return {
            "id": review.id,
            "text": review.text,
            "rating": rating_value,
            "user_id": review.user.id,
            "place_id": review.place.id,
        }, 200

    @api.expect(review_model)
    @api.response(200, "Review updated successfully")
    @api.response(404, "Review not found")
    @api.response(400, "Invalid input data")
    def put(self, review_id):
        """Update a review's information"""
        try:
            updated_review = facade.update_review(review_id, api.payload)
            if not updated_review:
                return {"error": "Review not found"}, 404
            return {"message": "Review updated successfully"}, 200
        except ValueError as error:
            return {"error": str(error)}, 400

    @api.response(200, "Review deleted successfully")
    @api.response(404, "Review not found")
    def delete(self, review_id):
        """Delete a review"""
        success = facade.delete_review(review_id)
        if not success:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted successfully"}, 200
