from core.db import session
from etl.encounter import EncounterETL
from etl.patient import PatientETL
from etl.procedure import ProcedureETL
from etl.observation import ObservationETL
from utils.constants import required_fields


def run_etl(url):
    for etl in [PatientETL, EncounterETL, ProcedureETL, ObservationETL]:
        instance = etl(
            url,
            session
        )
        instance.set_dataframe_from_url()
        instance.refinement_dataframe()
        instance.remain_only_required_fields(
            required_fields=required_fields[instance.get_name()]
        )
        instance.export_in_db()
        print(f"Rows {instance.show_amount_rows()} in "
              f"table - {instance.get_name()}")

        if instance.get_name() == "Encounter":
            days = instance.get_the_most_and_least_popular_days_by_col(
                "start_date"
            )
            print(f"The most popular day is {days[0]} and "
                  f"the least popular day is {days[1]}")

        elif instance.get_name() == "Patient":
            print(f"Count patient by gender:")
            for gender, count in instance.get_stats_by_gender().items():
                print(f"{gender} - {count}")

        elif instance.get_name() == "Procedure":
            print("Procedure\tCount\n")
            print(instance.get_top_n_in_column("type_code", 10))
