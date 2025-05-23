STORE_SCHEMA = {
      {
        "id": {
            "type": "integer"
        },
        "petId": {
            "type": "integer"
        },
        "quantity": {
            "type": "integer"
        },
        "shipDate": {
            "type": "string",
            "enum": ["placed", "approved", "delivered"]
        },
        "complete": {
            "type": "boolean"
        },
        "additionalProperties": False
    }
}
