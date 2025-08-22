from flask import Flask
import os
from typing import Dict, Any, Union, Tuple

app = Flask(__name__)


@app.route('/')
def home() -> Dict[str, Any]:
    return {
        'message': 'yourBook API is running!',
        'mongo_uri_configured': bool(os.getenv('MONGO_URI')),
        'mongo_db_name': os.getenv('MONGO_DB_NAME', 'Not configured')
    }


@app.route('/health')
def health() -> Union[Dict[str, Any], Tuple[Dict[str, str], int]]:
    from yourBookApi.utils.db.db_connect import DB
    client, db_name = DB.connect()
    try:
        # if app.mongo_client:
        #     return {'status': 'healthy', 'database': 'connected'}
        if client:
            return {'status': 'healthy', 'database': 'connected', 'db_name': db_name}
        else:
            return {'status': 'unhealthy', 'database': 'disconnected'}, 500
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500
