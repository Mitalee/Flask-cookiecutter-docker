from flask import Blueprint

user = Blueprint('user', __name__)

## to ensure alembic generates migrations properly
from . import models