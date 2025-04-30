from flask import Flask, jsonify, request
from models import db, Message
from datetime import datetime, timedelta
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = 'chave_secreta' # depois trocar

db.init_app(app)


with app.app_context():
    db.create_all()



 # Função que protege rotas com JWT ----------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Token deve vir no cabeçalho Authorization: Bearer <token>
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'error': 'Token ausente'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']  # pode ser nome de usuário, ID, etc.
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorated

#----------------
#rotas para pegar mensagens

@app.route('/messages', methods=['GET'])
@token_required
def get_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages])

#Rota para criar mensagens----------------------------------------

@app.route('/messages', methods=['POST'])
@token_required
def create_message():
    data = request.get_json()

    required_fields = ['user_name', 'message', 'state']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400

    try:
        dt = datetime.fromisoformat(data['dateTime']) if 'dateTime' in data else datetime.utcnow()
    except ValueError:
        return jsonify({'error': 'Formato de dateTime inválido. Use ISO 8601.'}), 400

    new_msg = Message(
        user_name=data['user_name'],
        message=data['message'],
        dateTime=dt,
        state=data['state']
    )
    db.session.add(new_msg)
    db.session.commit()

    return jsonify(new_msg.to_dict()), 201

# Rota de login que gera um token
@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'error': 'Usuário ou senha ausente'}), 400

    # Aqui é um exemplo fixo, mas você pode usar um banco de usuários
    if auth['username'] == 'admin' and auth['password'] == '123':
        token = jwt.encode({
            'user': auth['username'],
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'error': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    app.run(debug=True)