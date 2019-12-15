import pandas as pd

from handlers.dataframe import create_dataframe_by_ndjson_url
from utils.stats import get_count_rows


class BaseETL:
    name = "Base"

    def __init__(self, url, session):
        self.url = url
        self.session = session
        self.df = None
        self.json_file_name = None
        self.schema = None
        self.table_name = None

    def set_dataframe_from_url(self):
        """
        Parse ndjson from url
        :return: pandas DateFrame
        """
        self.df = create_dataframe_by_ndjson_url(
            url=f"{self.url}/{self.json_file_name}?raw=true",
            schema=self.schema
        )

    def remain_only_required_fields(self, required_fields=()):
        self.df = self.df[required_fields]
        return self.df

    def refinement_dataframe(self):
        raise NotImplementedError

    def show_amount_rows(self):
        return get_count_rows(self.df)

    def export_in_db(self):
        self.df.to_sql(
            self.table_name, self.session.get_bind(), if_exists="append",
            index=False, index_label="id", chunksize=100
        )
        return True

    def read_query(self, table_name):
        return pd.read_sql_query(f"SELECT source_id from {table_name}",
                                 con=self.session.get_bind())

    def get_name(self):
        return self.name
