"""The purpose of this app is to optimize the register of new products on VTEX.
    A default plataform's spreadsheet was used as base to create a new one, in the folder planilhapadrão,

    It's possible
    Written by Victor Costa (victorcost_@outlook.com).
    v1.0"""

from models_builders.model_builder_skus import BuilderSkuSheet
from models_builders.model_builder_imag import BuilderImageSheet
from models_builders.model_builder_spec import BuilderSpecSheet

import salvar_ajustar.salvar_ajustar as sv

if __name__ == "__main__":
    planilha = sv.gerar_dataframe(sv.escolher_arquivo())
    list_to_save = []
    dict_to_save = dict()
    models = [BuilderSkuSheet, BuilderSpecSheet, BuilderImageSheet]
    for model in models:
        df = model(planilha)
        file_name = df.filename
        spreadsheet = df.builded_model
        dict_to_save = {"Nome": file_name, "Dataframe": spreadsheet}
        list_to_save.append(dict_to_save.copy())

    sv.salvar_planilhas(list_to_save)
