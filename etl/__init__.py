import requests

# from handlers.dataframe import create_dataframe_by_ndjson_url

# from utils.constants import relation_names


# def run_etls(url):
#     for name, objects in relation_names:
#         df = create_dataframe_by_ndjson_url(
#             url=f"{url}/{objects['json_file']}?raw=true",
#             schema=objects['json_schema']
#         )



# df = create_dataframe_by_ndjson_url(
#     url='https://raw.githubusercontent.com/smart-on-fhir/flat-fhir-files/master/r3/Encounter.ndjson',
#     schema=encounter_schema
# )


# print(requests.get("https://github.com/smart-on-fhir/flat-fhir-files/blob/master/r3/Patient.ndjson?raw=true").text)

# from etl.encounter import EncounterETL
# from utils.constants import encounter_required_fields
#
# encounter = EncounterETL("https://github.com/smart-on-fhir/flat-fhir-files/blob/master/r3")
# encounter.set_dataframe_from_url()
# encounter.refinement_dataframe()
# encounter.remain_only_required_fields(encounter_required_fields)
# encounter.export_in_db()
# print(encounter.show_amount_rows())
# print(encounter.get_the_most_and_least_popular_days_by_col("start_date"))
