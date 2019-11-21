import pytest


class VirtualFile:
    def __init__(self, path):
        self.__path = path
        self.__filename = self.__path.split(".")[0]
        self.__extension = ""
        if "/" in str(self.__path) or "\\" in str(self.__path):
            print(self.__path + "t")
            # self.__extension = self.__path.split("/")[1]
        else:
            i = 1
            while i < len(self.__path.split(".")):
                self.__extension += "." + self.__path.split(".")[i]
                i += 1

    @property
    def get_filename(self):
        return str(self.__filename)

    @property
    def get_size(self):
        return int(self.__size)

    @property
    def get_extension(self):
        return str(self.__extension)

    @property
    def get_abs_path(self):
        return str(self.__path)

    @property
    def check_file_exist(self):
        pass

    @property
    def get_path(self):
        return str(self.__path)

    def delete_image(self):
        pass
