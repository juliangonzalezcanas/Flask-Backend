import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "Julixx26")
    MYSQL_DB = os.getenv("MYSQL_DB", "clothing")