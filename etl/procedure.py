import pandas as pd

from schemas import procedure_schema
from utils.stats import get_top_n_in_column
from etl.base import BaseETL


class ProcedureETL(BaseETL):
    name = "Procedure"

    def __init__(self, url, session):
        super().__init__(url, session)
        self.schema = procedure_schema
        self.json_file_name = "Procedure.ndjson"
        self.table_name = "procedure"

    def refinement_dataframe(self):
        self.df.rename(
            columns={"id": "source_id"},
            inplace=True
        )
        self.df['patient_id'] = self.df.subject.apply(
            pd.Series).reference.str.partition("/")[2]
        self.df["encounter_id"] = self.df.context.apply(
            pd.Series).reference.str.partition("/")[2]

        # Combine 2 different columns performedDateTime and PerformedPeriod
        self.df["procedure_date"] = self.df.performedDateTime.fillna(
            self.df.performedPeriod.apply(pd.Series).start)

        self.df[["type_code", "type_code_system"]] = self.df.code.apply(
            pd.Series).coding.apply(pd.Series)[0].apply(
            pd.Series)[["code", "system"]]

        return self.df

    def get_top_n_in_column(self, col, n):
        return get_top_n_in_column(self.df, col, n)
