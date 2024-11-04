import requests
from fastapi import APIRouter, HTTPException, status, Depends

from app.auth.injections import get_current_user
from app.models.consents import UserConsentRequests
from app.services.fiu import get_headers, create_consent_body, AA_API_BASE_URL

router = APIRouter()


@router.post("/create-aa-redirect")
async def create_aa_redirect(current_user: dict = Depends(get_current_user)):
    """
    Create an AA redirection URL and save the consent request.
    """
    mobile = current_user.mobile
    if not mobile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mobile number not found in user data",
        )

    url = f"{AA_API_BASE_URL}/v2/consents/request"
    headers = get_headers()
    try:
        consent_body = create_consent_body(mobile)
        print("requesting consent ")
        response = requests.post(url, headers=headers, json=consent_body)
        print("consent request response: ", response.status_code)
        response.raise_for_status()
        fiu_response = response.json()

        # Save the consent request
        consent_handle = fiu_response["consents"][0]["handle"]
        UserConsentRequests.create(user=current_user, consent_handle=consent_handle)

        return {"redirect_url": fiu_response["redirect_url"]}
    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating AA redirect: {str(e)}",
        )


@router.post("/fetch-consent-status")
async def fetch_consent_status(current_user: dict = Depends(get_current_user)):
    """
    Fetch the status of the latest consent request for the current user.
    """

    # Get the latest consent request for the user
    latest_consent_request = (
        UserConsentRequests.select()
        .where(UserConsentRequests.user == current_user)
        .order_by(UserConsentRequests.created_at.desc())
        .first()
    )

    if not latest_consent_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No consent requests found for this user",
        )

    url = f"{AA_API_BASE_URL}/v2/consents/fetch"
    headers = get_headers()
    headers["x-simulate-res"] = "Ok"

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"handle": str(latest_consent_request.consent_handle)},
        )
        response.raise_for_status()
        fiu_response = response.json()

        if "consents" in fiu_response and len(fiu_response["consents"]) > 0:
            consent_status = fiu_response["consents"][0]["status"]

            return {"status": consent_status}

    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching data from FIU: {str(e)}",
        )
