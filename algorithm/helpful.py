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


def paths_to_nested_dict(paths):
    """
    Turns a file paths into a nested dictionary representing the folder
    hierarchy.

    https://stackoverflow.com/a/66995788/18298763
    :param paths: [str]. file paths
    :return: {str: str}. nested dictionary representing folder hierarchy
    """
    paths = sorted(
        paths,
        key=lambda s: len(s.lstrip('/').split('/')),
        reverse=True
    )

    tree_path = dict()
    for path in paths:
        levels = path.lstrip('/').split('/')
        file = levels.pop()
        acc = tree_path
        for i, folder in enumerate(levels, start=1):
            if i == len(levels):
                acc[folder] = acc[folder] if folder in acc else []
                if isinstance(acc[folder], list):
                    acc[folder].append(file)
            else:
                acc.setdefault(folder, {})
            acc = acc[folder]

    return tree_path
