import criar_planilha_especificacoes
import criar_planilha_imagens
import criar_planilha_sku
import salvar_ajustar as open_and_save

if __name__ == "__main__":
    planilha = open_and_save.gerar_dataframe(open_and_save.escolher_arquivo())
    criar_planilha_sku.iniciar(planilha)
    criar_planilha_especificacoes.iniciar(planilha)
    criar_planilha_imagens.iniciar(planilha)

