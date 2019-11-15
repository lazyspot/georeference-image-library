import os


class Image:
    def __init__(self, path):
        self.__path = path
        self.__path = os.path.abspath(self.__path)
        self.__size = os.path.getsize(self.__path)
        self.__filename = os.path.basename(self.__path).split(".")[0]
        self.__extension = os.path.basename(self.__path).split(".")[1]

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
        if not os.path.isfile(self.__path):
            raise Exception("File %s not exist", self.__path)

    @property
    def get_path(self):
        if "/" in str(self.__path):
            return "/".join(str(self.__path).split('/')[:-1])
        elif '\\' in str(self.__path):
            return "\\".join(str(self.__path).split('\\')[:-1])
        else:
            raise Exception("Extension error.")

    def delete_image(self):
        try:
            os.remove(str(self.get_abs_path))
            print("Successful delete file " + str(self.get_abs_path))
        except:
            raise Exception("Unsupported error:", os.sys.exc_info()[0])
