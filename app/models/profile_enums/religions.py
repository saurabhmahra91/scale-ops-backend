from enum import auto
from .base import ValueExtractableIntEnum


class Religions(ValueExtractableIntEnum):
    BUDDHISM = auto()
    CHRISTIANITY = auto()
    HINDUISM = auto()
    ISLAM = auto()
    JUDAISM = auto()
    SIKHISM = auto()
    OTHER_RELIGION = auto()
    NO_RELIGION = auto()
    PREFER_NOT_TO_SAY = auto()
