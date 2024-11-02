import base64
from datetime import datetime, timedelta, timezone
import curlify
import requests
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


AA_API_BASE_URL = "http://localhost:8080"
FIU_ENTITY_ID = "ScaleOps_FIU"
AA_ENTITY_ID = "saafe-sandbox"
FIU_REGISTRATION_APP_ID = "ai_4XXVPB5FA9Y47XhjZBEEfiF4hXFqFquK"
FIU_REGISTRATION_APP_SECRET = "as_ftqdDk9EKR6rdSNV4XTpSPuaZpqPPkbu"

CONSENT_DURATION_DAYS = 730  # 2 years
FI_DATA_RANGE_PAST_DAYS = 365 * 3  # 3 years
FI_DATA_RANGE_FUTURE_DAYS = 365  # 1 year


router = APIRouter()


def get_basic_auth_token(username: str, password: str) -> str:
    """
    Convert username and password to Basic Auth format.
    """
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded_credentials}"


class ConsentRequest(BaseModel):
    mobile: str
    callback_url: str


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


def create_consent_body(mobile: str, callback_url: str):
    """
    Create the consent request body.
    """
    consent_start, consent_expiry = get_consent_dates()
    fi_from, fi_to = get_fi_data_range()

    return {
        "redirect_params": {"callback_url": callback_url},
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


@router.post("/create-aa-redirect")
async def create_aa_redirect(request: ConsentRequest):
    """
    Create an AA redirection URL.
    """

    url = f"{AA_API_BASE_URL}/v2/consents/request"
    headers = get_headers()
    try:
        print(create_consent_body(request.mobile, request.callback_url))
        response = requests.post(url, headers=headers, json=create_consent_body(request.mobile, request.callback_url))
        response.raise_for_status()
        fiu_response = response.json()
        return {"redirect_url": fiu_response["redirect_url"], "consent_handle": fiu_response["consents"][0]["handle"]}
    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error creating AA redirect: {str(e)}"
        )


class ConsentFetchRequest(BaseModel):
    handle: str


@router.post("/notify-consent-accepted")
async def notify_consent_accepted(request: ConsentFetchRequest):
    """
    Fetch data from FIU after consent has been accepted.
    """

    url = f"{AA_API_BASE_URL}/v2/consents/fetch"
    headers = get_headers()
    headers["x-simulate-res"] = "Ok"

    try:
        response = requests.post(url, headers=headers, json={"handle": request.handle})
        response.raise_for_status()
        fiu_response = response.json()

        print(curlify.to_curl(response.request))

        return fiu_response
    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error fetching data from FIU: {str(e)}"
        )
