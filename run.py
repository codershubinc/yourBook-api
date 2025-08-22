from flask import Flask
from pymongo import MongoClient
import os
from yourBookApi.modules.users.controller import user_config_bp

app = Flask(__name__)

# MongoDB configuration (env or defaults)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "myapp")

# Do not create a Mongo client at import time to avoid DNS/SRV delays or failures.
# Controllers will return 500 if the client isn't initialized.
app.mongo_client = MongoClient(MONGO_URI)  # type: ignore[attr-defined]
print("connecting to mongo db client :::", app.mongo_client)


@app.route('/')
def home():
    return "Welcome to the YourBook API! , just a debugging test || DONE"

# add temporarily in run.py to verify


@app.get("/health/db")
def db_health():
    client = getattr(app, "mongo_client", None)
    if client is None:
        return {"db": "not-initialized"}, 503
    try:
        client.admin.command("ping")
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}, 500


# Register blueprints
app.register_blueprint(user_config_bp)


if __name__ == '__main__':
    app.run(debug=True)
