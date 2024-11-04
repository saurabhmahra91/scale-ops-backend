from enum import auto
from ..base import ValueExtractableIntEnum


class EducationLevels(ValueExtractableIntEnum):
    PRIMARY_EDUCATION = auto()
    SECONDARY_EDUCATION = auto()
    HIGH_SCHOOL_HIGHER_SECONDARY = auto()
    DIPLOMA = auto()
    BACHELORS_DEGREE = auto()
    MASTERS_DEGREE = auto()
    DOCTORATE_PHD = auto()
    POST_DOCTORAL = auto()
    PROFESSIONAL_CERTIFICATION = auto()
    VOCATIONAL_TRAINING = auto()
    SOME_COLLEGE_NO_DEGREE = auto()
    ASSOCIATE_DEGREE = auto()
    OTHER = auto()
    PREFER_NOT_TO_SAY = auto()
