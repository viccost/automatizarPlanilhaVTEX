import criarPlanilhaImagem, criarPlanilhaSku, criarPlanilhaEspecificacoes, \
    salvarAjustar as openAndSave


if __name__ == "__main__":
    planilha = openAndSave.gerarDataFrame(openAndSave.escolherArquivo())
    criarPlanilhaSku.iniciar(planilha)
    criarPlanilhaEspecificacoes.iniciar(planilha)
    criarPlanilhaImagem.iniciar(planilha)

