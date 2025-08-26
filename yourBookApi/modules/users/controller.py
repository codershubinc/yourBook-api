from flask import current_app
from typing import Dict, Any, Tuple
from yourBookApi.models.user_config import User_Config_Schema
from yourBookApi.utils.db.db_connect import DB


class user_config:

    def create_user_config(
        self,
        name: str,
        email: str,
        avatar_uri: str,
        createdAt: str,
        updatedAt: str,
        user_type: str = "regular"
    ) -> Tuple[Dict[str, Any], int]:
        """Create user config with clear TypeScript-style parameters"""
        try:
            # Check DB connection - return 500 if missing
            if not hasattr(current_app, 'mongo_client'):
                return {"error": "Database connection unavailable"}, 500

            mongo_db = getattr(current_app, 'mongo_db')

            # Check if user exists
            if mongo_db.user_config.find_one({"email": email}):
                return {"error": "User already exists"}, 409

            # Create user document
            user_doc = {
                "name": name,
                "email": email,
                "avatar_uri": avatar_uri,
                "user_type": user_type,
                "createdAt": createdAt,
                "updatedAt": updatedAt
            }

            # Save to MongoDB
            result = mongo_db.user_config.insert_one(
                User_Config_Schema(**user_doc))

            return {
                "message": "User created successfully",
                "user_id": str(result.inserted_id),
                "name": name,
                "user_type": user_type
            }, 201

        except Exception as e:
            return {"error": str(e)}, 500

    def get_user_config(
        self, email: str
    ) -> Tuple[Dict[str, Any], int]:
        """Retrieve user config by email"""
        try:
            if not hasattr(current_app, 'mongo_client'):
                return {"error": "Database connection unavailable"}, 500

            mongo_db = getattr(current_app, 'mongo_db')
            if mongo_db == None:
                reconnect_db = DB.connect()
                if not bool(reconnect_db):
                    return {"error": "Database connection unavailable"}, 500

            user = mongo_db.user_config.find_one({"email": email})

            if not user:
                return {"error": "User not found"}, 404

            user['_id'] = str(user['_id'])  # Convert ObjectId to string
            return user, 200

        except Exception as e:
            return {"error": str(e)}, 500
