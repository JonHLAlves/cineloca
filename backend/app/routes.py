from flask import jsonify, request
from .models import Cliente, db

def init_app(app):

    @app.route('/api/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "API da CineLoca conectada ao DB!"})

    # --- CRUD Clientes ---
    @app.route('/api/clientes', methods=['POST'])
    def create_cliente():
        data = request.get_json()
        
        if not data or not data.get('nome') or not data.get('email'):
            return jsonify({"error": "Nome e Email são obrigatórios"}), 400

        novo_cliente = Cliente(
            nome=data.get('nome'),
            email=data.get('email'),
            telefone=data.get('telefone')
        )
        
        try:
            db.session.add(novo_cliente)
            db.session.commit()
            return jsonify(novo_cliente.to_json()), 201 # 201 = Created
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao criar cliente: {str(e)}"}), 500

    #Todos os clientes
    @app.route('/api/clientes', methods=['GET'])
    def get_clientes():
        clientes = Cliente.query.all()
        return jsonify([cliente.to_json() for cliente in clientes]), 200
