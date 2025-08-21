"""
User configuration endpoints.

This module exposes a minimal endpoint to create a user configuration document
in MongoDB. It is intentionally lightweight and self-contained so it can be
registered directly with a Flask app without extra dependencies.

Endpoint contract
-----------------
POST /user/config

Request JSON body:
{
    "name": string,   // required
    "pass": string    // required (note: stored as plain text in this example)
}

Responses:
- 201 Created: { _id: string, name: string, pass: string }
- 400 Bad Request: { error: "Missing name or pass" }
- 500 Internal Server Error: { error: string } (on unexpected DB errors)

Behavior & design notes
-----------------------
- The code looks for a long-lived MongoClient attached to the Flask app as
    `current_app.mongo_client`. If not present, it returns 500 and does not
    attempt to create a new client (no auto reconnect).
- Environment variables used:
    - MONGO_URI (default: mongodb://localhost:27017)
    - MONGO_DB_NAME (default: myapp)
- The document is saved into the `user_config` collection.
- For a production system, DO NOT store passwords in plain text. Replace
    `pass` with a hashed value (e.g., using werkzeug.security or passlib).

Example curl
------------
curl -X POST http://localhost:5000/user/config \
    -H "Content-Type: application/json" \
    -d '{"name":"alice","pass":"secret"}'

Blueprint registration
----------------------
from yourBookApi.modules.users.controller import user_config_bp
app.register_blueprint(user_config_bp)  # exposes /user/config
"""

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
