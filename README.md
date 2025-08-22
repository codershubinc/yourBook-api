# yourBook API

A Flask-based REST API for managing personal books, reading progress, and sharing functionality.

## 🚀 Features

- **User Management**: User registration, authentication, and profile management
- **Book Management**: Add, edit, and organize personal book collections
- **Reading Progress**: Track reading progress with page-by-page updates
- **Sharing**: Share books and reading progress with friends
- **Health Monitoring**: Built-in health check endpoints
- **MongoDB Integration**: Robust database connectivity with connection pooling

## 🛠️ Tech Stack

- **Backend**: Flask 3.1.1
- **Database**: MongoDB (via PyMongo 4.14.1)
- **Environment**: Python 3.13+ with virtual environment
- **Production**: Gunicorn WSGI server
- **Testing**: pytest with Flask integration

## 📋 Prerequisites

- Python 3.13 or higher
- MongoDB Atlas account or local MongoDB installation
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/codershubinc/yourBook-api.git
   cd yourBook-api
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
   MONGO_DB_NAME=yourDayBookApi
   ```

   The `.flaskenv` file is already configured for development:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   FLASK_DEBUG=1
   FLASK_RUN_PORT=5001
   ```

## 🚀 Running the Application

### Development Mode

**Option 1: Using Flask CLI (Recommended)**

```bash
source .venv/bin/activate
flask run
```

**Option 2: Using Python directly**

```bash
source .venv/bin/activate
python run.py
```

The API will be available at `http://localhost:5001`

### Production Mode

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 📁 Project Structure

```
yourBook-api/
├── app.py                     # Flask application instance
├── run.py                     # Application entry point
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (private)
├── .flaskenv                  # Flask environment variables (public)
├── yourBookApi/
│   ├── __init__.py
│   ├── core/                  # Core functionality
│   │   ├── auth.py           # Authentication logic
│   │   └── extensions.py     # Flask extensions
│   ├── models/               # Database models
│   ├── modules/              # Feature modules
│   │   ├── books/           # Book management
│   │   ├── users/           # User management
│   │   └── sharing/         # Sharing functionality
│   ├── routes/              # API routes
│   └── utils/               # Utility functions
│       ├── cloudinary_service.py
│       └── db/
│           └── db_connect.py # Database connection
└── typings/                 # Type definitions
```

## 🔗 API Endpoints

### Core Endpoints

- `GET /` - API status and configuration info
- `GET /health` - Health check with database connectivity

### Planned Endpoints

- `POST /users` - Create new user
- `GET /users/{id}` - Get user profile
- `POST /books` - Add new book
- `GET /books` - List user's books
- `PUT /books/{id}/progress` - Update reading progress
- `POST /sharing` - Share book with friends

## 🗄️ Database Schema

The API uses MongoDB with the following main collections:

- **users**: User profiles and authentication
- **books**: Book metadata and user collections
- **reading_progress**: Page-by-page reading tracking
- **sharing**: Book sharing and social features

## 🧪 Testing

Run the test suite:

```bashv
# Install test dependencies (if not already installed)
pip install pytest pytest-flask

# Run tests
pytest

# Run with coverage
pytest --cov=yourBookApi
```

## 🔍 Health Check

Check if the API and database are running properly:

```bash
curl http://localhost:5001/health
```

Expected response:

```json
{
  "status": "healthy",
  "database": "connected",
  "db_name": "yourDayBookApi"
}
```

##  Documentation

- [API Architecture](./yourBookApi_detailed_architecture.excalidraw) - Visual architecture diagram
- [Project Plan](./yourBookApi_project_plan.md) - Development roadmap and requirements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **codershubinc** - _Initial work_ - [GitHub](https://github.com/codershubinc)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- MongoDB for reliable database services
- Python ecosystem for robust development tools
