from virtual_directory import VirtualDirectory


class VirtualFile(VirtualDirectory):
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

        if '/' in self.__path:
            VirtualDirectory.__init__(self, directory=str(self.__path[:-len(self.__path.split("/")[-1])]))
        elif '\\' in self.__path:
            VirtualDirectory.__init__(self, directory=str(self.__path[:len(self.__path.split('\\')[-1])]))
        else:
            VirtualDirectory.__init__(self, directory="")

    def __del__(self):
        pass

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
    def delete_file(self):
        return str("rm " + self.__path)

    def change_backslash_to_slash(self):
        """WARNING: NOT WORKING"""
        if "\\" in self.__path:
            self.__init__(path=str(self.__path).replace("\\", "/"))

    def change_slash_to_backslash(self):
        """WARNING: NOT WORKING"""
        if "/" in self.__path:
            self.__init__(path=str(self.__path).replace("/", '\\'))
