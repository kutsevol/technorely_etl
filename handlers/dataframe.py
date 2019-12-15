import pandas as pd

from validators.validator import validate
from utils.request import response_ndjson_iteration


def create_dataframe_by_ndjson_url(url, schema):
    """
    Create dataframe by ndjson url.
    :param url: path to ndjson
    :param schema: json schema
    :return: DataFrame
    """
    return pd.DataFrame(
        raw_json
        for raw_json in response_ndjson_iteration(url)
        if validate(schema=schema, data=raw_json)
    )
