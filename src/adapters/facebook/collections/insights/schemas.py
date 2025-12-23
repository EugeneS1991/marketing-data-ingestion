from pydantic import BaseModel, ConfigDict, Field
from src.utils import utc_timestamp_micros


class Insights(BaseModel):
    """Account Models Schema"""

    model_config = ConfigDict(from_attributes=True, allow_extra=True)
    date: str | None = Field(None, alias="date_start")
    date_stop: str | None = Field(None, alias="date_stop")
    # account
    account_id: int | None = Field(None, alias="account_id")
    account_name: str | None = Field(None, alias="account_name")
    account_currency: str | None = Field(None, alias="account_currency")
    # campaign
    campaign_id: int | None = Field(None, alias="campaign_id")
    campaign_name: str | None = Field(None, alias="campaign_name")
    buying_type: str | None = Field(None, alias="buying_type")
    objective: str | None = Field(None, alias="objective")
    # adset
    adset_id: int | None = Field(None, alias="adset_id")
    adset_name: str | None = Field(None, alias="adset_name")
    # ad
    ad_id: int | None = Field(None, alias="ad_id")
    ad_name: str | None = Field(None, alias="ad_name")
    created_time: str | None = Field(None, alias="created_time")
    # metrics
    clicks: int | None = Field(None, alias="clicks")
    impressions: int | None = Field(None, alias="impressions")
    reach: int | None = Field(None, alias="reach")
    spend: float | None = Field(None, alias="spend")
    actions: list[dict] | None = Field(None, alias="actions")
    conversions: list[dict] | None = Field(None, alias="conversions")
    inline_link_clicks: int | None = Field(None, alias="inline_link_clicks")
    inline_link_click_ctr: float | None = Field(None, alias="inline_link_click_ctr")
    inline_post_engagement: int | None = Field(None, alias="inline_post_engagement")
    social_spend: str | None = Field(None, alias="social_spend")
    unique_clicks: int | None = Field(None, alias="unique_clicks")
    unique_ctr: float | None = Field(None, alias="unique_ctr")
    unique_inline_link_clicks: int | None = Field(
        None, alias="unique_inline_link_clicks"
    )
    unique_inline_link_click_ctr: float | None = Field(
        None, alias="unique_inline_link_click_ctr"
    )
    unique_link_clicks_ctr: float | None = Field(None, alias="unique_link_clicks_ctr")
    # actions
    quality_ranking: str | None = Field(None, alias="quality_ranking")
    engagement_rate_ranking: str | None = Field(None, alias="engagement_rate_ranking")
    conversion_rate_ranking: str | None = Field(None, alias="conversion_rate_ranking")
    video_thruplay_watched_actions: list[dict] | None = Field(
        None, alias="video_thruplay_watched_actions"
    )
    synced_at_micros_: int = Field(default_factory=lambda:utc_timestamp_micros())
