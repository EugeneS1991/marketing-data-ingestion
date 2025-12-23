from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

from datetime import datetime
from src.utils import utc_timestamp_micros


class Location(BaseModel):
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class Browser(BaseModel):
    name: Optional[str] = None
    family: Optional[str] = None
    producer: Optional[str] = None
    producer_url: Optional[str] = Field(None, alias="producerUrl")
    type: Optional[str] = None
    url: Optional[str] = None
    version: Optional[List[str]] = None


class SentBy(BaseModel):
    id: Optional[str] = None
    created: Optional[int] = None


class CausedBy(BaseModel):
    id: Optional[str] = None
    created: Optional[int] = None


class LegalBasisChange(BaseModel):
    legal_basis_type: Optional[str] = Field(None, alias="legalBasisType")
    legal_basis_explanation: Optional[str] = Field(None, alias="legalBasisExplanation")
    opt_state: Optional[str] = Field(None, alias="optState")


class Subscription(BaseModel):
    id: Optional[int] = None
    status: Optional[str] = None
    legal_basis_change: Optional[LegalBasisChange] = Field(
        None, alias="legalBasisChange"
    )


class ObsoletedBy(BaseModel):
    id: Optional[str] = None
    created: Optional[int] = None


class EmailEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    date: Optional[str] = None
    app_id: Optional[int] = Field(None, alias="appId")
    app_name: Optional[str] = Field(None, alias="appName")
    location: Optional[Location] = None
    id: Optional[str] = None
    duration: Optional[int] = None
    created: Optional[int] = None
    browser: Optional[Browser] = None
    suppressed_message: Optional[str] = Field(None, alias="suppressedMessage")
    suppressed_reason: Optional[str] = Field(None, alias="suppressedReason")
    device_type: Optional[str] = Field(None, alias="deviceType")
    user_agent: Optional[str] = Field(None, alias="userAgent")
    type: Optional[str] = None
    portal_id: Optional[int] = Field(None, alias="portalId")
    sent_by: Optional[SentBy] = Field(None, alias="sentBy")
    smtp_id: Optional[int] = Field(None, alias="smtpId")
    recipient: Optional[str] = None
    filtered_event: Optional[bool] = Field(None, alias="filteredEvent")
    email_campaign_id: Optional[int] = Field(None, alias="emailCampaignId")
    email_campaign_group_id: Optional[int] = Field(None, alias="emailCampaignGroupId")
    attempt: Optional[int] = None
    response: Optional[str] = None
    from_: Optional[str] = Field(None, alias="from")
    cc: Optional[List[str]] = Field(default_factory=list)
    bcc: Optional[List[str]] = Field(default_factory=list)
    subject: Optional[str] = None
    referer: Optional[str] = None
    link_id: Optional[int] = Field(None, alias="linkId")
    url: Optional[str] = None
    caused_by: Optional[CausedBy] = Field(None, alias="causedBy")
    source: Optional[str] = None
    source_id: Optional[str] = Field(None, alias="sourceId")
    subscriptions: Optional[List[Subscription]] = None
    portal_subscription_status: Optional[str] = Field(
        None, alias="portalSubscriptionStatus"
    )
    drop_message: Optional[str] = Field(None, alias="dropMessage")
    drop_reason: Optional[str] = Field(None, alias="dropReason")
    category: Optional[str] = None
    status: Optional[str] = None
    requested_by: Optional[str] = Field(None, alias="requestedBy")
    bounced: Optional[bool] = None
    obsoleted_by: Optional[ObsoletedBy] = Field(None, alias="obsoletedBy")

    synced_at_micros_: int = Field(default_factory=lambda:utc_timestamp_micros())

    def model_post_init(self, __context):
        if self.created and not self.date:
            self.date = datetime.utcfromtimestamp(self.created / 1000).strftime(
                "%Y-%m-%d"
            )


class EmailEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    has_more: Optional[bool] = Field(alias="hasMore")
    offset: Optional[str]
    events: List[EmailEvent]
