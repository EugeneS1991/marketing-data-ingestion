from src.adapters.facebook.collections.config import (
    DEFAULT_PARAMS,
    INSIGHTS_FIELDS,
)
from src.adapters.facebook.collections.insights.schemas import Insights
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adreportrun import AdReportRun

import asyncio
from src.log_config import logger

async def get_insights(
    ad_account: AdAccount,
    sync_from: str,
    sync_to: str,
) -> list[dict]:
    params = {
        **DEFAULT_PARAMS,
        "limit": 250,
        "time_range": {"since": sync_from, "until": sync_to},
    }
    report_run: AdReportRun = ad_account.get_insights(
        fields=INSIGHTS_FIELDS, params=params, is_async=True
    )
    while True:
        status = report_run.api_get()
        if (
            status[AdReportRun.Field.async_status] == "Job Completed"
            and status[AdReportRun.Field.async_percent_completion] >= 100
        ):
            break
        logger.info(
            "[Facebook] Report status=%s, %s%%",
            status[AdReportRun.Field.async_status],
            status[AdReportRun.Field.async_percent_completion],
        )
        await asyncio.sleep(1)
    rows = list(report_run.get_result())
    return [Insights(**r).model_dump() for r in rows]
