import pandas as pd
from salvarAjustar import escolherArquivo, gerarDataFrame, salvarArquivo

# --------------------- Planilha Imagens
# na hora de integrar vai ser necessário alterar o método chamarPreencherMapaPlanilhaImagens

mapaPlanilhaImagens = {}  # deve ser encapsulado de alguma forma
nomeArquivo = "VTEX Imagens built in Python"


def preencherMapaPlanilhaImagens(sku: int, prdUrl: str, marca: str, numImagens: int):
    """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de imagens"""
    textoImagensAux = []
    labelImagensAux = []
    linkImagem = []
    numImagens = int(numImagens)
    caminhoServidor = r"https://images.ferimport.app/Imagens/"
    if numImagens != 1:
        for n in range(1, numImagens + 1):
            textoImagensAux.append(prdUrl + f"-00{n}")
            if n == 1:
                labelImagensAux.append("Principal")
            else:
                labelImagensAux.append(f"00{n}")
            linkImagem.append(caminhoServidor + fr'{marca}/{prdUrl}-00{n}.jpg')
    elif numImagens == 1:
        textoImagensAux.append(prdUrl + f"-001")
        labelImagensAux.append("Principal")
        linkImagem.append(caminhoServidor + fr'{marca}/{prdUrl}-001.jpg')
    # outras    
    mapaPlanilhaImagens[sku] = {"TextoImagem": textoImagensAux, "Label": labelImagensAux,
                                "Link": linkImagem}


def chamarPreencherMapaPlanilhaImagens(planilha: pd.DataFrame):
    """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de imagens,
    chamando o método responsável por preencher o dicionário para estruturar a planilha de imagens."""
    for index, valor in planilha.iloc[:, 0].items():
        preencherMapaPlanilhaImagens(planilha.iloc[index, 0],  # url
                                     planilha.iloc[index, 20],  # prdUrl
                                     planilha.iloc[index, 14],  # marca
                                     planilha.iloc[index, 21])  # numImagens
        # alterar esse tipo de identificação de coluna?


def estruturarPlanilhaVtex():
    """Transforma as informações presentes no dicionário de imagens em listas para transformá-las em linhas e alimentar
    o DataFrame."""
    vtxURL, vtxNomeImagem, vtxTextoImagem, vtxLabel, vtxIdSKU = ([] for i in range(5))
    vtxCodigoreferenciaSKU = vtxIdSKU
    for key in mapaPlanilhaImagens.keys():
        vtxURL.extend(str(n) for n in mapaPlanilhaImagens[key]['Link'])
        vtxNomeImagem.extend(str(n) + ".jpg" for n in mapaPlanilhaImagens[key]['TextoImagem'])
        vtxTextoImagem.extend(str(n) for n in mapaPlanilhaImagens[key]['TextoImagem'])
        vtxLabel.extend(str(n) for n in mapaPlanilhaImagens[key]['Label'])
        vtxIdSKU.extend([key] * len(mapaPlanilhaImagens[key]['Label']))  # apenas para contar quantas ocorrências
        # da imagem
    dataFrameVTEX = pd.DataFrame(
        {'URL': vtxURL, 'NomeImagem': vtxNomeImagem, 'TextoImagem': vtxTextoImagem, 'Label': vtxLabel,
         'IdSku': vtxIdSKU,
         'CodigoreferenciaSKU': vtxCodigoreferenciaSKU})
    return dataFrameVTEX


def iniciar(planilha: pd.DataFrame):
    chamarPreencherMapaPlanilhaImagens(planilha)
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo)


if __name__ == '__main__':
    chamarPreencherMapaPlanilhaImagens(gerarDataFrame(escolherArquivo()))
    salvarArquivo(estruturarPlanilhaVtex(), nomeArquivo)
