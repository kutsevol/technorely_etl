import pandas as pd

from etl.base import BaseETL
from schemas import observation_schema


class ObservationETL(BaseETL):
    name = "Observation"

    def __init__(self, url, session):
        super().__init__(url, session)
        self.schema = observation_schema
        self.json_file_name = "Observation.ndjson"
        self.table_name = "observation"

    def refinement_dataframe(self):
        self.df.rename(
            columns={'id': 'source_id',
                     "effectiveDateTime": "observation_date"},
            inplace=True
        )
        # Unpack list value in column and create base on this rows
        self.df = self.df.explode("component").reset_index(drop=True)

        # Split data on / and get id patient or encounter
        self.df['patient_id'] = self.df.subject.apply(
            pd.Series).reference.str.partition("/")[2]
        self.df["encounter_id"] = self.df.context.apply(
            pd.Series).reference.str.partition("/")[2]

        value_quantity_col = self.df.valueQuantity.apply(pd.Series)
        code_col = self.df.code.apply(pd.Series).coding.apply(
            pd.Series)[0].apply(pd.Series)

        component_col = self.df.component.apply(pd.Series)
        code_component_col = component_col.code.apply(pd.Series)
        value_quantity_component_col = component_col.valueQuantity.apply(
            pd.Series)

        # Combine unpacked component column and simple column
        self.df[
            ["type_code", "type_code_system"]
        ] = code_component_col.coding.apply(pd.Series)[0].apply(
            pd.Series)[["code", "system"]].fillna(code_col[["code", "system"]])

        self.df[
            ["value", "unit_code", "unit_code_system"]
        ] = value_quantity_component_col[["value", "unit", "system"]].fillna(
            value_quantity_col[["value", "unit", "system"]])

        self.df = self.df.loc[self.df.encounter_id.isin(
            self.read_query("encounter").source_id.tolist()
        )]
        return self.df
