import os
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv


load_dotenv()
AA_API_BASE_URL = os.environ["AA_API_BASE_URL"]


def aa_request_headers():
    return {
        "Content-Type": "application/json",
        "x-client-id": os.environ["CLIENT_ID"],
        "x-client-secret": os.environ["CLIENT_SECRET"],
    }


def z_string_utc_time(utc_datetime: datetime) -> str:
    return utc_datetime.isoformat().replace("+00:00", "Z")


def current_time_iso_string() -> str:
    return z_string_utc_time(datetime.now(timezone.utc))


def one_year_ago_iso_string() -> str:
    return z_string_utc_time(datetime.now(timezone.utc) - timedelta(days=365))


def one_year_after_iso_string() -> str:
    return z_string_utc_time(datetime.now(timezone.utc) + timedelta(days=365))
