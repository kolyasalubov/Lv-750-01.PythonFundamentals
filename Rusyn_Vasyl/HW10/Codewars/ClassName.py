import re


def class_name_changer(cls, new_name):
    # Check if the new name follows the required format
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError(
            "Invalid class name: must start with an uppercase letter, followed by alphanumeric characters only.")

    # Set the new name for the class object
    cls.__name__ = new_name