from enum import auto
from ..base import ValueExtractableIntEnum


class Genders(ValueExtractableIntEnum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()
    PREFER_NOT_TO_SAY = auto()
