from file import File
import pathlib
import gdal


class Image(File):
    _flavour = pathlib.Path('.')._flavour

    @property
    def get_x_size(self):
        if self.is_file():
            if self.exists():
                data_set = gdal.Open(self, gdal.GA_ReadOnly)
                return data_set.RasterXSize

    @property
    def get_y_size(self):
        if self.is_file():
            if self.exists():
                data_set = gdal.Open(self, gdal.GA_ReadOnly)
                return data_set.RasterYSize


