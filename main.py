import os

import requests
from fastapi import FastAPI
from fetch_fi_data import fetch_fi_data
from request_fi_data import request_fi_data

from common import (
    AA_API_BASE_URL,
    aa_request_headers,
    current_time_iso_string,
    one_year_after_iso_string,
    one_year_ago_iso_string,
)

app = FastAPI()


def get_customer_id_by_mobile(mobile: str):
    return f"{mobile}@onemoney"


def data_consumer_id():
    return "setu-fiu-id"


def redirect_url():
    return os.environ["REDIRECT_URL"]


def create_consent_request_body(mobile: str):
    return {
        "Detail": {
            "consentStart": current_time_iso_string(),
            "consentEnd": one_year_after_iso_string(),
            "Customer": {
                "id": get_customer_id_by_mobile(mobile),
            },
            "FIDataRange": {
                "from": one_year_ago_iso_string(),
                "to": current_time_iso_string(),
            },
            "consentMode": "STORE",
            "consentTypes": ["TRANSACTIONS", "PROFILE", "SUMMMARY"],
            "fetchType": "PERIODIC",
            "Frequency": {"value": 30, "unit": "MONTH"},
            "DataFilter": [{"type": "TRANSACTIONAMOUNT", "value": "0"}],
            "DataLife": {"value": 1, "unit": "DAYS"},
            "DataConsumer": {
                "id": data_consumer_id(),
            },
            "Purpose": {
                "Category": {
                    "type": "DEFAULT",
                },
                "code": "101",
                "text": "Analysis for best health insurance prediction",
                "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
            },
            "fiTypes": ["DEPOSI"],
            "redirectUrl": redirect_url(),
        }
    }


def consent_submit_url():
    return f"{AA_API_BASE_URL}/consents"


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.get("/sessions/{mobile}")
def create_consent_call_to_aa_for_mobile_number(mobile: str):
    request_body = create_consent_request_body(mobile)
    response = requests.post(url=consent_submit_url(), json=request_body, headers=aa_request_headers())
    return {"aa_url": response.json()["url"]}


@app.post("/notification")
def receive_notification(notification: dict):
    print("Received notification:", notification)

    if notification["type"] == "CONSENT_STATUS_UPDATE":
        if notification["data"]["status"] == "ACTIVE":
            print("consent active")
            request_fi_data(consent_id=notification["consentId"])
        else:
            print("Consent rejected")

    if notification["type"] == "SESSION_STATUS_UPDATE":
        if notification["data"]["status"] == "COMPLETED":
            print("consent completed")
            fetch_fi_data(session_id=notification["dataSessionId"])
        else:
            print("Consent pending")


@app.post("/events/v2")
def event_listening(event: dict):
    print(event)
    return {"message": "Event received"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
