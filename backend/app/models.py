from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    
    def __init__(self, nome, email, telefone=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    ano_lancamento = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    estoque = db.Column(db.Integer, nullable=False, default=1)

    def to_json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano_lancamento": self.ano_lancamento,
            "genero": self.genero,
            "estoque": self.estoque
        }