def validate_obj_list(obj_to_validate, valid_obj):
    """Check if object is a list or a specified object"""

    # check if list of objects
    if isinstance(obj_to_validate, list):
        for obj in obj_to_validate:
            if isinstance(obj, valid_obj):
                return obj_to_validate

    # check if object
    if isinstance(obj_to_validate, valid_obj):
        return [obj_to_validate]

    raise TypeError('Invalid object type...')
