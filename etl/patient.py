import pandas as pd

from etl.base import BaseETL
from schemas import patient_schema
from utils.constants import race_code_url, ethnicity_code_url
from utils.stats import get_stats_by_gender


class PatientETL(BaseETL):
    name = "Patient"

    def __init__(self, url, session):
        super().__init__(url, session)
        self.schema = patient_schema
        self.json_file_name = "Patient.ndjson"
        self.table_name = "patient"

    def refinement_dataframe(self):
        self.df.rename(
            columns={"id": "source_id", "birthDate": "birth_date"},
            inplace=True
        )

        self.df['country'] = self.df.address.apply(pd.Series)[0].apply(
            pd.Series)[["country"]]

        extension = self.df.extension.apply(pd.Series)

        dict_codes = {
            race_code_url: self._get_code_and_system_cols,
            ethnicity_code_url:  self._get_code_and_system_cols
        }

        for col in list(extension):
            if race_code_url in extension[col].apply(pd.Series)["url"].unique():
                self.df[
                    ["race_code", "race_code_system"]
                ] = dict_codes[race_code_url](extension, col)
            elif ethnicity_code_url in extension[col].apply(pd.Series)[
                "url"].unique():
                self.df[
                    ["ethnicity_code", "ethnicity_code_system"]
                ] = dict_codes[ethnicity_code_url](extension, col)
            continue

        return self.df

    @staticmethod
    def _get_code_and_system_cols(df, col):
        return df[col].apply(pd.Series).valueCodeableConcept.apply(
            pd.Series).coding.apply(pd.Series)[0].apply(
            pd.Series)[["code", "system"]]

    def get_stats_by_gender(self):
        return get_stats_by_gender(self.df)
