import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import quote_plus # <-- IMPORTAR ISSO

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db_user = os.environ.get('DB_USER')
    db_pass_raw = os.environ.get('DB_PASS', '')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    db_pass_encoded = quote_plus(db_pass_raw)

    database_url = f"postgresql://{db_user}:{db_pass_encoded}@{db_host}:{db_port}/{db_name}"

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from . import routes
    routes.init_app(app)

    return app