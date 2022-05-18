import pandas as pd


class ImagesSheet:

    def __init__(self, list_url, list_nome_imagem, list_texto_imagem, list_label, list_sku, list_ref_sku):
        self._spreadsheet = pd.DataFrame.from_dict(
            {
                "URL": list_url,
                "NomeImagem": list_nome_imagem,
                "TextoImagem": list_texto_imagem,
                "Label": list_label,
                "IdSku": list_sku,
                "CodigoreferenciaSKU": list_ref_sku,
            }, orient='index'
        )
        self._spreadsheet = self._spreadsheet.transpose()

    @property
    def spreadsheet(self):
        return self._spreadsheet


class SpecSheet:

    def __init__(self, list_id, list_nomeprd, list_idcampo, list_nomecampo, list_nometipocampo, list_idcampovalor,
                 list_nomecampovalor,
                 list_codigoespc, list_valorespec, list_codref):
        self._spreadsheet = pd.DataFrame.from_dict(
            {
                "_IdProduto (Não alterável)": list_id,
                "_NomeProduto (Não alterável)": list_nomeprd,
                "IdCampo (Não alterável)": list_idcampo,
                "NomeCampo (Não alterável)": list_nomecampo,
                "NomeTipoCampo (Não alterável)": list_nometipocampo,
                "IdCampoValor (Não alterável)": list_idcampovalor,
                "NomeCampoValor (Não alterável)": list_nomecampovalor,
                "CodigoEspecificacao (Não alterável)": list_codigoespc,
                "ValorEspecificacao": list_valorespec,
                "_CodigoReferenciaProduto (Não alterável)": list_codref,
            }, orient='index'
        )
        self._spreadsheet = self._spreadsheet.transpose()

    @property
    def spreadsheet(self):
        return self._spreadsheet


class SkuSheet:

    def __init__(self, list_sku, list_nomesku, list_ativsku, list_skuativ, list_skuean, list_altu,
                 list_larg, list_compr, list_peso, list_unidmed,
                 list_multund, list_codrefsk, list_codfabr, list_idprd, list_nomeprd,
                 list_exibesite, list_texlink, list_descprd,
                 list_titsite, list_metatag, list_exibestq,
                 list_idcat, list_nomecat, list_idmarc, list_marca, list_condiccomer, list_codloj
                 ):
        empty = []

        self._spreadsheet = pd.DataFrame.from_dict(
            {
                "_SkuId(Não alterável": list_sku,
                "_NomeSku": list_nomesku,
                "_AtivarSkuSePossível": list_ativsku,
                "_SkuAtivo (Não alterável)": list_skuativ,
                "_SkuEan": list_skuean,
                "_Altura": list_altu,
                "_AlturaReal": empty,
                "_Largura": list_larg,
                "_LarguraReal": empty,
                "_Comprimento": list_compr,
                "_ComprimentoReal": empty,
                "_Peso": list_peso,
                "_PesoReal": empty,
                "_UnidadeMedida": list_unidmed,
                "_MultiplicadorUnidade": list_multund,
                "_CodigoReferenciaSKU": list_codrefsk,
                "_ValorFidelidade": empty,
                "_DataPrevisaoChegada": empty,
                "_CodigoFabricante": list_codfabr,
                "_IdProduto (Não alterável)": list_idprd,
                "_NomeProduto (Obrigatório)": list_nomeprd,
                "_NomeComplemento": empty,
                "_ProdutoAtivo (Não alterável)": empty,
                "_CodigoReferenciaProduto": empty,
                "_ExibeNoSite": list_exibesite,
                "_TextoLink (Não alterável)": list_texlink,
                "_DescricaoProduto": list_descprd,
                "_DataLancamentoProduto": empty,
                "_PalavrasChave": empty,
                "_TituloSite": list_titsite,
                "_MetaTagDescription": list_metatag,
                "_IdFornecedor": empty,
                "_ExibeSemEstoque": list_exibestq,
                "_Kit (Não Alterável)": empty,
                "_IdDepartamento (Não alterável)": empty,
                "_NomeDepartamento": empty,
                "_IdCategoria": list_idcat,
                "_NomeCategoria": list_nomecat,
                "_IdMarca": list_idmarc,
                "_Marca": list_marca,
                "_PesoCubico": empty,
                "_CondicaoComercial": list_condiccomer,
                "_CodigosLojas": list_codloj,
                "_Acessorios": empty,
                "_Similares": empty,
                "_Sugestoes": empty,
                "MostrarJunto": empty,
                "_Anexos": empty,
            }, orient='index'
        )
        # solving empty columns
        self._spreadsheet = self._spreadsheet.transpose()

    @property
    def spreadsheet(self):
        return self._spreadsheet
