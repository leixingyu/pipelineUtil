import os
import shutil


def create_dir(path):
    """
    Create a working directory

    :param path: str. name of the folder
    :return: str. full path of the folder
    """

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('directory already exists')

    os.startfile(path)
    print('Created working directory: \n\t{}'.format(path))
    return path


def copy_file(src_path, dst_path):
    """
    Copy the file from one place to the other

    :param src_path: str. source file full path
    :param dst_path: str. destination folder full path
    """
    if not os.path.isfile(src_path):
        print('file not located')
        return

    file_name = os.path.basename(src_path)
    if os.path.isfile(os.path.join(dst_path, file_name)):
        print('file already exists in destination directory')
        return

    shutil.copy(src_path, dst_path)


def get_files(path):
    """
    Return only files not directories inside a directory

    :param path: str. root directory for searching
    :return: list. list of files in that directory
    """
    return [f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))]
