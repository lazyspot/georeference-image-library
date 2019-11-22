class VirtualDirectory:
    def __init__(self, directory):
        self.__directory = str(directory)

    @property
    def get_directory(self):
        return str(self.__directory)
