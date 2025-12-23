from google.cloud import bigquery


class EmailCampaign:
    schema = [
        bigquery.SchemaField("date", "DATE", "NULLABLE"),
        bigquery.SchemaField("id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("app_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("app_name", "STRING", "NULLABLE"),
        bigquery.SchemaField("content_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("subject", "STRING", "NULLABLE"),
        bigquery.SchemaField("name", "STRING", "NULLABLE"),
        bigquery.SchemaField(
            "counters",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("processed", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("deferred", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("unsubscribed", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("statuschange", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("bounce", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("dropped", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("delivered", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("suppressed", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("sent", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("click", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("open", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("type", "STRING", "NULLABLE"),
        bigquery.SchemaField("synced_at_micros_", "INTEGER", "NULLABLE")
    ]
    partitioning_field = "date"
    clustering_field = ["id"]


email_campaign = EmailCampaign()
