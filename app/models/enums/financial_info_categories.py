from enum import auto
from app.models.enums.base import ValueExtractableIntEnum

class FinancialInfoCategory(ValueExtractableIntEnum):
    INCOME_PATTERNS = auto()
    EXPENDITURE_HABITS = auto()
    SAVINGS_BEHAVIOR = auto()
    INVESTMENT_ACTIVITIES = auto()
    DEBT_OBLIGATIONS = auto()
    FINANCIAL_DISCIPLINE = auto()
    FINANCIAL_SUPPORT_OBLIGATIONS = auto()
    PHILANTHROPY = auto()
    LIFESTYLE_INDICATORS = auto()
    RISK_MANAGEMENT_AND_INSURANCE = auto()
    FINANCIAL_GOALS_AND_FUTURE_PLANNING = auto()
    HEALTHCARE_SPENDING = auto()
    FAMILY_STRUCTURE = auto()