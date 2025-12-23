# Marketing Data Ingestion Framework

A serverless Python-based ETL framework designed to automate data extraction from marketing platforms and load it directly into Google BigQuery.

## Supported Connectors
Currently, the following integrations are available:
- **Facebook Ads**: Monthly/Daily Insights extraction (campaigns, ad sets, ads, spend, clicks, impressions, etc.).
- **HubSpot**: 
  - **Email Events**: High-volume stream of interaction data (opens, clicks, bounces).
  - **Email Campaigns**: Metadata and settings for marketing campaigns.

## Cloud Services Stack
- **Google Cloud Functions (GCF)**: Executes the Python logic (Runtime: Python 3.11).
- **Google Cloud Scheduler**: Automates the trigger of the GCF via HTTP POST requests on a specified schedule (e.g., daily at 2:00 AM).
- **Google BigQuery**: Serves as the data warehouse for all ingested marketing metrics.
- **Google Cloud Build**: Automates the deployment process.

---

## Setup & Deployment Instructions

### 1. Deploy the Cloud Function
The deployment is managed via Google Cloud Build. Ensure your GCP CLI is configured and run:

```bash
gcloud builds submit --config cloudbuild.yaml .
```

This will deploy a Cloud Function named `marketing-data-ingestion`. Once completed, the CLI or GCP Console will provide an **HTTP Trigger URL**. Take note of this URL.

### 2. Configure Cloud Scheduler
Navigate to **Cloud Scheduler** in the GCP Console and create a new job for each data collection you want to sync.

**Settings:**
- **Frequency**: e.g., `0 2 * * *` (Daily at 2 AM).
- **Target Type**: HTTP.
- **URL**: Paste the URL of your deployed Cloud Function.
- **HTTP Method**: POST.
- **Auth Header**: Select "Add OIDC token" (Use a service account with `Cloud Functions Invoker` permissions).

---

## Request Payloads (JSON Body)

Pass the following JSON in the Body of the Cloud Scheduler job to trigger specific syncs.

### HubSpot Sync Request
```json
{
  "source": "hubspot",
  "collection": "email_event",
  "access_token": "your_private_app_token",
  "project_id": "gcp-project-id",
  "dataset_id": "marketing_dataset",
  "table_id": "hubspot_raw_events",
  "sync_from": "2023-12-01",
  "sync_to": "2023-12-22"
}
```
*Fields:*
- `source`: Must be `"hubspot"`.
- `collection`: Either `"email_event"` or `"email_campaign"`.
- `access_token`: HubSpot Private App Access Token.
- `project_id`, `dataset_id`, `table_id`: BigQuery destination details.
- `sync_from` / `sync_to`: (Optional) Format `YYYY-MM-DD`. Defaults to Yesterday if omitted.

### Facebook Sync Request
```json
{
  "source": "facebook",
  "collection": "insights",
  "access_token": "your_marketing_api_token",
  "account_id": "1234567890",
  "app_id": "fb_app_id",
  "app_secret": "fb_app_secret",
  "project_id": "gcp-project-id",
  "dataset_id": "marketing_dataset",
  "table_id": "facebook_daily_insights"
}
```
*Fields:*
- `source`: Must be `"facebook"`.
- `collection`: Currently supports `"insights"`.
- `account_id`: Your Facebook Ad Account ID (without `act_` prefix).
- `app_id` & `app_secret`: Your Facebook Developer App credentials.
- `sync_from` / `sync_to`: (Optional) Daily loop iterates between these dates.

---

## Technical Features
- **Day-by-Day Iteration**: To avoid memory limits and API timeouts, large date ranges are automatically split into single-day requests.
- **Auto-Schema Management**: Automatically creates BigQuery tables with correct schemas, partitioning (by date), and clustering if they don't exist.
- **Reliable Logging**: Structured logging provides clear visibility into which date/collection is currently processing.
