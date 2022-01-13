import pandas as pd
from salvar_ajustar import escolher_arquivo, gerar_dataframe, salvar_arquivo_planilha

# --------------------- Planilha Produtos

mapa_planilha_plan_sku = {}  # deve ser encapsulado de alguma forma
nome_arquivo = "VTEX Produtos built in Python"


def chamar_preencher_mapa_planilha_produtos(planilha: pd.DataFrame) -> None:
    """Responsável por receber um dataframe, percorrer suas linhas, e iniciar o mapeamento da planilha de produtos e
    sku """
    for index, valor in planilha.iloc[:, 0].items():
        preencher_mapa_planilha_produtos(
            [planilha.iloc[index, n] for n in range(0, 21)])  # mandando uma lista com os campos
        # alterar esse tipo de identificação de coluna


def preencher_mapa_planilha_produtos(campos_planilha_usuario) -> pd.DataFrame:
    """Define quais as colunas serão utilizadas para preencher o dicionário de cada produto, e seus respectivos
    atributos."""
    sku = campos_planilha_usuario[0]
    mapa_planilha_plan_sku[sku] = {"NomeSKU": campos_planilha_usuario[2],
                                    "EAN": campos_planilha_usuario[3], "Altura": campos_planilha_usuario[4],
                                    "Largura": campos_planilha_usuario[5], "Comprimento": campos_planilha_usuario[6],
                                    "Peso": (campos_planilha_usuario[7]), "CodFab": campos_planilha_usuario[8],
                                    "Nome": campos_planilha_usuario[9], "Descricao": campos_planilha_usuario[10],
                                    "Meta": campos_planilha_usuario[11], "IdCat": campos_planilha_usuario[12],
                                    "NomeCat": campos_planilha_usuario[13], "IdMarca": campos_planilha_usuario[14],
                                    "Marca": campos_planilha_usuario[15], "URL": campos_planilha_usuario[20]}


def estruturar_planilha_vtex() -> pd.DataFrame:
    vtx_nome_sku, vtx_sku_ean, vtx_altura, vtx_largura, vtx_comprimento, vtx_peso, vtx_unidade_medida, \
        vtx_mult_unidade, vtx_codigo_fabricante, vtx_descricao_produto, vtx_meta_tag_description, vtx_id_categoria, \
        vtx_nome_categoria, vtx_id_marca, vtx_marca, vtx_condicao_comercial, vtx_codigos_lojas, vtx_text_link = \
        ([] for cont in range(18))

    vtx_sku_id = vtx_codigo_referencia_sku = []

    vtx_titulo_site = vtx_nome_produto = []

    vtx_ativar_sku_se_possivel = vtx_exibe_no_site = vtx_exibe_sem_estoque = []
    # vazias
    vtx_valor_fidelidade = vtx_data_previsao_chegada = vtx_nome_complemento = vtx_produto_ativo = \
        vtx_data_lancamento_produto = vtx_palavras_chave = vtx_id_fornecedor = vtx_kit = vtx_id_departamento = \
        vtx_nome_departamento = vtx_peso_cubico = vtx_acessorios = vtx_similares = vtx_sugestoes = vtx_mostrar_junto \
        = vtx_anexos = vtx_peso_real = vtx_comprimento_real = vtx_altura_real = vtx_largura_real = sku_ativo = \
        vtx_codigo_referencia_produto = vtx_id_produto = []

    for key in mapa_planilha_plan_sku.keys():
        vtx_sku_id.append(key)
        vtx_nome_sku.append(mapa_planilha_plan_sku[key]['NomeSKU'])
        vtx_sku_ean.append(mapa_planilha_plan_sku[key]['EAN'])
        vtx_altura.append(mapa_planilha_plan_sku[key]['Altura'])
        vtx_largura.append(mapa_planilha_plan_sku[key]['Largura'])
        vtx_comprimento.append(mapa_planilha_plan_sku[key]['Comprimento'])
        vtx_peso.append(mapa_planilha_plan_sku[key]['Peso'])
        vtx_codigo_fabricante.append(mapa_planilha_plan_sku[key]['CodFab'])
        vtx_nome_produto.append(mapa_planilha_plan_sku[key]['Nome'])
        vtx_descricao_produto.append(mapa_planilha_plan_sku[key]['Descricao'])
        vtx_meta_tag_description.append(mapa_planilha_plan_sku[key]['Meta'])
        vtx_id_categoria.append(mapa_planilha_plan_sku[key]['IdCat'])
        vtx_nome_categoria.append(mapa_planilha_plan_sku[key]['NomeCat'])
        vtx_id_marca.append(mapa_planilha_plan_sku[key]['IdMarca'])
        vtx_marca.append(mapa_planilha_plan_sku[key]['Marca'])
        vtx_exibe_no_site.append("SIM")
        vtx_condicao_comercial.append("Padrão")
        vtx_codigos_lojas.append("1")
        vtx_mult_unidade.append("1")
        vtx_unidade_medida.append("un")
        vtx_valor_fidelidade.append("")
        vtx_text_link.append(mapa_planilha_plan_sku[key]['URL'])

    data_frame_vtex = pd.DataFrame({'_SkuId(Não alterável': vtx_sku_id, '_NomeSku': vtx_nome_sku,
                                    '_AtivarSkuSePossível': vtx_ativar_sku_se_possivel,
                                    '_SkuAtivo (Não alterável)': sku_ativo, '_SkuEan': vtx_sku_ean,
                                    '_Altura': vtx_altura,
                                    '_AlturaReal': vtx_altura_real, '_Largura': vtx_largura,
                                    '_LarguraReal': vtx_largura_real,
                                    '_Comprimento':
                                        vtx_comprimento, '_ComprimentoReal': vtx_comprimento_real, '_Peso': vtx_peso,
                                    '_PesoReal': vtx_peso_real,
                                    '_UnidadeMedida': vtx_unidade_medida, '_MultiplicadorUnidade': vtx_mult_unidade,
                                    '_CodigoReferenciaSKU':
                                        vtx_codigo_referencia_sku, '_ValorFidelidade': vtx_valor_fidelidade,
                                    '_DataPrevisaoChegada':
                                        vtx_data_previsao_chegada, '_CodigoFabricante': vtx_codigo_fabricante,
                                    '_IdProduto (Não alterável)': vtx_id_produto,
                                    '_NomeProduto (Obrigatório)': vtx_nome_produto,
                                    '_NomeComplemento': vtx_nome_complemento,
                                    '_ProdutoAtivo (Não alterável)': vtx_produto_ativo,
                                    '_CodigoReferenciaProduto': vtx_codigo_referencia_produto,
                                    '_ExibeNoSite': vtx_exibe_no_site,
                                    '_TextoLink (Não alterável)':
                                        vtx_text_link, '_DescricaoProduto': vtx_descricao_produto,
                                    '_DataLancamentoProduto':
                                        vtx_data_lancamento_produto, '_PalavrasChave': vtx_palavras_chave,
                                    '_TituloSite': vtx_titulo_site,
                                    '_MetaTagDescription': vtx_meta_tag_description, '_IdFornecedor': vtx_id_fornecedor,
                                    '_ExibeSemEstoque':
                                        vtx_exibe_sem_estoque, '_Kit (Não Alterável)': vtx_kit,
                                    '_IdDepartamento (Não alterável)':
                                        vtx_id_departamento, '_NomeDepartamento': vtx_nome_departamento,
                                    '_IdCategoria': vtx_id_categoria,
                                    '_NomeCategoria': vtx_nome_categoria, '_IdMarca': vtx_id_marca, '_Marca': vtx_marca,
                                    '_PesoCubico': vtx_peso_cubico,
                                    '_CondicaoComercial': vtx_condicao_comercial, '_CodigosLojas': vtx_codigos_lojas,
                                    '_Acessorios': vtx_acessorios,
                                    '_Similares': vtx_similares, '_Sugestoes': vtx_sugestoes,
                                    'MostrarJunto': vtx_mostrar_junto,
                                    '_Anexos': vtx_anexos
                                    })
    return data_frame_vtex


def iniciar(planilha: pd.DataFrame):
    chamar_preencher_mapa_planilha_produtos(planilha)
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nome_arquivo, 'xls')


if __name__ == '__main__':
    chamar_preencher_mapa_planilha_produtos(gerar_dataframe(escolher_arquivo()))
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nome_arquivo, 'xls')
