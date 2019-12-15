observation_schema = {
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
        "effectiveDateTime": {
            "type": "string"
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
        "valueQuantity": {
            "type": "object",
            "properties": {
                "unit": {
                    "type": "string"
                },
                "value": {
                    "type": ["string", "number"]
                },
                "system": {
                    "type": "string"
                }
            },
            "required": ["unit"]
        },
        "component": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string"
                            },
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
                                        },
                                        "display": {
                                            "type": "string"
                                        }
                                    },
                                    "required": ["code", "system", "display"]
                                }
                            }
                        },
                        "required": ["text", "coding"]
                    },
                    "valueQuantity": {
                        "type": "object",
                        "properties": {
                            "unit": {
                                "type": "string"
                            },
                            "value": {
                                "type": ["string", "number"]
                            },
                            "system": {
                                "type": "string"
                            }
                        },
                        "required": ["unit"]
                    }
                },
                "required": ["code", "valueQuantity"]
            }
        }
    },
    "required": ["id", "subject", "effectiveDateTime", "code"],
    "anyOf": [
        {"required": ["valueQuantity"]},
        {"required": ["component"]}
    ]
}
