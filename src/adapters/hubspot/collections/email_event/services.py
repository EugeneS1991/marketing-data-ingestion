import requests
from src.adapters.hubspot.collections.email_event.schemas import (
    EmailEventResponse
)
from src.adapters.hubspot.collections.config import settings


def email_event(
    access_token: str, sync_from: int, sync_to: int
) -> list[dict]:
    url = settings.hubspot_api.prefix.events
    params = {"limit": 1000, "startTimestamp": sync_from, "endTimestamp": sync_to}
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}",
    }
    out = []
    
    with requests.Session() as session:
        has_more, offset = True, None
        while has_more:
            if offset:
                params["offset"] = offset
            
            r = session.get(url, headers=headers, params=params, timeout=30)
            r.raise_for_status()
            
            body = EmailEventResponse.model_validate(r.json())
            out.extend(body.events)
            has_more, offset = body.has_more, body.offset
            
    return [e.model_dump() for e in out]
