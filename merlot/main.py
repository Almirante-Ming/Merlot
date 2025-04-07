from flask import Flask, jsonify, request
from models import db, Message
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages])

@app.route('/messages', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)