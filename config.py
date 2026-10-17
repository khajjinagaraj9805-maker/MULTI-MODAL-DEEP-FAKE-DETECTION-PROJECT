import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = "deepfake_secret_key_2026"

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "Nagaraj@2005"
    MYSQL_DB = "deepfake_detection"

    password = quote_plus(MYSQL_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{password}@{MYSQL_HOST}/{MYSQL_DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join("static", "uploads")

    MAX_CONTENT_LENGTH = 200 * 1024 * 1024