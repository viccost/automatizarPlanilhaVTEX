import pandas as pd
from tqdm import tqdm
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from vtex_spreadsheet import VtexSpreadsheet
import requests


# --------------------- Planilha Imagens


class ImagesSpreadsheet(VtexSpreadsheet):
    images_spreadsheet_skeleton = {}

    def __init__(self, spreadsheet: pd.DataFrame):
        super().__init__(spreadsheet)
        self.file_name = "VTEX Imagens built in Python"

    def colect_data(self):
        """Essa função recebe um DataFrame e percorre as suas linhas, iniciando o mapeamento da planilha de imagens,
        chamando o método responsável por preencher o dicionário para estruturar a planilha de imagens."""
        for index, valor in self.spreadsheet.iloc[:, 0].items():
            self.fill_lists(
                self.spreadsheet.iloc[index, 0],  # sku
                self.spreadsheet.iloc[index, 20],  # url produto
                self.spreadsheet.iloc[index, 15],  # marca
                self.spreadsheet.iloc[index, 21],  # numImagens
            )
            # alterar esse tipo de identificação de coluna?

    def fill_lists(self, sku: int, prd_url: str, marca: str, num_imagens: int):
        """Cria um dicionário com SKU como chave, com os campos necessários para o preenchimento da planilha de
        imagens"""
        texto_imagens_aux = []
        label_imagens_aux = []
        link_imagem = []
        num_imagens = int(num_imagens)
        caminho_servidor = r"https://images.ferimport.app/Imagens/"
        if num_imagens != 1:
            for n in range(1, num_imagens + 1):
                texto_imagens_aux.append(prd_url + f"-00{n}")
                if n == 1:
                    label_imagens_aux.append("Principal")
                else:
                    label_imagens_aux.append(f"00{n}")
                link_imagem.append(caminho_servidor + fr"{marca}/{prd_url}-00{n}.jpg")
        elif num_imagens == 1:
            texto_imagens_aux.append(prd_url + f"-001")
            label_imagens_aux.append("Principal")
            link_imagem.append(caminho_servidor + fr"{marca}/{prd_url}-001.jpg")
        # outras
        self.images_spreadsheet_skeleton[sku] = {
            "TextoImagem": texto_imagens_aux,
            "Label": label_imagens_aux,
            "Link": link_imagem,
        }

    def build_vtex_spreadsheet(self):
        """Transforma as informações presentes no dicionário de imagens em listas para transformá-las em linhas e alimentar
        o DataFrame."""
        vtx_url, vtx_nome_imagem, vtx_texto_imagem, vtx_label, vtx_id_sku = (
            [] for _ in range(5)
        )
        vtx_codigoreferencia_sku = vtx_id_sku
        for key in self.images_spreadsheet_skeleton.keys():
            vtx_url.extend(
                str(n) for n in self.images_spreadsheet_skeleton[key]["Link"]
            )
            vtx_nome_imagem.extend(
                str(n) + ".jpg"
                for n in self.images_spreadsheet_skeleton[key]["TextoImagem"]
            )
            vtx_texto_imagem.extend(
                str(n) for n in self.images_spreadsheet_skeleton[key]["TextoImagem"]
            )
            vtx_label.extend(
                str(n) for n in self.images_spreadsheet_skeleton[key]["Label"]
            )
            vtx_id_sku.extend(
                [key] * len(self.images_spreadsheet_skeleton[key]["Label"])
            )  # apenas para contar quantas ocorrências da imagem

        dataframe_vtex = pd.DataFrame(
            {
                "URL": vtx_url,
                "NomeImagem": vtx_nome_imagem,
                "TextoImagem": vtx_texto_imagem,
                "Label": vtx_label,
                "IdSku": vtx_id_sku,
                "CodigoreferenciaSKU": vtx_codigoreferencia_sku,
            }
        )
        url_status = self.check_links(dataframe_vtex["URL"].tolist())
        dataframe_vtex["Status Imagem"] = url_status
        return dataframe_vtex

    @staticmethod
    def check_links(urls: list) -> list:
        url_status = []
        numero_urls = len(urls)
        print("Verificando links das imagens...")

        with tqdm(total=numero_urls) as barra_progresso:
            for i in range(numero_urls):
                try:
                    barra_progresso.update(1)
                    url = urls[i]
                    statusCode = requests.get(url).status_code
                    if 300 > statusCode >= 200:
                        url_status.append("Online")
                    else:
                        url_status.append("Offline")
                except requests.exceptions.MissingSchema:
                    url_status.append("URL Inválida")
        print()
        return url_status


if __name__ == "__main__":
    images_spreadsheet = ImagesSpreadsheet(gerar_dataframe(escolher_arquivo()))
    images_spreadsheet.init_process()
