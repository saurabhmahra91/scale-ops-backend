from enum import auto
from ..base import ValueExtractableIntEnum


class MaritalStatus(ValueExtractableIntEnum):
    NEVER_MARRIED = auto()
    DIVORCED = auto()
    WIDOWED = auto()
    AWAITING_DIVORCE = auto()
    MARRIED = auto()
    PREFER_NOT_TO_SAY = auto()
