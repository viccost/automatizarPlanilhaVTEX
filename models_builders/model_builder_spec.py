import pandas as pd
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from models.models import SpecSheet
from models_builders.model_builder import ModelBuilder


# --------------------- Planilha Especificações


class BuilderSpecSheet(ModelBuilder):
    processed_data = {}

    def __init__(self, spreadsheet: pd.DataFrame):
        super().__init__(spreadsheet)
        self.__filename = "VTEX Espec built in Python"

    @property
    def filename(self):
        return self.__filename

    def colect_data(self) -> None:
        try:
            # utilizando o iloc para poder naver pelas linhas e colunas
            for index, valor in self.spreadsheet.iloc[:, 0].items():
                # percorrendo todas as linhas
                self.fill_lists(
                    self.spreadsheet.iloc[index, 0],
                    self.spreadsheet.iloc[index, 1],
                    self.spreadsheet.iloc[index, 9],
                    self.spreadsheet.iloc[index, 16],
                    self.spreadsheet.iloc[index, 17],
                    self.spreadsheet.iloc[index, 18],
                    self.spreadsheet.iloc[index, 19],
                )
                # alterar esse tipo de identificação de coluna
        except IndexError:
            print("Cheque se a sua planilha tem todas as colunas necessárias!")
            exit()

    def fill_lists(
            self,
            sku: int,
            id_product: int,
            nome_prd: str,
            inf_tec: str,
            inf_for: str,
            desc: str,
            video: str,
    ) -> None:
        infos = list()

        if str(inf_tec) != "nan":
            infos.append(["51", inf_tec, "Informações Técnicas"])
        if str(inf_for) != "nan":
            infos.append(["52", inf_for, "Informações do Fornecedor"])
        if str(desc) != "nan":
            infos.append(["53", desc, "Descrição do Produto"])
        if str(video) != "nan":
            infos.append(["56", video, "Vídeo do Produto"])

        self.processed_data[sku] = {
            "Nome Produto": nome_prd,
            "Informações": infos,
            "IdProduto": id_product,
        }

    def build_vtex_spreadsheet(self) -> SpecSheet:
        id_campo_valor = nome_campo_valor = codigo_referencia_produto = []
        (
            nome_campo,
            id_produto,
            nome_produto,
            id_campo,
            valor_especificacao,
            nome_tipo_campo,
            codigo_especificacao,
        ) = ([] for i in range(7))

        for key in self.processed_data.keys():
            linhas_desse_id = len(
                self.processed_data[key]["Informações"]
            )
            id_produto.extend(
                [self.processed_data[key]["IdProduto"]]
                * linhas_desse_id
            )
            nome_produto.extend(
                [self.processed_data[key]["Nome Produto"]]
                * linhas_desse_id
            )
            for valor in self.processed_data[key]["Informações"]:
                id_campo.append(valor[0])
                nome_campo.append(valor[2])
                valor_especificacao.append(valor[1])
                nome_tipo_campo.append("Texto Grande")

        self.builded_model = SpecSheet(id_produto, nome_produto, id_campo, nome_campo, nome_tipo_campo, id_campo_valor,
                                       nome_campo_valor, codigo_especificacao, valor_especificacao,
                                       codigo_referencia_produto).spreadsheet

        return self.builded_model

    def verifications(self, *args) -> None:
        ...


if __name__ == "__main__":
    specification_spreadsheet = BuilderSpecSheet(gerar_dataframe(escolher_arquivo()))
    salvar_arquivo_planilha(specification_spreadsheet.builded_model, specification_spreadsheet.filename, 'xlsx')
