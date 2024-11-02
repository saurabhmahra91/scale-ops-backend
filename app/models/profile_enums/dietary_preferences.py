from enum import auto
from .base import ValueExtractableIntEnum


class DietaryPreferences(ValueExtractableIntEnum):
    NO_PREFERENCE = auto()
    VEGETARIAN = auto()
    VEGAN = auto()
    PESCATARIAN = auto()
    OMNIVORE = auto()
    KETO = auto()
    PALEO = auto()
    GLUTEN_FREE = auto()
    DAIRY_FREE = auto()
    HALAL = auto()
    KOSHER = auto()
    LOW_CARB = auto()
    LOW_FAT = auto()
    ORGANIC = auto()
    PREFER_NOT_TO_SAY = auto()

    @classmethod
    def get_values(cls):
        return [preference.name.replace("_", " ").title() for preference in cls]
