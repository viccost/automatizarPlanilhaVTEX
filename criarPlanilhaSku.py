import pandas as pd
from salvarAjustar import escolherArquivo, gerarDataFrame, salvarArquivo

# --------------------- Planilha Produtos

mapaPlanilhaPlanSKU = {}  # deve ser encapsulado de alguma forma
nomeArquivo = "VTEX Produtos built in Python"


def preencherMapaPlanilhaProdutos(camposPlanilhaUsuario):
    sku = camposPlanilhaUsuario[0]
    mapaPlanilhaPlanSKU[sku] = {"NomeSKU": camposPlanilhaUsuario[1],
                                "EAN": camposPlanilhaUsuario[2], "Altura": camposPlanilhaUsuario[3],
                                "Largura": camposPlanilhaUsuario[4], "Comprimento": camposPlanilhaUsuario[5],
                                "Peso": (camposPlanilhaUsuario[6]), "CodFab": camposPlanilhaUsuario[7],
                                "Nome": camposPlanilhaUsuario[8], "Descricao": camposPlanilhaUsuario[9],
                                "Meta": camposPlanilhaUsuario[10], "IdCat": camposPlanilhaUsuario[11],
                                "NomeCat": camposPlanilhaUsuario[12], "IdMarca": camposPlanilhaUsuario[13],
                                "Marca": camposPlanilhaUsuario[14], "URL": camposPlanilhaUsuario[19]}


def chamarPreencherMapaPlanilhaProdutos(planilha: pd.DataFrame):
    """Responsável por receber um dataframe, percorrer suas linhas, e iniciar o mapeamento da planilha de produtos e
    sku """
    for index, valor in planilha.iloc[:, 0].items():
        preencherMapaPlanilhaProdutos(
            [planilha.iloc[index, n] for n in range(0, 20)])  # mandando uma lista com os campos
        # alterar esse tipo de identificação de coluna


def estruturarPlanilhaVtex():
    vtxNomeSku, vtxSkuEan, vtxAltura, vtxLargura, vtxComprimento, vtxPeso, vtxUnidadeMedida, vtxMultUnidade,\
        vtxCodigoFabricante, vtxDescricaoProduto, vtxMetaTagDescription, vtxIdCategoria, vtxNomeCategoria, vtxIdMarca,\
        vtxMarca, vtxCondicaoComercial, vtxCodigosLojas, vtxTextLink = ([] for cont in range(18))

    vtxSkuId = vtxCodigoReferenciaSKU = []

    vtxTituloSite = vtxNomeProduto = []

    vtxAtivarSkuSePossivel = vtxExibeNoSite = vtxExibeSemEstoque = []
    # vazias
    vtxValorFidelidade = vtxDataPrevisaoChegada = vtxIdProduto = vtxNomeComplemento = vtxProdutoAtivo = \
        vtxDataLancamentoProduto = vtxPalavrasChave = vtxIdFornecedor = vtxKit = vtxIdDepartamento = \
        vtxNomeDepartamento = vtxPesoCubico = vtxAcessorios = vtxSimilares = vtxSugestoes = vtxMostrarJunto \
        = vtxAnexos = vtxPesoReal = vtxComprimentoReal = vtxAlturaReal = vtxLarguraReal = SkuAtivo = \
        vtxCodigoReferenciaProduto = []

    for key in mapaPlanilhaPlanSKU.keys():
        vtxSkuId.append(key)
        vtxNomeSku.append(mapaPlanilhaPlanSKU[key]['NomeSKU'])
        vtxSkuEan.append(mapaPlanilhaPlanSKU[key]['EAN'])
        vtxAltura.append(mapaPlanilhaPlanSKU[key]['Altura'])
        vtxLargura.append(mapaPlanilhaPlanSKU[key]['Largura'])
        vtxComprimento.append(mapaPlanilhaPlanSKU[key]['Comprimento'])
        vtxPeso.append(mapaPlanilhaPlanSKU[key]['Peso'])
        vtxCodigoFabricante.append(mapaPlanilhaPlanSKU[key]['CodFab'])
        vtxNomeProduto.append(mapaPlanilhaPlanSKU[key]['Nome'])
        vtxDescricaoProduto.append(mapaPlanilhaPlanSKU[key]['Descricao'])
        vtxMetaTagDescription.append(mapaPlanilhaPlanSKU[key]['Meta'])
        vtxIdCategoria.append(mapaPlanilhaPlanSKU[key]['IdCat'])
        vtxNomeCategoria.append(mapaPlanilhaPlanSKU[key]['NomeCat'])
        vtxIdMarca.append(mapaPlanilhaPlanSKU[key]['IdMarca'])
        vtxMarca.append(mapaPlanilhaPlanSKU[key]['Marca'])
        vtxExibeNoSite.append("SIM")
        vtxCondicaoComercial.append("Padrão")
        vtxCodigosLojas.append("1")
        vtxMultUnidade.append("1")
        vtxUnidadeMedida.append("un")
        vtxValorFidelidade.append("")
        vtxTextLink.append(mapaPlanilhaPlanSKU[key]['URL'])

    dataFrameVtex = pd.DataFrame({'_SkuId(Não alterável': vtxSkuId, '_NomeSku': vtxNomeSku,
                                  '_AtivarSkuSePossível': vtxAtivarSkuSePossivel,
                                  '_SkuAtivo (Não alterável)': SkuAtivo, '_SkuEan': vtxSkuEan, '_Altura': vtxAltura,
                                  '_AlturaReal': vtxAlturaReal, '_Largura': vtxLargura, '_LarguraReal': vtxLarguraReal,
                                  '_Comprimento':
                                      vtxComprimento, '_ComprimentoReal': vtxComprimentoReal, '_Peso': vtxPeso,
                                  '_PesoReal': vtxPesoReal,
                                  '_UnidadeMedida': vtxUnidadeMedida, '_MultiplicadorUnidade': vtxMultUnidade,
                                  '_CodigoReferenciaSKU':
                                      vtxCodigoReferenciaSKU, '_ValorFidelidade': vtxValorFidelidade,
                                  '_DataPrevisaoChegada':
                                      vtxDataPrevisaoChegada, '_CodigoFabricante': vtxCodigoFabricante,
                                  '_IdProduto (Não alterável)': vtxIdProduto,
                                  '_NomeProduto (Obrigatório)': vtxNomeProduto, '_NomeComplemento': vtxNomeComplemento,
                                  '_ProdutoAtivo (Não alterável)': vtxProdutoAtivo,
                                  '_CodigoReferenciaProduto': vtxCodigoReferenciaProduto,
                                  '_ExibeNoSite': vtxExibeNoSite,
                                  '_TextoLink (Não alterável)':
                                      vtxTextLink, '_DescricaoProduto': vtxDescricaoProduto, '_DataLancamentoProduto':
                                      vtxDataLancamentoProduto, '_PalavrasChave': vtxPalavrasChave,
                                  '_TituloSite': vtxTituloSite,
                                  '_MetaTagDescription': vtxMetaTagDescription, '_IdFornecedor': vtxIdFornecedor,
                                  '_ExibeSemEstoque':
                                      vtxExibeSemEstoque, '_Kit (Não Alterável)': vtxKit,
                                  '_IdDepartamento (Não alterável)':
                                      vtxIdDepartamento, '_NomeDepartamento': vtxNomeDepartamento,
                                  '_IdCategoria': vtxIdCategoria,
                                  '_NomeCategoria': vtxNomeCategoria, '_IdMarca': vtxIdMarca, '_Marca': vtxMarca,
                                  '_PesoCubico': vtxPesoCubico,
                                  '_CondicaoComercial': vtxCondicaoComercial, '_CodigosLojas': vtxCodigosLojas,
                                  '_Acessorios': vtxAcessorios,
                                  '_Similares': vtxSimilares, '_Sugestoes': vtxSugestoes,
                                  'MostrarJunto': vtxMostrarJunto,
                                  '_Anexos': vtxAnexos
                                  })
    return dataFrameVtex


def iniciar(planilha: pd.DataFrame):
    chamarPreencherMapaPlanilhaProdutos(planilha)
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo, 'xls')


if __name__ == '__main__':
    chamarPreencherMapaPlanilhaProdutos(gerarDataFrame(escolherArquivo()))
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo, 'xls')
