from pathlib import PurePath


BASE_DIR = PurePath(__file__).parent.parent
CONFIG_DIR = "config"
ENV_FILE_TEMPLATE = ".env.template"
ENV_FILE = ".env"

FULL_PATH_ENV_FILE_TEMPLATE = PurePath(BASE_DIR, CONFIG_DIR, ENV_FILE_TEMPLATE)
FULL_PATH_ENV_FILE = PurePath(BASE_DIR, CONFIG_DIR, ENV_FILE)

race_code_url = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race'
ethnicity_code_url = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity'

required_fields = {
    "Encounter": [
        "source_id", "patient_id", "start_date", "end_date", "type_code",
        "type_code_system"
    ],
    "Patient": [
        "source_id", "birth_date", "gender", "race_code", "race_code_system",
        "ethnicity_code", "ethnicity_code_system", "country"
    ],
    "Procedure": [
        "source_id", "patient_id", "encounter_id", "procedure_date",
        "type_code", "type_code_system"
    ],
    "Observation": [
        "source_id", "patient_id", "encounter_id", "observation_date",
        "type_code", "type_code_system", "value", "unit_code",
        "unit_code_system"
    ]
}
