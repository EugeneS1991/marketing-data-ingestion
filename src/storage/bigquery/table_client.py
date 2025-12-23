from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from src.log_config import logger


def _create_table(client: bigquery.Client, table_path: str, schema) -> str:   
    logger.info(f"Creating table: {table_path}")
    try:
        client.get_table(table_path)
    except NotFound:
        table = bigquery.Table(table_path, schema=schema.schema)

        table.clustering_fields = schema.clustering_field
        table.time_partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY,
                field=schema.partitioning_field,
                expiration_ms=None,
            )

        created_table = client.create_table(table)
        logger.info(
            f"Table created: {created_table.project}.{created_table.dataset_id}.{created_table.table_id}"
        )
    return 'ok'


def insert_rows_json_bq (sync_request, schema, data):
    client = bigquery.Client(project=sync_request.project_id)
    table_path = f"{sync_request.project_id}.{sync_request.dataset_id}.{sync_request.table_id}"

    if _create_table(client, table_path, schema) == 'ok':
        table = client.get_table(table_path)
        client.insert_rows_json(json_rows=data, table=table)
        logger.info("Success uploaded to table {}".format(table.table_id))


