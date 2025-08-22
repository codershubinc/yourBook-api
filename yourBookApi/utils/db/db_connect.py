from app import app
import os
from pymongo import MongoClient
from flask.cli import load_dotenv
from typing import Optional, Tuple, Any

# Load environment variables from .env file
load_dotenv()


class DataBase:

    @staticmethod
    def connect() -> Tuple[Optional[MongoClient[Any]], Optional[str]]:
        try:
            if hasattr(app, 'mongo_client') and hasattr(app, 'mongo_db'):

                print("\n +++++++++++++++++++++++++++++++++++++ ::: MongoDB connection already established.++++++++++++++++++++++++++++++++++++++\n ")
                print("Using existing MongoDB connection.")
                mongo_client = getattr(app, 'mongo_client')
                # print("Existing MongoDB client:", mongo_client.admin.ping())
                mongo_db = getattr(app, 'mongo_db')

                return mongo_client, getattr(mongo_db, 'name', None)

# -----------------------------------------------------------------------------------------------

            print("Connecting to MongoDB...")
            client: MongoClient[Any] = MongoClient(
                os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
            db_name = os.getenv("MONGO_DB_NAME", "mydatabase")
            # setting attributes on the app
            setattr(app, 'mongo_client', client)
            setattr(app, 'mongo_db', client[db_name])

            print("Connected to MongoDB database:", db_name)
            return client, db_name

        except Exception as e:
            print("Error connecting to MongoDB:", e)
            return None, None


DB = DataBase()
