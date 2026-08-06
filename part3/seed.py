from app import create_app, db
from app.models.user import User
from app.models.amenity import Amenity

app = create_app()

with app.app_context():

    db.create_all()

    admin_email = "admin@hbnb.io"
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(
            first_name="Admin",
            last_name="HBnB",
            email=admin_email,
            password="admin123_password",
            is_admin=True
        )
        db.session.add(admin)
        print("Admin user created.")

    wifi = Amenity.query.filter_by(name="Wi-Fi").first()
    if not wifi:
        wifi = Amenity(name="Wi-Fi")
        db.session.add(wifi)

    db.session.commit()
    print("Database seeded successfully!")
