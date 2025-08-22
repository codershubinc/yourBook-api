from flask import Flask
import os
import json
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
        if client and db_name:
            # Test find_one on the database
            db = client[db_name]  # Get the database
            collection = db.user_config  # Get the user_config collection

            # Get all documents from collection
            all_documents = list(collection.find())

            # Convert ObjectIds to strings for JSON serialization
            for doc in all_documents:
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])

            # Print all collection data as JSON
            print("All Collection Data (JSON):")
            print(json.dumps(all_documents, indent=2))
            print(f"Total documents found: {len(all_documents)}")

            return {
                'status': 'healthy',
                'database': 'connected',
                'db_name': db_name,
                'total_documents': len(all_documents),
                'all_data': all_documents
            }
        else:
            return {'status': 'unhealthy', 'database': 'disconnected'}, 500
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500
