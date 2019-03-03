class List:
    NAME = "lists"
    COLUMNS = {
        "name": {
            "bsonType": "string",
            "description": "must be a string and is required"
        }
    }
    VALIDATORS = {
        "$jsonSchema": {
            "bsonType": "object",
            "properties": COLUMNS,
        },
    }
    VALIDATION_LEVEL = "strict"
    VALIDATION_ACTION = "error"


class Item:
    NAME = "items"
    COLUMNS = {
        "text": {
            "bsonType": "string",
            "description": "must be a string and is required",
        },
        "date": {
            "bsonType": "date",
            "description": "must be a date-time and is required",
        },
        "status": {
            "bsonType": "bool",
            "description": "must be a boolean and is required",
        },
        "list_id": {
            "bsonType": "objectId",
            "description": "must be a string and is required",
        }
    }

    REQUIRED = ["list_id"]
    VALIDATORS = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": REQUIRED,
            "properties": COLUMNS,
        },
    }
    VALIDATION_LEVEL = "strict"
    VALIDATION_ACTION = "error"
