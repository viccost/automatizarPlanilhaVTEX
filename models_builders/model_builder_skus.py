from pandas import DataFrame
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from models_builders.model_builder import ModelBuilder
from verifications.verifications import verify_id
from typing import List
from models.models import SkuSheet


# --------------------- Planilha Produtos


class BuilderSkuSheet(ModelBuilder):
    processed_data = {}  # deve ser encapsulado de alguma forma

    def __init__(self, spreadsheet: DataFrame):
        super().__init__(spreadsheet)
        self.__file_name = "VTEX Produtos built in Python"

    @property
    def filename(self):
        return self.__file_name

    def colect_data(self) -> None:
        for index, valor in self.spreadsheet.iloc[:, 0].items():
            self.fill_lists(
                [self.spreadsheet.iloc[index, n] for n in range(0, 21)]
            )

    def fill_lists(self, spreadsheet_fields):
        sku = spreadsheet_fields[0]
        self.processed_data[sku] = {
            "NomeSKU": spreadsheet_fields[2],
            "EAN": spreadsheet_fields[3],
            "Altura": spreadsheet_fields[4],
            "Largura": spreadsheet_fields[5],
            "Comprimento": spreadsheet_fields[6],
            "Peso": (spreadsheet_fields[7]),
            "CodFab": spreadsheet_fields[8],
            "IdProduto": spreadsheet_fields[1],
            "Nome": spreadsheet_fields[9],
            "Descricao": spreadsheet_fields[10],
            "Meta": spreadsheet_fields[11],
            "IdCat": spreadsheet_fields[12],
            "NomeCat": spreadsheet_fields[13],
            "IdMarca": spreadsheet_fields[14],
            "Marca": spreadsheet_fields[15],
            "URL": spreadsheet_fields[20],
        }

    def build_vtex_spreadsheet(self) -> DataFrame:
        (
            vtx_nome_sku,
            vtx_sku_ean,
            vtx_altura,
            vtx_largura,
            vtx_comprimento,
            vtx_peso,
            vtx_unidade_medida,
            vtx_mult_unidade,
            vtx_codigo_fabricante,
            vtx_id_produto,
            vtx_descricao_produto,
            vtx_meta_tag_description,
            vtx_id_categoria,
            vtx_nome_categoria,
            vtx_id_marca,
            vtx_marca,
            vtx_condicao_comercial,
            vtx_codigos_lojas,
            vtx_text_link,
        ) = ([] for _ in range(19))

        vtx_sku_id = vtx_codigo_referencia_sku = []
        vtx_titulo_site = vtx_nome_produto = []
        vtx_ativar_sku_se_possivel = vtx_exibe_no_site = vtx_sku_ativo = []
        vtx_exibe_sem_estoque = []

        empty = []
        for key in self.processed_data.keys():
            vtx_sku_id.append(key)
            vtx_nome_sku.append(self.processed_data[key]["NomeSKU"])
            vtx_sku_ean.append(self.processed_data[key]["EAN"])
            vtx_altura.append(self.processed_data[key]["Altura"])
            vtx_largura.append(self.processed_data[key]["Largura"])
            vtx_comprimento.append(
                self.processed_data[key]["Comprimento"]
            )
            vtx_peso.append(self.processed_data[key]["Peso"])
            vtx_codigo_fabricante.append(
                self.processed_data[key]["CodFab"]
            )
            vtx_id_produto.append(
                self.processed_data[key]["IdProduto"]
            )
            vtx_nome_produto.append(self.processed_data[key]["Nome"])
            vtx_descricao_produto.append(
                self.processed_data[key]["Descricao"]
            )
            vtx_meta_tag_description.append(
                self.processed_data[key]["Meta"]
            )
            vtx_id_categoria.append(self.processed_data[key]["IdCat"])
            vtx_nome_categoria.append(
                self.processed_data[key]["NomeCat"]
            )
            vtx_id_marca.append(self.processed_data[key]["IdMarca"])
            vtx_marca.append(self.processed_data[key]["Marca"])
            vtx_exibe_no_site.append("SIM")
            vtx_exibe_sem_estoque.append("NÃO")
            vtx_condicao_comercial.append("Padrão")
            vtx_codigos_lojas.append("1")
            vtx_mult_unidade.append("1")
            vtx_unidade_medida.append("un")
            empty.append("")
            vtx_text_link.append(self.processed_data[key]["URL"])

        self.builded_model = SkuSheet(
            vtx_sku_id,
            vtx_nome_sku,
            vtx_ativar_sku_se_possivel,
            vtx_sku_ativo,
            vtx_sku_ean,
            vtx_altura,
            vtx_largura,
            vtx_comprimento,
            vtx_peso,
            vtx_unidade_medida,
            vtx_mult_unidade,
            vtx_codigo_referencia_sku,
            vtx_codigo_fabricante,
            vtx_id_produto,
            vtx_nome_produto,
            vtx_exibe_no_site,
            vtx_text_link,
            vtx_descricao_produto,
            vtx_titulo_site,
            vtx_meta_tag_description,
            vtx_exibe_sem_estoque,
            vtx_id_categoria,
            vtx_nome_categoria,
            vtx_id_marca,
            vtx_marca,
            vtx_condicao_comercial,
            vtx_codigos_lojas,
        ).spreadsheet
        return self.spreadsheet

    def verifications(self, ids_list: List):
        verify_id(ids_list)


if __name__ == "__main__":
    products_spreadsheet = BuilderSkuSheet(gerar_dataframe(escolher_arquivo()))
    products_spreadsheet.verifications(products_spreadsheet.spreadsheet['id'].values)
    salvar_arquivo_planilha(
        products_spreadsheet.builded_model, products_spreadsheet.filename, "xls"
    )
