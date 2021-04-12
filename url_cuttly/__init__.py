from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from .config import SQLALCHEMY_DATABASE_URI

# import config

# Database
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Application
app = Flask(__name__)
# app.config.from_object('config')

from url_cuttly.views import *