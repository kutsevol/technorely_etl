import fastjsonschema


def validate(schema, data):
    """
    Check json files accordingly to schema
    :param schema: json schema
    :param data: json
    """

    try:
        fastjsonschema.validate(definition=schema, data=data)
    except fastjsonschema.exceptions.JsonSchemaException:
        return False
    return True
