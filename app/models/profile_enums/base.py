from enum import IntEnum


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
