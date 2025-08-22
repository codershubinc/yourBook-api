from flask import Blueprint, request, jsonify, current_app
import os

user_config_bp = Blueprint("user_config", __name__)


@user_config_bp.route("/user/config", methods=["POST"])
def create_user_config():
    """Create a user configuration document.

    Reads JSON from the request, validates required fields, inserts a document
    into the `user_config` collection, and returns the created document with
    the inserted `_id` stringified.
    """
    # Parse and validate input JSON (force=True will parse even if no
    # Content-Type header was provided; you can remove force=True to be stricter)
    data = request.get_json(force=True)
    name = data.get("name")
    password = data.get("pass")
    if not name or not password:
        return {"error": "Missing name or pass"}, 400

    # Get MongoDB client and DB from app context
    # Prefer a single, long-lived MongoClient for the whole app. If one is not
    # attached, lazily create it and cache on the Flask app instance.
    mongo_client = getattr(current_app, "mongo_client", None)
    if mongo_client is None:
        return {"error": "failed to connect to MongoDB"}, 500
    # Determine DB name (prefer Flask config, fallback to env, then default)
    db_name = current_app.config.get(
        "MONGO_DB_NAME") or os.getenv("MONGO_DB_NAME", "myapp")
    db = mongo_client[db_name]

    doc = {  # type: ignore
        "name": name,
        "pass": password,
        "test_field": "test_value"
    }

    result = db.user_config.insert_one(doc)

    print(f"Inserted user config result: {result}")
    doc["_id"] = str(result.inserted_id)
    return jsonify(doc), 201
