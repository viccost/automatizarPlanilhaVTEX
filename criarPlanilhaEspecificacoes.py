import pandas as pd
from manipularPlanilhas.salvarAjustar import escolherArquivo, gerarDataFrame, salvarArquivo

# --------------------- Planilha Especificações

mapaPlanilhaEspec = {}
nomeArquivo = "VTEX Espec built in Python"


def preencherMapaPlanilhaEspecificacoes(sku: int, nomePrd: str, infPrd: str, infTec: str, infFor: str, descPrd: str,
                                        videoPrd: str):
    """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de imagens"""
    infos = list()
    if str(infPrd) != 'nan':
        infos.append(['50', infPrd, 'Informações do Produto'])
    if str(infTec) != 'nan':
        infos.append(['51', infTec, 'Informações Técnicas'])
    if str(infFor) != 'nan':
        infos.append(['52', infFor, 'Informações do Fornecedor'])
    if str(descPrd) != 'nan':
        infos.append(['53', descPrd, 'Descrição do Produto'])
    if str(videoPrd) != 'nan':
        infos.append(['53', videoPrd, 'Vídeo do Produto'])

    mapaPlanilhaEspec[sku] = {'Nome Produto': nomePrd, 'Informações': infos}


def chamarPreencherMapaPlanilhaEspecificacoes(planilha: pd.DataFrame):
    """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de especificações,
    chamando o método responsável por preencher o dicionário para estruturar a planilha de especificações."""
    try:
        for index, valor in planilha.iloc[:, 0].items():
            preencherMapaPlanilhaEspecificacoes(planilha.iloc[index, 0], planilha.iloc[index, 8],
                                                planilha.iloc[index, 15],
                                                planilha.iloc[index, 16], planilha.iloc[index, 17],
                                                planilha.iloc[index, 18],
                                                planilha.iloc[index, 19])
            # alterar esse tipo de identificação de coluna
    except IndexError:
        print("Cheque se a sua planilha tem todas as colunas necessárias!")
        exit()


def estruturarPlanilhaVtex():
    IdCampoValor = NomeCampoValor = _CodigoReferenciaProduto = []
    NomeCampo, SKU_Procx, _IdProduto, _NomeProduto, IdCampo, ValorEspecificacao, NomeTipoCampo, CodigoEspecificacao = \
        ([] for i in range(8))
    for key in mapaPlanilhaEspec.keys():
        linhasSKU = len(mapaPlanilhaEspec[key]['Informações'])
        SKU_Procx.extend([key] * linhasSKU)
        _NomeProduto.extend([mapaPlanilhaEspec[key]['Nome Produto']] * linhasSKU)
        for valor in mapaPlanilhaEspec[key]['Informações']:
            IdCampo.append(valor[0])
            NomeCampo.append(valor[2])
            ValorEspecificacao.append(valor[1])
            NomeTipoCampo.append("Texto Grande")
    planilhaVTEX = {'PROCX': SKU_Procx,
                    '_IdProduto (Não alterável)': _IdProduto,
                    '_NomeProduto (Não alterável)': _NomeProduto,
                    'IdCampo (Não alterável)': IdCampo,
                    'NomeCampo (Não alterável)': NomeCampo,
                    'NomeTipoCampo (Não alterável)': NomeTipoCampo,
                    'IdCampoValor (Não alterável)': IdCampoValor,
                    'NomeCampoValor (Não alterável)': NomeCampoValor,
                    'CodigoEspecificacao (Não alterável)': CodigoEspecificacao,
                    'ValorEspecificacao': ValorEspecificacao,
                    '_CodigoReferenciaProduto (Não alterável)': _CodigoReferenciaProduto}
    dataFrameVTEX = pd.DataFrame.from_dict(planilhaVTEX, orient='index')
    dataFrameVTEX = dataFrameVTEX.transpose()
    return dataFrameVTEX


def iniciar(planilha: pd.DataFrame):
    chamarPreencherMapaPlanilhaEspecificacoes(planilha)
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo, formatar=False)


if __name__ == '__main__':
    chamarPreencherMapaPlanilhaEspecificacoes(gerarDataFrame(escolherArquivo()))
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo)
