# src/core/config.py
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class HubspotApiPrefix(BaseModel):
    campaigns: str = "https://api.hubapi.com/email/public/v1/campaigns/by-id"
    campaign: str = "https://api.hubapi.com/email/public/v1/campaigns/{campaign_id}"
    events: str = "https://api.hubapi.com/email/public/v1/events"


class HubSpotAPISettings(BaseModel):
    base_url: str = "https://api.hubapi.com"
    prefix: HubspotApiPrefix = HubspotApiPrefix()
    # ...


class Settings(BaseSettings):
    # ... other settings
    hubspot_api: HubSpotAPISettings = HubSpotAPISettings()


settings = Settings()
