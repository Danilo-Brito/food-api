from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_openapi3 import Tag, OpenAPI

app = OpenAPI(__name__)
app.config.from_pyfile('config.py')
CORS(app)

db = SQLAlchemy(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
food_tag = Tag(name="Alimento", description="Adição, visualização e remoção dos alimento da base")
