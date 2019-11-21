import os
from file import File


class Image(File):
    def __init__(self, path):
        File.__init__(self, path=path)
        self.__x_size = 0
        self.__y_size = 0

    def get_x_size(self):
        pass

    def get_y_size(self):
        pass
