import os
import base64
from datetime import datetime, timedelta, timezone


AA_API_BASE_URL = "http://localhost:8080"
AA_CALLBACK_URL = "http://localhost:5000/fiu/consent-notification"
FIU_ENTITY_ID = "ScaleOps_FIU"
AA_ENTITY_ID = "saafe-sandbox"
FIU_REGISTRATION_APP_ID = os.environ["FIU_REGISTRATION_APP_ID"]
FIU_REGISTRATION_APP_SECRET = os.environ["FIU_REGISTRATION_APP_SECRET"]

CONSENT_DURATION_DAYS = 730  # 2 years
FI_DATA_RANGE_PAST_DAYS = 365 * 3  # 3 years
FI_DATA_RANGE_FUTURE_DAYS = 365  # 1 year


def get_basic_auth_token(username: str, password: str) -> str:
    """
    Convert username and password to Basic Auth format.
    """
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded_credentials}"


def get_headers():
    """
    Generate headers for the AA API request.
    """
    return {
        "fiu_entity_id": FIU_ENTITY_ID,
        "aa_entity_id": AA_ENTITY_ID,
        "Content-Type": "application/json",
        "Authorization": get_basic_auth_token(FIU_REGISTRATION_APP_ID, FIU_REGISTRATION_APP_SECRET),
    }


def datetime_to_iso_string(dt: datetime) -> str:
    """
    Convert a datetime object to an ISO 8601 string with millisecond precision and 'Z' suffix.

    Args:
        dt (datetime): The datetime object to convert.

    Returns:
        str: The ISO 8601 formatted string with millisecond precision and 'Z' suffix.
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def get_consent_dates():
    """
    Generate consent start and expiry dates.
    """
    now = datetime.now(tz=timezone.utc)
    consent_start = datetime_to_iso_string(now)
    consent_expiry = datetime_to_iso_string(now + timedelta(days=CONSENT_DURATION_DAYS))
    return consent_start, consent_expiry


def get_fi_data_range():
    """
    Generate FI data range dates.
    """
    now = datetime.now(tz=timezone.utc)
    from_date = datetime_to_iso_string((now - timedelta(FI_DATA_RANGE_PAST_DAYS)))
    to_date = datetime_to_iso_string(now - timedelta(FI_DATA_RANGE_FUTURE_DAYS))
    return from_date, to_date


def create_consent_body(mobile: str):
    """
    Create the consent request body.
    """
    consent_start, consent_expiry = get_consent_dates()
    fi_from, fi_to = get_fi_data_range()

    return {
        "redirect_params": {"callback_url": AA_CALLBACK_URL},
        "consents": [
            {
                "consent_start": consent_start,
                "consent_expiry": consent_expiry,
                "consent_mode": "STORE",
                "fetch_type": "PERIODIC",
                "consent_types": ["PROFILE", "SUMMARY", "TRANSACTIONS"],
                "fi_types": ["DEPOSIT"],
                "customer": {"identifiers": [{"type": "MOBILE", "value": mobile}]},
                "purpose": {"code": "101", "text": "Wealth management service"},
                "fi_data_range": {"from": fi_from, "to": fi_to},
                "data_life": {"unit": "MONTH", "value": 10},
                "frequency": {"unit": "MONTH", "value": 31},
            }
        ],
    }
