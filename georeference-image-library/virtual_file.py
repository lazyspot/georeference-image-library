class VirtualFile:
    def __init__(self, path):
        self.__path = path
        self.__filename = path
        self.__extension = ""
        '''Get file nam from path'''
        if '/' in self.__path:
            self.__filename = self.__path.split("/")[-1]
        if '\\' in self.__path:
            self.__filename = self.__path.split("\\")[-1]
        '''Get extension from path.'''
        i = 1
        while i < len(self.__filename.split(".")):
            self.__extension += "." + self.__filename.split(".")[i]
            i += 1

    @property
    def get_filename(self):
        return str(self.__filename)

    @property
    def get_file(self):
        return str(self.__filename.split(".")[0])

    @property
    def get_extension(self):
        return str(self.__extension)

    @property
    def get_path(self):
        return str(self.__path)

    @property
    def get_directory(self):
        if '/' in self.__path:
            return str(self.__path[:-len(self.__path.split("/")[-1])])
        elif '\\' in self.__path:
            return str(self.__path[:len(self.__path.split("\\")[-1])])
        else:
            return ""

    @property
    def delete_file(self):
        return str("rm " + self.__path)
