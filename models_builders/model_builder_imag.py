from pandas import DataFrame
from salvar_ajustar.salvar_ajustar import (
    escolher_arquivo,
    gerar_dataframe,
    salvar_arquivo_planilha,
)
from models.models import ImagesSheet
from models_builders.model_builder import ModelBuilder
from verifications.verifications import verify_image_link


# --------------------- Planilha Imagens


class BuilderImageSheet(ModelBuilder):
    processed_data = {}

    def __init__(self, spreadsheet: DataFrame):
        super().__init__(spreadsheet)
        self.__file_name = "VTEX Imagens built in Python"

    @property
    def filename(self):
        return self.__file_name

    def colect_data(self):
        for index, valor in self.spreadsheet.iloc[:, 0].items():
            self.fill_lists(
                self.spreadsheet.iloc[index, 0],  # sku
                self.spreadsheet.iloc[index, 20],  # url produto
                self.spreadsheet.iloc[index, 15],  # marca
                self.spreadsheet.iloc[index, 21],  # numImagens
            )

    def fill_lists(self, sku: int, prd_url: str, marca: str, num_imagens: int):
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
        self.processed_data[sku] = {
            "TextoImagem": texto_imagens_aux,
            "Label": label_imagens_aux,
            "Link": link_imagem,
        }

    def build_vtex_spreadsheet(self) -> ImagesSheet:
        list_url, list_nome_img, list_texto_img, list_label, list_sku = (
            [] for _ in range(5)
        )
        list_refsku = list_sku
        for key in self.processed_data.keys():
            list_url.extend(
                str(n) for n in self.processed_data[key]["Link"]
            )
            list_nome_img.extend(
                str(n) + ".jpg"
                for n in self.processed_data[key]["TextoImagem"]
            )
            list_texto_img.extend(
                str(n) for n in self.processed_data[key]["TextoImagem"]
            )
            list_label.extend(
                str(n) for n in self.processed_data[key]["Label"]
            )
            list_sku.extend(
                [key] * len(self.processed_data[key]["Label"])
            )  # apenas para contar quantas ocorrências da imagem

        self.builded_model = ImagesSheet(list_url, list_nome_img, list_texto_img,
                                         list_label, list_sku, list_refsku).spreadsheet

        self.verifications()
        return self.builded_model

    def verifications(self) -> None:
        url_status = verify_image_link(self.builded_model['URL'].to_list())
        self.builded_model["Status Imagem"] = url_status


if __name__ == "__main__":
    image_spreadsheet = BuilderImageSheet(gerar_dataframe(escolher_arquivo()))
    salvar_arquivo_planilha(
        image_spreadsheet.builded_model, image_spreadsheet.filename, "xls")
