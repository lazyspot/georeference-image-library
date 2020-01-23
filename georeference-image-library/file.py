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