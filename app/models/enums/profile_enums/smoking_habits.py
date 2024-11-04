from enum import auto
from ..base import ValueExtractableIntEnum


class SmokingHabits(ValueExtractableIntEnum):
    NON_SMOKER = auto()
    OCCASIONAL_SMOKER = auto()
    REGULAR_SMOKER = auto()
    TRYING_TO_QUIT = auto()
    PREFER_NOT_TO_SAY = auto()
