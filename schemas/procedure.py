procedure_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
        },
        "subject": {
            "type": "object",
            "properties": {
                "reference": {
                    "type": "string"
                }
            },
            "required": ["reference"]
        },
        "context": {
            "type": "object",
            "properties": {
                "reference": {
                    "type": "string"
                }
            },
            "required": ["reference"]
        },
        "performedDateTime": {
            "type": "string"
        },
        "performedPeriod": {
            "type": "object",
            "properties": {
                "start": {
                    "type": "string"
                },
                "end": {
                    "type": "string"
                }
            }
        },
        "code": {
            "type": "object",
            "properties": {
                "coding": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string"
                            },
                            "system": {
                                "type": "string"
                            }
                        },
                        "required": ["code", "system"]
                    }
                }
            },
            "required": ["coding"]
        },
    },
    "required": ["id", "subject", "code"]
}
