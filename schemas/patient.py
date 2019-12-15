patient_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
        },
        "gender": {
            "type": "string"
        },
        "birthDate": {
            "type": "string"
        },
        "address": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                    }
                }
            }
        },
        "extension": {
            "type": "array",
            "minProperties": 2,
            "items": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string"
                    },
                    "valueCodeableConcept": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string"
                            },
                            "coding": {
                                "type": "array",
                                "maxProperties": 1,
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                        },
                                        "system": {
                                            "type": "string"
                                        },
                                        "external_field": {
                                            "type": "string"
                                        }
                                    },
                                    "required": ["code", "system"]
                                }
                            }
                        },
                        "required": ["text", "coding"]
                    }
                }
            },
            "required": ["url", "valueCodeableConcept"]
        }
    },
    "required": ["id", "gender"]
}
