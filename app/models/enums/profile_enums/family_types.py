from enum import auto
from ..base import ValueExtractableIntEnum


class FamilyType(ValueExtractableIntEnum):
    NUCLEAR_FAMILY = auto()
    JOINT_FAMILY = auto()
    SINGLE_PARENT_FAMILY = auto()
    EXTENDED_FAMILY = auto()
    BLENDED_FAMILY = auto()
    CHILDLESS_FAMILY = auto()
    GRANDPARENT_FAMILY = auto()
    FOSTER_FAMILY = auto()
    ADOPTIVE_FAMILY = auto()
    LIVING_ALONE = auto()
    OTHER = auto()
    PREFER_NOT_TO_SAY = auto()
