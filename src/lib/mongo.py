def create_collections(db, Collection):
    collection = db.get_collection(Collection.NAME)
    if collection.name not in db.collection_names():
        collection = db.create_collection(Collection.NAME, **{
            "validator": Collection.VALIDATORS,
            "validationLevel": Collection.VALIDATION_LEVEL,
        })

    return collection.name
