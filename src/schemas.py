from pydantic import BaseModel, Field, model_validator
from datetime import date, timedelta




class BaseSyncRequest(BaseModel):
    access_token: str = Field(..., description="HubSpot API access token", min_length=1)
    source: str = Field(..., description="Data source (e.g., hubspot, facebook)", min_length=1)
    collection: str = Field(..., description="Data collection name (e.g., contacts, companies, deals)", min_length=1)
    project_id: str = Field(..., description="Google Cloud project ID")
    dataset_id: str = Field(..., description="BigQuery dataset ID")
    table_id: str = Field(..., description="BigQuery table ID")
    
    # Common date logic is also kept here
    sync_from: date = Field(
        default_factory=lambda: date.today() - timedelta(days=1),
        description="Start date"
    )
    sync_to: date = Field(
        default_factory=lambda: date.today() - timedelta(days=1),
        description="End date (Yesterday by default)"
    )




class HubSpotSyncRequest(BaseSyncRequest):
    """Pydantic schema for HubSpot data sync request."""
    
    pass


class FacebookSyncRequest(BaseSyncRequest):
    account_id: str = Field(..., description="Facebook account ID")
    app_id: str = Field(..., description="Facebook app ID")
    app_secret: str = Field(..., description="Facebook app secret")
    