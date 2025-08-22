from flask import Blueprint, request, jsonify
from yourBookApi.modules.users.controller import user_config

# Create blueprint
user_config_bp = Blueprint('user_config', __name__, url_prefix='/user')
controller = user_config()


@user_config_bp.route('/config', methods=['POST'])
def create_user_config():
    """POST /user/config - Simple endpoint like TS"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON required"}), 400

    # Extract typed parameters
    name: str = data.get('name')
    email: str = data.get('email')
    avatar_uri: str = data.get('avatar_uri', '')
    user_type: str = data.get('user_type', 'regular')

    # Generate timestamps
    from datetime import datetime
    current_time = datetime.now().isoformat()

    if not name or not email:
        return jsonify({"error": "name and email required"}), 400

    # Call controller with typed params
    response, status = controller.create_user_config(
        name=name,
        email=email,
        avatar_uri=avatar_uri,
        createdAt=current_time,
        updatedAt=current_time,
        user_type=user_type
    )

    return jsonify(response), status
