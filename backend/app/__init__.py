"""Preparação do Ambiente (Imports e Variáveis Globais)"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from urllib.parse import quote_plus
#Leitura do .env
load_dotenv()
#Criação do objeto banco de dados
db = SQLAlchemy()
"""Preparação do Ambiente (Imports e Variáveis Globais)"""

"""Inicio da Aplicação"""
def create_app():
    #Iniciando flask
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    #Configurando o banco de dados
    db_user = os.environ.get('DB_USER')
    db_pass_raw = os.environ.get('DB_PASS', '')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    #Tratamento da senha com caracteres
    db_pass_encoded = quote_plus(db_pass_raw)
    #URL do banco de dados
    database_url = f"postgresql://{db_user}:{db_pass_encoded}@{db_host}:{db_port}/{db_name}"
    #Injeta a configuração do banco de dados ao flask
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Inicia o banco de dados
    db.init_app(app)
    #Inicia o CORS
    # Em produção, troca-se o "*" pelo domínio real
    #CORS(app, resources={r"/api/*": {"origins": ["https://meusite.com.br", "https://app.meusite.com"]}})
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    #Importa as rotas
    from . import routes
    routes.init_app(app)

    return app
"""Inicio da Aplicação"""