from fastapi import Header, HTTPException, Depends
import secrets


# predefined Secret Key
SECERT_KEY = "XLTUp-Vr3F8S2qG7c-_6fsHOiy31YRuw-_zbv8UwEEc"

# Dep to validate the Authorization Header
def verify_authorization(authorization: str = Header(...)):
    if authorization != f"Bearer {SECERT_KEY}":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing Authorization header"
        )


