encounter_schema = {
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
        "period": {
            "type": "object",
            "properties": {
                "start": {
                    "type": "string"
                },
                "end": {
                    "type": "string"
                }
            },
            "required": ["start", "end"]
        },
        "type": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    },
                    "coding":  {
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
                        }
                    }
                },
            }
        }
    },
    "required": ["id", "subject", "period"]
}
