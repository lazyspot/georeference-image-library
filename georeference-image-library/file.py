from directory import Directory
import pathlib


class File(Directory):
    _flavour = pathlib.Path('.')._flavour

    @property
    def get_extension(self):
        return ''.join(self.suffixes)

    @property
    def get_filename(self):
        return self.name.split(".")[0]

    # def get__str_slash(self):
    #     return str(self.__str__()).replace("\\", "/")
    #
    # def get__str_backslash(self):
    #     return str(self.parent).replace("/", "\\")
