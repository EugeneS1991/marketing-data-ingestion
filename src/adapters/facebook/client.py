from src.schemas import FacebookSyncRequest
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from src.adapters.facebook.collections.insights.services import get_insights
# from src.adapters.facebook.collections.account.services import get_account
from src.storage.bigquery.table_client import insert_rows_json_bq
from src.storage.bigquery.schemas.facebook.insights.schemas import insights as schema_insights
# from src.storage.bigquery.schemas.facebook.account.schemas import account as schema_account
import asyncio
from src.utils import daterange_strings

def handle_facebook_sync(sync_request: FacebookSyncRequest):
    FacebookAdsApi.init(sync_request.app_id, sync_request.app_secret, sync_request.access_token)
    account = AdAccount('act_'+str(sync_request.account_id))
    
    total_rows = 0

    if sync_request.collection == "insights":
        for day_str in daterange_strings(sync_request.sync_from, sync_request.sync_to):
            rows_to_insert = asyncio.run(get_insights(account, day_str, day_str))
            if rows_to_insert:
                insert_rows_json_bq(sync_request=sync_request, schema=schema_insights, data=rows_to_insert)
                total_rows += len(rows_to_insert)

    # elif sync_request.collection == "account":
    #     # Placeholder for Account collection (fetching without daily loop)
    #     rows_to_insert = get_account(account)
    #     if rows_to_insert:
    #         insert_rows_json_bq(sync_request=sync_request, schema=schema_account, data=rows_to_insert)
    #         total_rows = len(rows_to_insert)

    else:
        return {"error": f"Unsupported collection: {sync_request.collection}"}, 400

    return {"status": "success", "rows_loaded": total_rows}, 200