#  adding bp to the app
from flask import Flask
from yourBookApi.modules.users.routes import user_config_bp


bps = [
    user_config_bp
]


def register_blueprints(app: Flask) -> None:
    for bp in bps:
        print("Registering the BPs")
        app.register_blueprint(bp)
