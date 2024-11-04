from enum import Enum

class FinancialParameterStorageType(str, Enum):
    ENUM = "ENUM"
    BOOL = "BOOL"
    DECIMAL = "DECIMAL"

    def __str__(self):
        return self.value