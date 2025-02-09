# config.py
class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/Matching'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # type : ignore
    # This is only used for API
