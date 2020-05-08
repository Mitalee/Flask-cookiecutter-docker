
DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordev'


# SQLAlchemy.
db_uri = 'postgresql://flaskwallet:walletpassword@postgres:5432/flaskwallet'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
