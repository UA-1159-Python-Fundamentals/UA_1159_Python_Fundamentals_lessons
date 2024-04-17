def class_name_changer(cls, new_name):
    # Check if the new name follows the naming conventions
    if not new_name[0].isupper():
        raise ValueError("New class name must start with an uppercase letter")
    if not new_name.isalnum():
        raise ValueError("New class name must contain only alphanumeric characters")

    setattr(cls, "__name__", new_name)