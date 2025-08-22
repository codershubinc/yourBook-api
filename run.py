from app import app
from yourBookApi.utils.db.db_connect import DB
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    # Connect to database before starting the app
    DB.connect()
    app.run(debug=True)
