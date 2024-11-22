from app import app, db  # Ensure 'app' is the name of your Flask app file (without .py extension)

# Create the application context
with app.app_context():
    # Create the database and the Todo table
    db.create_all()

print("Database and tables created!")