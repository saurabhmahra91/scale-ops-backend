from enum import auto
from .base import ValueExtractableIntEnum


class DrinkingHabits(ValueExtractableIntEnum):
    NON_DRINKER = auto()
    OCCASIONAL_DRINKER = auto()
    SOCIAL_DRINKER = auto()
    REGULAR_DRINKER = auto()
    TRYING_TO_QUIT = auto()
    PREFER_NOT_TO_SAY = auto()
