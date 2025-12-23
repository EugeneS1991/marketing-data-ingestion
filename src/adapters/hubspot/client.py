from datetime import date

from src.schemas import HubSpotSyncRequest

from src.adapters.hubspot.collections.email_event.services import email_event
from src.storage.bigquery.schemas.hubspot.email_event.schemas import email_event as schema_email_event
from src.adapters.hubspot.collections.email_campaign.services import email_campaign
from src.storage.bigquery.schemas.hubspot.email_campaign.schemas import email_campaign as schema_email_campaign
from src.storage.bigquery.table_client import insert_rows_json_bq
from src.utils import daterange_timestamps


def handle_hubspot_sync(sync_request: HubSpotSyncRequest):
    total_rows = 0

    if sync_request.collection == "email_event":
        for ts_from, ts_to in daterange_timestamps(sync_request.sync_from, sync_request.sync_to):
            rows_to_insert = email_event(sync_request.access_token, ts_from, ts_to)
            if rows_to_insert:
                insert_rows_json_bq(sync_request=sync_request, schema=schema_email_event, data=rows_to_insert)
                total_rows += len(rows_to_insert)
                
    elif sync_request.collection == "email_campaign":
        # Campaign collection does not support date filtering within the API call (all are fetched)
        rows_to_insert = email_campaign(sync_request.access_token)
        if rows_to_insert:
            insert_rows_json_bq(sync_request=sync_request, schema=schema_email_campaign, data=rows_to_insert)
            total_rows = len(rows_to_insert)
    
    else:
        return {"error": f"Unsupported collection: {sync_request.collection}"}, 400

    return {"status": "success", "rows_loaded": total_rows}, 200
