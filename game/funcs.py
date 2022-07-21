def validate_obj_list(obj_to_validate, valid_obj):
    """
    Check if object is a list of the specified
    object or the specified object.

    :param obj_to_validate: Object or list to validate.
    :param valid_obj: The object to validate.
    :return: List of objects that are valid.
    """

    # validate list of objects
    if isinstance(obj_to_validate, list):
        for obj in obj_to_validate:
            if isinstance(obj, valid_obj):
                return obj_to_validate

    # validate object
    if isinstance(obj_to_validate, valid_obj):
        return [obj_to_validate]

    raise TypeError('Invalid object type...')
