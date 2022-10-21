import logging
import os
import shutil


logger = logging.getLogger(__name__)


def create_dir(path):
    """
    Create a working directory

    :param path: str. full name of the folder to be created
    :return: str.
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


def copy_file(src_file, dst_folder):
    """
    Copy the file from one place to the other

    :param src_file: str. source file full path
    :param dst_folder: str. destination folder full path
    :return: bool. whether the copy is successful
    """
    if not os.path.isfile(src_file):
        logger.warning('%s not located', src_file)
        return False

    file_name = os.path.basename(src_file)
    if os.path.isfile(os.path.join(dst_folder, file_name)):
        logger.warning('%s already exists in destination directory', file_name)
        return False

    shutil.copy(src_file, dst_folder)
    return True


def copy_file_content(src_file, dst_file):
    """
    Copy the file content from one file to another

    :param src_file: str. source file full path
    :param dst_file: str. destination file full path
    """
    with open(src_file, 'r') as from_file, open(dst_file, 'w') as to_file:
        file_content = from_file.read()
        to_file.write(file_content)


def get_files(folder):
    """
    Return only files not directories inside a directory

    :param folder: str. root directory for searching
    :return: list. list of files in full path of that directory
    """
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))]


def get_files_recursive(folder):
    """
    Return files (not directories) recursively inside a directory

    :param folder: str. root directory for searching
    :return: list. list of files in full path of that directory
    """
    files = list()
    for f in os.listdir(folder):
        full_path = os.path.join(folder, f)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            files.extend((get_files_recursive(full_path)))
    return files


def operate_file_recursive(folder, func):
    """
    Recursively operate on files (not directories) inside a directory

    :param folder: str. root directory for searching
    :param func: function callback
    """
    for f in os.listdir(folder):
        full_path = os.path.join(folder, f)
        if os.path.isfile(full_path):
            func(full_path)
        else:
            operate_file_recursive(full_path, func)


def operate_folder_recursive(folder, func):
    """
    Recursively operate on files (not directories) inside a directory

    :param folder: str. root directory for searching
    :param func: function callback
    """
    for f in os.listdir(folder):
        full_path = os.path.join(folder, f)
        if not os.path.isfile(full_path):
            operate_folder_recursive(full_path, func)
            func(full_path)
