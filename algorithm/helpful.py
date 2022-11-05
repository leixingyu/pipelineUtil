"""
Stuff that is helpful gathered here and there
"""


def get_percentages(sample_count):
    """
    Get normalized percent for each sample

    :param sample_count: int. number of sample point
    :return: list. normalized percents
    """
    if sample_count <= 1:
        return

    outputs = list()
    gap = 1.00 / (sample_count-1)
    for index in range(sample_count):
        outputs.append(index * gap)

    return outputs


def enum_mapping(cls, enum):
    """
    Get Enumerator namespace and value mapping

    e.g. Used for Qt flag
    ```
    enum = enum_mapping(QtCore.Qt, QtCore.Qt.AlignmentFlag)
    # enum = enum_mapping(QtWidgets, QtWidgets.QStyle)

    for item in sorted(enum.items(), key=str):
    print('%s: %s' % item)
    ```

    :param cls: str. class name
    :param enum: str. enum name
    :return: {str: int}. namespace as key and enum value as value
    """
    mapping = dict()
    for key in dir(cls):
        value = getattr(cls, key)
        if isinstance(value, enum):
            mapping[key] = value
    return mapping
