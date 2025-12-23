import requests
from src.adapters.hubspot.collections.email_campaign.schemas import (
    EmailCampaignListResponse,
    EmailCampaignList,
    EmailCampaign,
)
from src.adapters.hubspot.collections.config import settings


def email_campaign(
    access_token: str,
    sync_from: int | None = None,
    sync_to: int | None = None,
) -> list[dict]:
    api_url = settings.hubspot_api.prefix.campaigns
    params_url = {"limit": 1000}
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}",
    }

    campaigns_list: list[EmailCampaignList] = []
    
    with requests.Session() as session:
        # 1. Fetch all campaign IDs (List Loop)
        has_more, offset = True, None
        while has_more:
            if offset:
                params_url["offset"] = offset
            
            r = session.get(url=api_url, headers=headers, params=params_url, timeout=30)
            r.raise_for_status()
            
            campaigns_response = EmailCampaignListResponse.model_validate(r.json())
            campaigns_list.extend(campaigns_response.campaigns)
            has_more, offset = campaigns_response.has_more, campaigns_response.offset

        # 2. Fetch details for each campaign (Detail Loop)
        campaigns: list[EmailCampaign] = []
        for campaign_item in campaigns_list:
            url = settings.hubspot_api.prefix.campaign.format(campaign_id=campaign_item.id)
            try:
                r = session.get(url=url, headers=headers, timeout=30)
                r.raise_for_status()
                campaign_detail = EmailCampaign.model_validate(r.json())
                campaigns.append(campaign_detail)
            except Exception as e:
                # Log error or handle it as needed, currently skipping failed fetches
                print(f"Failed to fetch campaign {campaign_item.id}: {e}")
                continue

    return [c.model_dump() for c in campaigns]
