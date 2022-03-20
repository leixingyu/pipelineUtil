"""
Example:

path = r"C:\Users\Admin\test.txt"
a = File(path)
print(a.__dict__)

"""


import logging
import os

from . import info


class File(object):

    def __init__(self, path):
        if not os.path.isfile(path):
            logging.error('file % cannot be found', path)

        self._path = path
        self._mtime = 0
        self._ctime = 0
        self._size = 0

        self.update()

    def update(self):
        self.update_size()
        self.update_ctime()
        self.update_mtime()

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._path)

    @classmethod
    def get_from_dir(cls, directory):
        assets = list()
        files = os.listdir(directory)
        for f in files:
            if os.path.isfile(f):
                assets.append(cls(f))

        return assets

    @property
    def name(self):
        return os.path.basename(self._path)

    @property
    def ext(self):
        return os.path.splitext(self.name)

    @property
    def directory(self):
        return os.path.dirname(self._path)

    @property
    def path(self):
        return self._path

    @property
    def thumbnail(self):
        pass

    @property
    def owner(self):
        pass

    @property
    def size(self):
        return self._size

    @property
    def ctime(self):
        return self._ctime

    @property
    def mtime(self):
        return self._mtime

    def update_size(self):
        self._size = info.get_file_size(self._path)

    def update_mtime(self):
        self._mtime = info.get_modify_time(self._path)

    def update_ctime(self):
        self._ctime = info.get_create_time(self._path)

    def fopen(self):
        pass

    def fimport(self):
        pass

    def delete(self):
        os.remove(self._path)
