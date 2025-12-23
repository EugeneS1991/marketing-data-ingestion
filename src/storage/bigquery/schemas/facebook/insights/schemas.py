from google.cloud import bigquery


class Insights:
    schema = [
        bigquery.SchemaField("date", "DATE", "NULLABLE"),
        bigquery.SchemaField("date_stop", "DATE", "NULLABLE"),
        bigquery.SchemaField("account_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("account_name", "STRING", "NULLABLE"),
        bigquery.SchemaField("account_currency", "STRING", "NULLABLE"),
        bigquery.SchemaField("campaign_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("campaign_name", "STRING", "NULLABLE"),
        bigquery.SchemaField("buying_type", "STRING", "NULLABLE"),
        bigquery.SchemaField("objective", "STRING", "NULLABLE"),
        bigquery.SchemaField("adset_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("adset_name", "STRING", "NULLABLE"),
        bigquery.SchemaField("ad_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("ad_name", "STRING", "NULLABLE"),
        bigquery.SchemaField("created_time", "DATE", "NULLABLE"),
        bigquery.SchemaField("clicks", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("impressions", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("reach", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("spend", "FLOAT", "NULLABLE"),
        bigquery.SchemaField(
            "actions",
            "RECORD",
            "REPEATED",
            fields=[
                bigquery.SchemaField("action_type", "STRING", "NULLABLE"),
                bigquery.SchemaField("value", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField(
            "conversions",
            "RECORD",
            "REPEATED",
            fields=[
                bigquery.SchemaField("action_type", "STRING", "NULLABLE"),
                bigquery.SchemaField("value", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("inline_link_clicks", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("inline_link_click_ctr", "FLOAT", "NULLABLE"),
        bigquery.SchemaField("inline_post_engagement", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("social_spend", "STRING", "NULLABLE"),
        bigquery.SchemaField("unique_clicks", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("unique_ctr", "FLOAT", "NULLABLE"),
        bigquery.SchemaField("unique_inline_link_clicks", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("unique_inline_link_click_ctr", "FLOAT", "NULLABLE"),
        bigquery.SchemaField("unique_link_clicks_ctr", "FLOAT", "NULLABLE"),
        bigquery.SchemaField("quality_ranking", "STRING", "NULLABLE"),
        bigquery.SchemaField("engagement_rate_ranking", "STRING", "NULLABLE"),
        bigquery.SchemaField("conversion_rate_ranking", "STRING", "NULLABLE"),
        bigquery.SchemaField(
            "video_thruplay_watched_actions",
            "RECORD",
            "REPEATED",
            fields=[
                bigquery.SchemaField("action_type", "STRING", "NULLABLE"),
                bigquery.SchemaField("value", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("synced_at_micros_", "INTEGER", "NULLABLE")
    ]

    partitioning_field = "date"
    clustering_field = ["account_id", "adset_id", "ad_id", "campaign_id"]


insights = Insights()
