from peewee import Model

def insert_enum_values(model: Model, values: list, value_field: str = 'id'):
    existing_values = {getattr(enum, value_field) for enum in model.select(getattr(model, value_field))}
    values_to_insert = sorted([val for val in values if val not in existing_values])

    if values_to_insert:
        with model._meta.database.atomic():
            model.insert_many([{value_field: val} for val in values_to_insert]).execute()