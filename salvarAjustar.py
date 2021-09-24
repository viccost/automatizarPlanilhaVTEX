import pandas as pd
import xlsxwriter


def escolherArquivo():
    """Abre uma janela para que o usuário possa escolher QUALQUER ARQUIVO."""
    import tkinter as tk
    from tkinter import filedialog
    # Talvez setar os formatos específicos seja uma bom upgrade.
    root = tk.Tk()
    root.attributes('-topmost', 1)
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path == '':
        print("Encerrando")
        return exit()
    return file_path


def escolherPasta():
    """Abre uma janela para que o usuário possa escolher QUALQUER ARQUIVO."""
    import tkinter as tk
    from tkinter import filedialog
    # Talvez setar os formatos específicos seja uma bom upgrade.
    root = tk.Tk()
    root.attributes('-topmost', 1)
    root.withdraw()
    folderPath = filedialog.askdirectory()
    if folderPath == '':
        print("Encerrando")
        return exit()
    return folderPath


def gerarDataFrame(file_path):
    """Espera um arquivo .xls, .xlsx, .csv para converter para um pandas.DataFrame e retorná-lo"""
    # checar tipo do arquivo ou trycatch para tratar erros
    planilha = pd.read_excel(file_path)
    return planilha


def salvarArquivo(planilha: pd.DataFrame, nome: str, formato: str, formatar=True):
    """Recebe um DataFrame e nome do arquivo para salvá-lo como .xlsx. Ajusta automaticamente o tamanho das colunas.
    Index do DataFrame está setado como falso. E os campos em branco estão mantidos em branco sem alteração."""
    caminhoDesktop = r'C:\Users\Victor\Desktop'

    def checarCaminho():
        from os import path
        if path.exists(caminhoDesktop):
            pass
        else:
            print("Erro: Defina corretamente o caminho até a pasta que deseja salvar suas planilhas!\n"
                  "Encerrando.")
            exit()

    checarCaminho()

    if formato == "xls":
        engine = "xlwt"
        formatar = False
    else:
        formato = "xlsx"
        engine = "xlsxwriter"
    writer = pd.ExcelWriter(rf'{caminhoDesktop}\{nome}.{formato}', engine=f'{engine}')

    # engine_kwargs={'options': {'strings_to_numbers': True}})

    def ajustarColunas():
        for column in planilha:
            column_width = max(planilha[column].astype(str).map(len).max(), len(column))
            col_idx = planilha.columns.get_loc(column)
            writer.sheets[f'{nome}'].set_column(col_idx, col_idx, column_width)

    planilha.to_excel(writer, sheet_name=f'{nome}', index=False)

    if formatar:
        ajustarColunas()

    # com engine_kwargs ele automaticamente protege a planilha inteira, setando pra modo leitura
    # verificar como desativar isso

    try:
        writer.save()
        print(f'A planilha "{nome}" foi criada!')
    except Exception as err:
        print(f"Erro ao salvar o arquivo: {err}")
        exit()


'''  def setarTipo():
 workbook = writer.book
 worksheet = writer.sheets[f'{nome}']
 # https: // xlsxwriter.readthedocs.io / tutorial03.html
 # https://xlsxwriter.readthedocs.io/working_with_pandas.html '''
