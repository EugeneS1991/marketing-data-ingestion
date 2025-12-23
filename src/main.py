import functions_framework
from src.log_config import logger

from src.adapters.facebook.client import handle_facebook_sync
from src.adapters.hubspot.client import handle_hubspot_sync
from src.schemas import FacebookSyncRequest, HubSpotSyncRequest


@functions_framework.http
def main_handler(request):
    """
    Main entry point for the Cloud Function.
    Triggered by HTTP request from Cloud Scheduler.
    
    Automatically detects source (Facebook/HubSpot) based on payload fields.
    """
    request_json = request.get_json(silent=True)
    
    if not request_json:
        logger.error("No JSON payload received")
        return {"error": "No JSON payload received"}, 400

    try:
        source = request_json["source"].lower()
        logger.info(f"Detected source: {source}")
        if source == 'facebook':
            data = FacebookSyncRequest(**request_json)  
            return handle_facebook_sync(data)
        elif source == 'hubspot':
            data = HubSpotSyncRequest(**request_json)
            return handle_hubspot_sync(data)
        else:
            return {"error": f"Unsupported source: {source}"}, 400
            
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return {"error": str(e)}, 400
    except Exception as e:
        logger.exception(f"Error processing sync request")
        return {"error": f"Internal Server Error: {str(e)}"}, 500
