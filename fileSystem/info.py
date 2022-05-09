import ctypes
import os
import string
import time


def get_file_size(fpath):
    """
    Get file size in Bytes

    :param fpath: str. file path
    :return: int. size in bytes
    """
    return int(os.path.getsize(fpath))


def get_modify_time(fpath):
    """
    Get file modify time

    :param fpath: str. file path
    :return: int. raw system time
    """
    return time.ctime(os.path.getmtime(fpath))


def get_create_time(fpath):
    """
    Get file creation time

    :param fpath: str. file path
    :return: int. raw system time
    """
    return time.ctime(os.path.getctime(fpath))


def convert_size(size, unit=3):
    """
    Convert the size from bytes to other units like KB, MB or GB

    :param size: int. raw size in bytes
    :param unit: int. output unit
    :return: int. size in converted unit
    """
    class Unit(object):
        BYTES = 1
        KB = 2
        MB = 3
        GB = 4

    if unit == Unit.KB:
        return size / 1024
    elif unit == Unit.MB:
        return size / (1024 * 1024)
    elif unit == Unit.GB:
        return size / (1024 * 1024 * 1024)
    else:
        return size


def get_drives():
    """
    Get drive mounted

    :return: list. list of drive letters mounted
    """
    drives = list()
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def get_path_free_space(path):
    """
    Get how much space is free in a given path

    :param path: str. file path
    :return: int. size in megabytes
    """
    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(
        ctypes.c_wchar_p(path),
        None,
        None,
        ctypes.pointer(free_bytes)
    )
    return free_bytes.value / 1024 / 1024
