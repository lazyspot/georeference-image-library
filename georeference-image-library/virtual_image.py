from virtual_file import VirtualFile


class VirtualImage(VirtualFile):
    def __init__(self, path):
        VirtualFile.__init__(self,path=path)
        self.x_size = 0
        self.y_size = 0

    def get_compression_type(self):
        pass

    def get_resolution(self):
        pass