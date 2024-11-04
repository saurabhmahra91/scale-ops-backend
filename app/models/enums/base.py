from enum import IntEnum, StrEnum


class ValueExtractableIntEnum(IntEnum):
    @classmethod
    def get_values(cls):
        return [tag.value for tag in cls]

    @classmethod
    def from_string(cls, value):
        try:
            return cls[int(value)]
        except ValueError:
            raise ValueError(f"'{value}' is not a valid {cls.__name__}")

    def to_dict(self):
        return {"id": self.value, "name": self.name.replace("_", " ").title()}


class PeeWeeStrEnumBase(StrEnum):
    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]

    @classmethod
    def create_enum(cls, name, values):
        return StrEnum(name, {cls._to_enum_key(v): v for v in values})

    @staticmethod
    def _to_enum_key(value):
        return value.upper().replace(' ', '_').replace('-', '_')