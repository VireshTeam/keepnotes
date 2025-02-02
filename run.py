from app import create_app, db
import os

app = create_app()

with app.app_context():
    db.create_all()  # Create tables

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port =8080)

