import logging
import os
import shutil


logger = logging.getLogger(__name__)


def create_dir(path):
    """
    Create a working directory

    :param path: str. name of the folder
    :return: str. full path of the folder
    """
    try:
        os.makedirs(path)
        logger.info('Created working directory: \n\t%s', path)
        return path
    except FileExistsError:
        logger.error('Directory already exists: \n\t%s', path)
    except Exception as e:
        logger.error('Failed to create directory: \n\t%s', path)
    return ''


def copy_file(src_path, dst_path):
    """
    Copy the file from one place to the other

    :param src_path: str. source file full path
    :param dst_path: str. destination folder full path
    :return: bool. whether the copy is successful
    """
    if not os.path.isfile(src_path):
        logger.warning('%s not located', src_path)
        return False

    file_name = os.path.basename(src_path)
    if os.path.isfile(os.path.join(dst_path, file_name)):
        logger.warning('%s already exists in destination directory', file_name)
        return False

    shutil.copy(src_path, dst_path)
    return True


def get_files(path):
    """
    Return only files not directories inside a directory

    :param path: str. root directory for searching
    :return: list. list of files in full path of that directory
    """
    return [os.path.join(path, f) for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))]


def get_files_recursive(path):
    """
    Return files (not directories) recursively inside a directory

    :param path: str. root directory for searching
    :return: list. list of files in full path of that directory
    """
    files = list()
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            files.extend((get_files_recursive(full_path)))
    return files


def operate_file_recursive(path, func):
    """
    Recursively operate on files (not directories) inside a directory

    :param path: str. root directory for searching
    :param func: function callback
    """
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            func(full_path)
        else:
            operate_file_recursive(full_path, func)


def operate_dir_recursive(path, func):
    """
    Recursively operate on files (not directories) inside a directory

    :param path: str. root directory for searching
    :param func: function callback
    """
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if not os.path.isfile(full_path):
            operate_dir_recursive(full_path, func)
            func(full_path)
