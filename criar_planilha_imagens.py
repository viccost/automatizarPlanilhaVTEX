import pandas as pd
from tqdm import tqdm
from salvar_ajustar import escolher_arquivo, gerar_dataframe, salvar_arquivo_planilha

# --------------------- Planilha Imagens
# na hora de integrar vai ser necessário alterar o método chamarPreencherMapaPlanilhaImagens

mapa_planilha_imagens = {}  # deve ser encapsulado de alguma forma
nomeArquivo = "VTEX Imagens built in Python"


def chamar_preencher_mapa_planilha_imagens(planilha: pd.DataFrame):
    """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de imagens,
    chamando o método responsável por preencher o dicionário para estruturar a planilha de imagens."""
    for index, valor in planilha.iloc[:, 0].items():
        preencher_mapa_planilha_imagens(planilha.iloc[index, 0],  # sku
                                        planilha.iloc[index, 20],  # url produto
                                        planilha.iloc[index, 15],  # marca
                                        planilha.iloc[index, 21])  # numImagens
        # alterar esse tipo de identificação de coluna?


def preencher_mapa_planilha_imagens(sku: int, prdUrl: str, marca: str, num_imagens: int):
    """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de imagens"""
    texto_imagens_aux = []
    label_imagens_aux = []
    link_imagem = []
    num_imagens = int(num_imagens)
    caminho_servidor = r"https://images.ferimport.app/Imagens/"
    if num_imagens != 1:
        for n in range(1, num_imagens + 1):
            texto_imagens_aux.append(prdUrl + f"-00{n}")
            if n == 1:
                label_imagens_aux.append("Principal")
            else:
                label_imagens_aux.append(f"00{n}")
            link_imagem.append(caminho_servidor + fr'{marca}/{prdUrl}-00{n}.jpg')
    elif num_imagens == 1:
        texto_imagens_aux.append(prdUrl + f"-001")
        label_imagens_aux.append("Principal")
        link_imagem.append(caminho_servidor + fr'{marca}/{prdUrl}-001.jpg')
    # outras    
    mapa_planilha_imagens[sku] = {"TextoImagem": texto_imagens_aux, "Label": label_imagens_aux,
                                  "Link": link_imagem}


def estruturar_planilha_vtex():
    """Transforma as informações presentes no dicionário de imagens em listas para transformá-las em linhas e alimentar
    o DataFrame."""
    vtx_url, vtx_nome_imagem, vtx_texto_imagem, vtx_label, vtx_id_sku = ([] for _ in range(5))
    vtx_codigoreferencia_sku = vtx_id_sku
    for key in mapa_planilha_imagens.keys():
        vtx_url.extend(str(n) for n in mapa_planilha_imagens[key]['Link'])
        vtx_nome_imagem.extend(str(n) + ".jpg" for n in mapa_planilha_imagens[key]['TextoImagem'])
        vtx_texto_imagem.extend(str(n) for n in mapa_planilha_imagens[key]['TextoImagem'])
        vtx_label.extend(str(n) for n in mapa_planilha_imagens[key]['Label'])
        vtx_id_sku.extend([key] * len(mapa_planilha_imagens[key]['Label']))  # apenas para contar quantas ocorrências
        # da imagem
    data_frame_vtex = pd.DataFrame(
        {'URL': vtx_url, 'NomeImagem': vtx_nome_imagem, 'TextoImagem': vtx_texto_imagem, 'Label': vtx_label,
         'IdSku': vtx_id_sku,
         'CodigoreferenciaSKU': vtx_codigoreferencia_sku})
    url_status = checar_link_imagens(data_frame_vtex)
    data_frame_vtex['Status Imagem'] = url_status
    return data_frame_vtex


def checar_link_imagens(planilhaImagens):
    import requests
    url_status = []
    numero_urls = len(planilhaImagens['URL'])
    with tqdm(total=numero_urls) as barra_progresso:
        for i in range(numero_urls):
            try:
                barra_progresso.update(1)
                url = planilhaImagens['URL'][i]
                statusCode = requests.get(url).status_code
                if 300 > statusCode >= 200:
                    url_status.append("Online")
                else:
                    url_status.append("Offline")
            except requests.exceptions.MissingSchema:
                url_status.append("URL Inválida")
    print()
    return url_status


def iniciar(planilha: pd.DataFrame):
    chamar_preencher_mapa_planilha_imagens(planilha)
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nomeArquivo, 'xls')


if __name__ == '__main__':
    # Seguindo o modelo Python
    chamar_preencher_mapa_planilha_imagens(gerar_dataframe(escolher_arquivo()))
    salvar_arquivo_planilha(estruturar_planilha_vtex(), nomeArquivo, 'xls')
    # Só pra checar a URL
    # planilha_ = gerar_dataframe(escolherA'rquivo())
    # urlStatus_ = checarLinkImagens(planilha_)
    # planilha_['Checar URL'] = urlStatus_
    # salvar_arquivo(planilha_, "Py Imagem Check", 'xls')
