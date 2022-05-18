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
        @abc.abstractmethod
        def __fill_lists(*args) -> None:
            """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de
                   imagens """
            ...

    @abc.abstractmethod
    def build_vtex_spreadsheet(self) -> None:
        """Transforma as informações presentes no dicionário de imagens em listas para transformá-las em linhas e alimentar
                o DataFrame."""
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

