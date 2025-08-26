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


@user_config_bp.route('/config', methods=['GET'])
def get_user_config():
    email = request.get_json().get('email') if request.get_json() else None

    if not email:
        return jsonify({"error": "email required"}), 400

    response, status = controller.get_user_config(email=email)
    return jsonify(response), status


@user_config_bp.route('/config', methods=['PATCH'])
def update_user_config():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON required"}), 400

    email: str = data.get('email')
    name: str = data.get('name')
    avatar_uri: str = data.get('avatar_uri')

    if not email:
        return jsonify({"error": "email required"}), 400

    # Generate updated timestamp
    from datetime import datetime
    updated_time = datetime.now().isoformat()

    response, status = controller.update_user_config(
        email=email,
        name=name,
        avatar_uri=avatar_uri,
        updatedAt=updated_time,
        # Assuming createdAt is sent in the request
        createdAt=data.get('createdAt', ''),
        user_type=data.get('user_type', 'regular')
    )

    return jsonify(response), status
