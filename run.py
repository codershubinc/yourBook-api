from app import app
from yourBookApi.routes.user_routes import register_blueprints
from yourBookApi.utils.db.db_connect import DB
from dotenv import load_dotenv

load_dotenv()

print("Starting the Flask application...", __name__)
# Connect to database before starting the app
DB.connect()
# register blueprints
print("Registering the Blueprints now")
register_blueprints(app)
app.run(debug=True)
