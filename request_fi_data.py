import requests
from common import aa_request_headers, current_time_iso_string, one_year_ago_iso_string, AA_API_BASE_URL


def request_data_body_json(consent_id: str):
    return {
        "consentId": consent_id,
        "DataRange": {"from": one_year_ago_iso_string(), "to": current_time_iso_string()},
        "format": "json",
    }


def data_request_url():
    return f"{AA_API_BASE_URL}/sessions"


def request_fi_data(consent_id: str):
    request_body = request_data_body_json(consent_id)
    print("requesting fi data with consent id:", consent_id)
    response = requests.post(url=data_request_url(), headers=aa_request_headers(), json=request_body)
    print(response)
