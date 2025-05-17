from merlot.config.database import db
from sqlalchemy import Enum, Gender, MedicState, ExamState, VisitState
import datetime

class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(20))
    dt_birth = db.Column(db.String(20))
    gender = db.Column(db.Enum(Gender, name='gender_enum'))


class Medic(db.Model):
    __tablename__ = 'medic'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(20))
    dt_birth = db.Column(db.String(20))
    gender = db.Column(db.Enum('male', 'female', name='gender_enum'))
    m_state = db.Column(db.Enum(MedicState, name='medic_state_enum'))


class Exams(db.Model):
    __tablename__ = 'exams'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    e_state = db.Column(db.Enum(ExamState, name='exam_state_enum'))
    medic_id = db.Column(db.Integer, db.ForeignKey('medic.id'))
    dt_mrk = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    patient = db.relationship('Patient', backref='exams')
    medic = db.relationship('Medic', backref='exams')


class MedicalVisit(db.Model):
    __tablename__ = 'medical_visit'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    m_state = db.Column(db.Enum(VisitState, name='visit_state_enum'))
    medic_id = db.Column(db.Integer, db.ForeignKey('medic.id'))
    dt_mrk = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    patient = db.relationship('Patient', backref='visits')
    medic = db.relationship('Medic', backref='visits')
