from urllib.parse import quote
import secrets

class Config():
    HOST = "0.0.0.0"
    DB_USERNAME = "postgres"
    DB_PASSWORD = quote("@Paulmburu5")
    POSTGRES_URL = "task_db"
    POSTGRES_DB = "task_management_db"
    POSTGRES_PORT = 5432
    DB_URL = 'postgresql://{user}:{pswd}@{url}:{port}/{db}?application_name=TaskManagement'.format(user=DB_USERNAME, pswd=DB_PASSWORD, url=POSTGRES_URL, port=POSTGRES_PORT, db=POSTGRES_DB)

    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = { 'task_management_db': DB_URL }

    SECRET_KEY = secrets.token_hex(16)
    SECURITY_PASSWORD_SALT = secrets.token_hex(30)

    DEFAULT_PROFILE_IMAGE = "default1.png"
    DEFAULT_STUDENT_PROFILE = "defaultIcon.png"

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

