from app.serializers.enums import EnumItem


def enum_to_dict(enum_class) -> list[EnumItem]:
    return [EnumItem(name=item.name, value=item.value) for item in enum_class]
