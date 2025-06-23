# 🎬 MoviWebApp

A Flask-based web application for managing your personal movie collection with a delicious popcorn-themed interface.

## 📦 Features

- **User Management**: Create and manage user profiles
- **Movie Collection**: Add movies to your personal collection
- **OMDb Integration**: Automatically fetch movie details using the OMDb API
- **Beautiful Interface**: Popcorn-themed design with image backgrounds

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/AndErem314/MoviWebApp.git
cd MoviWebApp
```

### 2. Set up your environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure the API key

Create a .env file in the root directory with your OMDb API key:
```
OMDB_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

You can get a free key from https://www.omdbapi.com/apikey.aspx.

### 4. Initialize the database
```
python init_db.py
```
### 5. Run the app
```
flask run
```
## 📋 Requirements
	•	Python 3.7+
    •	Flask 2.0+
    •	SQLAlchemy
    •	python-dotenv
	•	Internet connection (for OMDb API)
	•	OMDb API key
    •	SECRET KEY for flash

## ✅ License

This project is open-source and free to use for educational and personal purposes.