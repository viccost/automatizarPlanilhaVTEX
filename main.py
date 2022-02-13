from vtex_specification_spreadsheet import SpecificationSpreadsheet
from vtex_images_spreadsheet import ImagesSpreadsheet
from vtex_productsskus_spreadsheet import ProductsSkusSpreadsheet
import salvar_ajustar.salvar_ajustar as open_and_save

if __name__ == "__main__":
    planilha = open_and_save.gerar_dataframe(open_and_save.escolher_arquivo())
    list_to_save = []
    dict_to_save = dict()
    models = [ProductsSkusSpreadsheet, SpecificationSpreadsheet, ImagesSpreadsheet]
    for model in models:
        file_name, spreadsheet = model(planilha).init_process()
        dict_to_save["Nome"] = file_name
        dict_to_save["Dataframe"] = spreadsheet
        list_to_save.append(dict_to_save.copy())

    open_and_save.salvar_planilhas(list_to_save)
