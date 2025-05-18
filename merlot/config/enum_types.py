from enum import Enum

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

class MedicState(Enum):
    WORKING = 'working'
    VACANCY = 'vacancy'

class ExamState(Enum):
    INIT = 'init'
    DONE = 'done'

class VisitState(Enum):
    MAKED = 'maked'
    CANCELED = 'canceled'