import abc
from pandas import DataFrame


class VtexSpreadsheet(metaclass=abc.ABCMeta):
    def __init__(self, spreadsheet: DataFrame):
        self.file_name = None
        self.spreadsheet = spreadsheet

    @abc.abstractmethod
    def colect_data(self):
        ...

    @abc.abstractmethod
    def fill_lists(self, *args):
        ...

    @abc.abstractmethod
    def build_vtex_spreadsheet(self):
        ...

    def init_process(self) -> list[str, build_vtex_spreadsheet]:
        """Returns the model's file name and its spreadsheet object."""
        self.colect_data()
        return [self.file_name, self.build_vtex_spreadsheet()]
