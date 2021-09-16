import criarPlanilhaImagem, criarPlanilhaSku, criarPlanilhaEspecificacoes, \
    manipularPlanilhas.salvarAjustar as openAndSave


if __name__ == "__main__":
    planilha = openAndSave.gerarDataFrame(openAndSave.escolherArquivo())
    opcao = int(input("---Escolha---\n"
                      "[0] - Todas\n"
                      "[1] - Produtos e SKU\n"
                      "[2] - Especificações\n"
                      "[3] - Imagens\n"))

    if opcao == 0:
        criarPlanilhaSku.iniciar(planilha)
        criarPlanilhaEspecificacoes.iniciar(planilha)
        criarPlanilhaImagem.iniciar(planilha)
    elif opcao == 1:
        criarPlanilhaSku.iniciar(planilha)
    elif opcao == 2:
        criarPlanilhaEspecificacoes.iniciar(planilha)
    elif opcao == 3:
        criarPlanilhaImagem.iniciar(planilha)
