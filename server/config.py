import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv
    ("DATABASE_URL", "postgresql://maverick:pharaoh@localhost:5432/pizza_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
