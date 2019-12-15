import pandas as pd

from schemas import encounter_schema
from utils.stats import get_stats_of_popular_days_of_week
from etl.base import BaseETL


class EncounterETL(BaseETL):
    name = "Encounter"

    def __init__(self, url, session):
        super().__init__(url, session)
        self.schema = encounter_schema
        self.json_file_name = "Encounter.ndjson"
        self.table_name = "encounter"

    def refinement_dataframe(self):
        self.df.rename(
            columns={"id": "source_id"},
            inplace=True
        )
        self.df["patient_id"] = self.df.subject.apply(
            pd.Series).reference.str.partition("/")[2]

        self.df[["start_date", "end_date"]] = self.df.period.apply(pd.Series)

        self.df[["type_code", "type_code_system"]] = self.df.type.apply(
            pd.Series)[0].apply(pd.Series).coding.apply(pd.Series)[0].apply(
            pd.Series)[["code", "system"]]
        return self.df

    def get_the_most_and_least_popular_days_by_col(self, col):
        return get_stats_of_popular_days_of_week(self.df, col)
