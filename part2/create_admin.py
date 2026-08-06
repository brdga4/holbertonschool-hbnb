from app.services import facade


def seed_admin():
    admin_data = {
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@hbnb.com",
        "password": "root",
        "is_admin": True
    }

    existing_admin = facade.get_user_by_email(admin_data["email"])
    if existing_admin:
        return

    try:
        new_admin = facade.create_user(admin_data)
        print("Admin user created successfully!")
        print(f"ID: {new_admin.id}")
        print(f"Email: {new_admin.email}")
        print(f"Password: root")
    except ValueError as e:
        print(f"Error creating admin: {e}")


if __name__ == "__main__":
    seed_admin()
