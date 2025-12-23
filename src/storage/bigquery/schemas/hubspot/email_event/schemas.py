from google.cloud import bigquery


class EmailEvent:
    schema = [
        bigquery.SchemaField("date", "DATE", "NULLABLE"),
        bigquery.SchemaField("app_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("app_name", "STRING", "NULLABLE"),
        bigquery.SchemaField(
            "location",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("country", "STRING", "NULLABLE"),
                bigquery.SchemaField("state", "STRING", "NULLABLE"),
                bigquery.SchemaField("city", "STRING", "NULLABLE"),
                bigquery.SchemaField("zipcode", "STRING", "NULLABLE"),
                bigquery.SchemaField("latitude", "FLOAT", "NULLABLE"),
                bigquery.SchemaField("longitude", "FLOAT", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("id", "STRING", "NULLABLE"),
        bigquery.SchemaField("duration", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("created", "INTEGER", "NULLABLE"),
        bigquery.SchemaField(
            "browser",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("name", "STRING", "NULLABLE"),
                bigquery.SchemaField("family", "STRING", "NULLABLE"),
                bigquery.SchemaField("producer", "STRING", "NULLABLE"),
                bigquery.SchemaField("producer_url", "STRING", "NULLABLE"),
                bigquery.SchemaField("type", "STRING", "NULLABLE"),
                bigquery.SchemaField("url", "STRING", "NULLABLE"),
                bigquery.SchemaField("version", "STRING", "REPEATED"),
            ],
        ),
        bigquery.SchemaField("suppressed_message", "STRING", "NULLABLE"),
        bigquery.SchemaField("suppressed_reason", "STRING", "NULLABLE"),
        bigquery.SchemaField("device_type", "STRING", "NULLABLE"),
        bigquery.SchemaField("user_agent", "STRING", "NULLABLE"),
        bigquery.SchemaField("type", "STRING", "NULLABLE"),
        bigquery.SchemaField("portal_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField(
            "sent_by",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("id", "STRING", "NULLABLE"),
                bigquery.SchemaField("created", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("smtp_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("recipient", "STRING", "NULLABLE"),
        bigquery.SchemaField("filtered_event", "BOOLEAN", "NULLABLE"),
        bigquery.SchemaField("email_campaign_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("email_campaign_group_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("attempt", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("response", "STRING", "NULLABLE"),
        bigquery.SchemaField("from_", "STRING", "NULLABLE"),
        bigquery.SchemaField("cc", "STRING", "REPEATED"),
        bigquery.SchemaField("bcc", "STRING", "REPEATED"),
        bigquery.SchemaField("subject", "STRING", "NULLABLE"),
        bigquery.SchemaField("referer", "STRING", "NULLABLE"),
        bigquery.SchemaField("link_id", "INTEGER", "NULLABLE"),
        bigquery.SchemaField("url", "STRING", "NULLABLE"),
        bigquery.SchemaField(
            "caused_by",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("id", "STRING", "NULLABLE"),
                bigquery.SchemaField("created", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("source", "STRING", "NULLABLE"),
        bigquery.SchemaField("source_id", "STRING", "NULLABLE"),
        bigquery.SchemaField(
            "subscriptions",
            "RECORD",
            "REPEATED",
            fields=[
                bigquery.SchemaField("id", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("status", "STRING", "NULLABLE"),
                bigquery.SchemaField(
                    "legal_basis_change",
                    "RECORD",
                    "NULLABLE",
                    fields=[
                        bigquery.SchemaField("legal_basis_type", "STRING", "NULLABLE"),
                        bigquery.SchemaField(
                            "legal_basis_explanation", "STRING", "NULLABLE"
                        ),
                        bigquery.SchemaField("opt_state", "STRING", "NULLABLE"),
                    ],
                ),
            ],
        ),
        bigquery.SchemaField("portal_subscription_status", "STRING", "NULLABLE"),
        bigquery.SchemaField("drop_message", "STRING", "NULLABLE"),
        bigquery.SchemaField("drop_reason", "STRING", "NULLABLE"),
        bigquery.SchemaField("category", "STRING", "NULLABLE"),
        bigquery.SchemaField("status", "STRING", "NULLABLE"),
        bigquery.SchemaField("requested_by", "STRING", "NULLABLE"),
        bigquery.SchemaField("bounced", "BOOLEAN", "NULLABLE"),
        bigquery.SchemaField(
            "obsoleted_by",
            "RECORD",
            "NULLABLE",
            fields=[
                bigquery.SchemaField("id", "STRING", "NULLABLE"),
                bigquery.SchemaField("created", "INTEGER", "NULLABLE"),
            ],
        ),
        bigquery.SchemaField("synced_at_micros_", "INTEGER", "NULLABLE")
    ]
    partitioning_field = "date"
    clustering_field = ["email_campaign_id"]


email_event = EmailEvent()
