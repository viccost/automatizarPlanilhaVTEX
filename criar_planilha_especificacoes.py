import pandas as pd
from salvar_ajustar import escolher_arquivo, gerar_dataframe, salvar_arquivo_planilha

# --------------------- Planilha Especificações

mapa_planilha_especificacao = {}
nome_arquivo = "VTEX Espec built in Python"


def chamar_preencher_mapa_planilha_especificacoes(planilha: pd.DataFrame) -> None:
    """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de especificações,
    chamando o método responsável por preencher o dicionário para estruturar a planilha de especificações."""
    try:
        # utilizando o iloc para poder naver pelas linhas e colunas
        for index, valor in planilha.iloc[:, 0].items():
            # percorrendo todas as linhas
            preencher_mapa_planilha_especificacoes(planilha.iloc[index, 0], planilha.iloc[index, 1],
                                                   planilha.iloc[index, 9],
                                                   planilha.iloc[index, 16], planilha.iloc[index, 17],
                                                   planilha.iloc[index, 18],
                                                   planilha.iloc[index, 19])
            # alterar esse tipo de identificação de coluna
    except IndexError:
        print("Cheque se a sua planilha tem todas as colunas necessárias!")
        exit()


def preencher_mapa_planilha_especificacoes(sku: int, id: int, nomePrd: str, infTec: str, infFor: str, descPrd: str,
                                           videoPrd: str) -> None:
    """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de imagens"""
    infos = list()
    if str(infTec) != 'nan':
        infos.append(['51', infTec, 'Informações Técnicas'])
    if str(infFor) != 'nan':
        infos.append(['52', infFor, 'Informações do Fornecedor'])
    if str(descPrd) != 'nan':
        infos.append(['53', descPrd, 'Descrição do Produto'])
    if str(videoPrd) != 'nan':
        infos.append(['53', videoPrd, 'Vídeo do Produto'])

    mapa_planilha_especificacao[sku] = {'Nome Produto': nomePrd, 'Informações': infos, 'IdProduto': id}


def estruturar_planilha_vtex() -> pd.DataFrame:
    id_campo_valor = nome_campo_valor = codigo_referencia_produto = []
    nome_campo, sku_procx, id_produto, nome_produto, id_campo, valor_especificacao, nome_tipo_campo, \
        codigo_especificacao = ([] for i in range(8))
    for key in mapa_planilha_especificacao.keys():
        linhas_desse_id = len(mapa_planilha_especificacao[key]['Informações'])
        id_produto.extend([mapa_planilha_especificacao[key]['IdProduto']] * linhas_desse_id)
        nome_produto.extend([mapa_planilha_especificacao[key]['Nome Produto']] * linhas_desse_id)
        for valor in mapa_planilha_especificacao[key]['Informações']:
            id_campo.append(valor[0])
            nome_campo.append(valor[2])
            valor_especificacao.append(valor[1])
            nome_tipo_campo.append("Texto Grande")
    planilha_vtex = {'_IdProduto (Não alterável)': id_produto,
                     '_NomeProduto (Não alterável)': nome_produto,
                     'IdCampo (Não alterável)': id_campo,
                     'NomeCampo (Não alterável)': nome_campo,
                     'NomeTipoCampo (Não alterável)': nome_tipo_campo,
                     'IdCampoValor (Não alterável)': id_campo_valor,
                     'NomeCampoValor (Não alterável)': nome_campo_valor,
                     'CodigoEspecificacao (Não alterável)': codigo_especificacao,
                     'ValorEspecificacao': valor_especificacao,
                     '_CodigoReferenciaProduto (Não alterável)': codigo_referencia_produto}
    dataframe_vtex = pd.DataFrame.from_dict(planilha_vtex, orient='index')
    dataframe_vtex = dataframe_vtex.transpose()
    return dataframe_vtex


def iniciar(planilha: pd.DataFrame) -> None:
    chamar_preencher_mapa_planilha_especificacoes(planilha)
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nome_arquivo, 'xls', formatar=False)


if __name__ == '__main__':
    chamar_preencher_mapa_planilha_especificacoes(gerar_dataframe(escolher_arquivo()))
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nome_arquivo, 'xls')
