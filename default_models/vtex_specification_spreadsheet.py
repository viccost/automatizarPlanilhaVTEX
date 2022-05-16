import pandas as pd
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from vtex_spreadsheet import VtexSpreadsheet


# --------------------- Planilha Especificações


class SpecificationSpreadsheet(VtexSpreadsheet):
    specification_spreadsheet_skeleton = {}

    def __init__(self, spreadsheet: pd.DataFrame):
        super().__init__(spreadsheet)
        self.file_name = "VTEX Espec built in Python"

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

        self.specification_spreadsheet_skeleton[sku] = {
            "Nome Produto": nome_prd,
            "Informações": infos,
            "IdProduto": id_product,
        }

    def build_vtex_spreadsheet(self) -> pd.DataFrame:
        id_campo_valor = nome_campo_valor = codigo_referencia_produto = []
        (
            nome_campo,
            sku_procx,
            id_produto,
            nome_produto,
            id_campo,
            valor_especificacao,
            nome_tipo_campo,
            codigo_especificacao,
        ) = ([] for i in range(8))

        for key in self.specification_spreadsheet_skeleton.keys():
            linhas_desse_id = len(
                self.specification_spreadsheet_skeleton[key]["Informações"]
            )
            id_produto.extend(
                [self.specification_spreadsheet_skeleton[key]["IdProduto"]]
                * linhas_desse_id
            )
            nome_produto.extend(
                [self.specification_spreadsheet_skeleton[key]["Nome Produto"]]
                * linhas_desse_id
            )
            for valor in self.specification_spreadsheet_skeleton[key]["Informações"]:
                id_campo.append(valor[0])
                nome_campo.append(valor[2])
                valor_especificacao.append(valor[1])
                nome_tipo_campo.append("Texto Grande")
        planilha_vtex = {
            "_IdProduto (Não alterável)": id_produto,
            "_NomeProduto (Não alterável)": nome_produto,
            "IdCampo (Não alterável)": id_campo,
            "NomeCampo (Não alterável)": nome_campo,
            "NomeTipoCampo (Não alterável)": nome_tipo_campo,
            "IdCampoValor (Não alterável)": id_campo_valor,
            "NomeCampoValor (Não alterável)": nome_campo_valor,
            "CodigoEspecificacao (Não alterável)": codigo_especificacao,
            "ValorEspecificacao": valor_especificacao,
            "_CodigoReferenciaProduto (Não alterável)": codigo_referencia_produto,
        }
        dataframe_vtex = pd.DataFrame.from_dict(planilha_vtex, orient="index")
        dataframe_vtex = dataframe_vtex.transpose()
        return dataframe_vtex


if __name__ == "__main__":
    planilha = gerar_dataframe(escolher_arquivo())
    specification_spreadsheet = SpecificationSpreadsheet(planilha)
    spreadsheet = specification_spreadsheet.init_process()
    salvar_arquivo_planilha(spreadsheet[1], spreadsheet[0], 'xlsx')