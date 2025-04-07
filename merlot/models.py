from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    dateTime = db.Column(db.DateTime, default=datetime.utcnow)
    state = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "message": self.message,
            "dateTime": self.dateTime.isoformat(),
            "state": self.state
        }