from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

from datetime import datetime
from src.utils import utc_timestamp_micros


class EmailCampaignList(BaseModel):
    id: Optional[int] = None
    appId: Optional[int] = None
    appName: Optional[str] = None


class EmailCampaignListResponse(BaseModel):
    has_more: Optional[bool] = Field(alias="hasMore")
    offset: Optional[str]
    campaigns: List[EmailCampaignList]


class EmailCampaignCounters(BaseModel):
    processed: Optional[int] = None
    deferred: Optional[int] = None
    unsubscribed: Optional[int] = None
    statuschange: Optional[int] = None
    bounce: Optional[int] = None
    dropped: Optional[int] = None
    delivered: Optional[int] = None
    suppressed: Optional[int] = None
    sent: Optional[int] = None
    click: Optional[int] = None
    open: Optional[int] = None


class EmailCampaign(BaseModel):
    date: str = Field(default_factory=lambda: str(datetime.utcnow().date()))
    id: Optional[int] = None
    app_id: Optional[int] = Field(None, alias="appId")
    app_name: Optional[str] = Field(None, alias="appName")
    content_id: Optional[int] = Field(None, alias="contentId")
    subject: Optional[str] = None
    name: Optional[str] = None
    counters: Optional[EmailCampaignCounters] = None
    type: Optional[str] = None
    synced_at_micros_: int = Field(default_factory=utc_timestamp_micros)
