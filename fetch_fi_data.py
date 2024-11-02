import requests
from common import aa_request_headers, AA_API_BASE_URL


def fetch_data_url(session_id: str):
    return f"{AA_API_BASE_URL}/sessions/{session_id}"


def fetch_fi_data(session_id):
    print("requesting fi data")
    response = requests.get(url=fetch_data_url(session_id), headers=aa_request_headers())
    print(response)
    print(response.json())
