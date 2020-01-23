import pathlib


class Directory(pathlib.Path):
    _flavour = pathlib.Path('.')._flavour

    def get_directory_str_slash(self):
        return str(self.__str__()).replace("\\", "/")

    def get_directory_str_backslash(self):
        return str(self.__str__()).replace("/", "\\")

    def create_directory_hierarchy(self):
        self.mkdir(mode=0o777, parents=True, exist_ok=True)
