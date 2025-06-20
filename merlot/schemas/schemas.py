from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields # permite definir campos customizados dentro do schema
from merlot.config.database import db
from merlot.config.enum_types import Gender, MedicState, ExamState, VisitState
from models import User, Patient, Medic, Exams, MedicalVisit  # importe corretamente

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

class PatientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        load_instance = True
        include_fk = True

class MedicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Medic
        load_instance = True
        include_fk = True

class ExamsSchema(SQLAlchemyAutoSchema):
    patient = fields.Nested(PatientSchema, only=("id", "full_name", "email"))
    medic = fields.Nested(MedicSchema, only=("id", "full_name", "email"))

    class Meta:
        model = Exams
        load_instance = True
        include_fk = True

class MedicalVisitSchema(SQLAlchemyAutoSchema):
    patient = fields.Nested(PatientSchema, only=("id", "full_name", "email"))
    medic = fields.Nested(MedicSchema, only=("id", "full_name", "email"))

    class Meta:
        model = MedicalVisit
        load_instance = True
        include_fk = True
