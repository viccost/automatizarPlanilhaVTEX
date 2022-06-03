import abc
from pandas import DataFrame


class ModelBuilder:
    def __init__(self, spreadsheet: DataFrame):
        self.spreadsheet = spreadsheet
        self.builded_model = DataFrame()
        self.colect_data()
        self.build_vtex_spreadsheet()
        self.lower_headers()

    @property
    @abc.abstractmethod
    def filename(self):
        ...

    @abc.abstractmethod
    def colect_data(self):
        """This function is the first step. Must receives the dataframe and runs its rows.
            Responsible for get importants columns to the model and send the data to next step.
        """
        ...

    @abc.abstractmethod
    def fill_lists(self, *args) -> None:
        """Cria um dicionário com SKU como chave, {SKU: {COLUMNS}} com os campos necessários para o preenchimento das
        planilhas. Basicamente preenchendo as colunas"""
        ...

    @abc.abstractmethod
    def build_vtex_spreadsheet(self) -> None:
        """Transforma as informações presentes no dicionário em listas para transformá-las em linhas e alimen
        tar o DataFrame. Distribuindo as informações."""
        ...

    @abc.abstractmethod
    def verifications(self, *args) -> None:
        """call the necessaries verifications"""
        ...

    def lower_headers(self):
        """Change all spreadsheet's keys to lowercase"""
        for key in self.spreadsheet.keys():
            teste = str.lower(key)
            self.spreadsheet.rename(columns={f"{key}": teste}, inplace=True)
