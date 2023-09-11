
def pretty_print_dict(d, indent_level=0):
    """
    Pretty print nested dictionary

    :param d: dict.
    :param indent_level: indentation level
    """
    for key, value in d.items():
        print('\t' * indent_level + str(key))
        if isinstance(value, dict):
            pretty_print_dict(value, indent_level + 1)
        else:
            print('\t' * (indent_level + 1) + str(value))


def pretty_print_list(lst, indent_level=0):
    """
    Pretty print nested list

    :param lst: list.
    :param indent_level: int. indentation level,
    """
    for item in lst:
        if isinstance(item, list):
            pretty_print_list(item, indent_level + 1)
        else:
            print('\t' * indent_level + str(item))


def flatten_list(lst):
    """
    Flatten nested (multi-level) list to one level

    :param lst: list.
    :return: list. list flattened
    """
    flattened_list = list()
    for element in lst:
        if type(element) == list:
            flattened_list += flatten_list(element)
        else:
            flattened_list += element
    return flattened_list
