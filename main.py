"""The purpose of this app is to optimize the register of new products on VTEX.
    A default plataform's spreadsheet was used as base to create a new one, in the folder planilhapadrão,

    It's possible
    Written by Victor Costa (victorcost_@outlook.com).
    v1.0"""

from default_models.vtex_specification_spreadsheet import SpecificationSpreadsheet
from default_models.vtex_images_spreadsheet import ImagesSpreadsheet
from default_models.vtex_productsskus_spreadsheet import ProductsSkusSpreadsheet
import salvar_ajustar.salvar_ajustar as sv

if __name__ == "__main__":
    planilha = sv.gerar_dataframe(sv.escolher_arquivo())
    list_to_save = []
    dict_to_save = dict()
    models = [ProductsSkusSpreadsheet, SpecificationSpreadsheet, ImagesSpreadsheet]
    for model in models:
        file_name, spreadsheet = model(planilha).init_process()
        dict_to_save["Nome"] = file_name
        dict_to_save["Dataframe"] = spreadsheet
        list_to_save.append(dict_to_save.copy())

    sv.salvar_planilhas(list_to_save)
