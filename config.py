import os

class Config(obj):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    MONGODB_SETTINGS = { 'db': 'ksps_db01' }
