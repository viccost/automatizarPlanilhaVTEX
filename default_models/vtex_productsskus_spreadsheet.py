from pandas import DataFrame
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from vtex_spreadsheet import VtexSpreadsheet
from verifications.verify_product_id import verify_id
from typing import List


# --------------------- Planilha Produtos


class ProductsSkusSpreadsheet(VtexSpreadsheet):
    productsku_spreadsheet_skeleton = {}  # deve ser encapsulado de alguma forma

    def __init__(self, spreadsheet: DataFrame):
        super().__init__(spreadsheet)
        self.file_name = "VTEX Produtos built in Python"

    def colect_data(self) -> None:
        for index, valor in self.spreadsheet.iloc[:, 0].items():
            self.fill_lists(
                [self.spreadsheet.iloc[index, n] for n in range(0, 21)]
            )  # mandando uma lista com os campos
            # alterar esse tipo de identificação de coluna

    def fill_lists(self, spreadsheet_fields):
        sku = spreadsheet_fields[0]
        self.productsku_spreadsheet_skeleton[sku] = {
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
        ) = ([] for cont in range(19))

        vtx_sku_id = vtx_codigo_referencia_sku = []
        vtx_titulo_site = vtx_nome_produto = []
        vtx_ativar_sku_se_possivel = vtx_exibe_no_site = vtx_sku_ativo = []
        vtx_exibe_sem_estoque = []

        empty = []

        for key in self.productsku_spreadsheet_skeleton.keys():
            vtx_sku_id.append(key)
            vtx_nome_sku.append(self.productsku_spreadsheet_skeleton[key]["NomeSKU"])
            vtx_sku_ean.append(self.productsku_spreadsheet_skeleton[key]["EAN"])
            vtx_altura.append(self.productsku_spreadsheet_skeleton[key]["Altura"])
            vtx_largura.append(self.productsku_spreadsheet_skeleton[key]["Largura"])
            vtx_comprimento.append(
                self.productsku_spreadsheet_skeleton[key]["Comprimento"]
            )
            vtx_peso.append(self.productsku_spreadsheet_skeleton[key]["Peso"])
            vtx_codigo_fabricante.append(
                self.productsku_spreadsheet_skeleton[key]["CodFab"]
            )
            vtx_id_produto.append(
                self.productsku_spreadsheet_skeleton[key]["IdProduto"]
            )
            vtx_nome_produto.append(self.productsku_spreadsheet_skeleton[key]["Nome"])
            vtx_descricao_produto.append(
                self.productsku_spreadsheet_skeleton[key]["Descricao"]
            )
            vtx_meta_tag_description.append(
                self.productsku_spreadsheet_skeleton[key]["Meta"]
            )
            vtx_id_categoria.append(self.productsku_spreadsheet_skeleton[key]["IdCat"])
            vtx_nome_categoria.append(
                self.productsku_spreadsheet_skeleton[key]["NomeCat"]
            )
            vtx_id_marca.append(self.productsku_spreadsheet_skeleton[key]["IdMarca"])
            vtx_marca.append(self.productsku_spreadsheet_skeleton[key]["Marca"])
            vtx_exibe_no_site.append("SIM")
            vtx_exibe_sem_estoque.append("NÃO")
            vtx_condicao_comercial.append("Padrão")
            vtx_codigos_lojas.append("1")
            vtx_mult_unidade.append("1")
            vtx_unidade_medida.append("un")
            empty.append("")
            vtx_text_link.append(self.productsku_spreadsheet_skeleton[key]["URL"])

        data_frame_vtex = DataFrame(
            {
                "_SkuId(Não alterável": vtx_sku_id,
                "_NomeSku": vtx_nome_sku,
                "_AtivarSkuSePossível": vtx_ativar_sku_se_possivel,
                "_SkuAtivo (Não alterável)": vtx_sku_ativo,
                "_SkuEan": vtx_sku_ean,
                "_Altura": vtx_altura,
                "_AlturaReal": empty,
                "_Largura": vtx_largura,
                "_LarguraReal": empty,
                "_Comprimento": vtx_comprimento,
                "_ComprimentoReal": empty,
                "_Peso": vtx_peso,
                "_PesoReal": empty,
                "_UnidadeMedida": vtx_unidade_medida,
                "_MultiplicadorUnidade": vtx_mult_unidade,
                "_CodigoReferenciaSKU": vtx_codigo_referencia_sku,
                "_ValorFidelidade": empty,
                "_DataPrevisaoChegada": empty,
                "_CodigoFabricante": vtx_codigo_fabricante,
                "_IdProduto (Não alterável)": vtx_id_produto,
                "_NomeProduto (Obrigatório)": vtx_nome_produto,
                "_NomeComplemento": empty,
                "_ProdutoAtivo (Não alterável)": empty,
                "_CodigoReferenciaProduto": empty,
                "_ExibeNoSite": vtx_exibe_no_site,
                "_TextoLink (Não alterável)": vtx_text_link,
                "_DescricaoProduto": vtx_descricao_produto,
                "_DataLancamentoProduto": empty,
                "_PalavrasChave": empty,
                "_TituloSite": vtx_titulo_site,
                "_MetaTagDescription": vtx_meta_tag_description,
                "_IdFornecedor": empty,
                "_ExibeSemEstoque": vtx_exibe_sem_estoque,
                "_Kit (Não Alterável)": empty,
                "_IdDepartamento (Não alterável)": empty,
                "_NomeDepartamento": empty,
                "_IdCategoria": vtx_id_categoria,
                "_NomeCategoria": vtx_nome_categoria,
                "_IdMarca": vtx_id_marca,
                "_Marca": vtx_marca,
                "_PesoCubico": empty,
                "_CondicaoComercial": vtx_condicao_comercial,
                "_CodigosLojas": vtx_codigos_lojas,
                "_Acessorios": empty,
                "_Similares": empty,
                "_Sugestoes": empty,
                "MostrarJunto": empty,
                "_Anexos": empty,
            }
        )
        return data_frame_vtex

    def verifications(self, ids_list: List):
        verify_id(ids_list)


if __name__ == "__main__":
    products_spreadsheet = ProductsSkusSpreadsheet(gerar_dataframe(escolher_arquivo()))
    df: DataFrame = products_spreadsheet.init_process()[1]
    teste = products_spreadsheet.spreadsheet
    products_spreadsheet.verifications(products_spreadsheet.spreadsheet['id'].values)
    salvar_arquivo_planilha(
        df, products_spreadsheet.file_name, "xls"
    )
