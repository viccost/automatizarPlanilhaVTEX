from api.get_product_id import get_product_id
from tqdm import tqdm
from typing import List
import requests
from time import sleep


def verify_id(idslist: List[int]) -> None:
    """module to verify if the first id on list of products that will be registered is the correct ID.
    The ID must be the last one on VTEX. So the previous must be filled and next unfilled."""

    def get_min_id():
        _idproduct = min(idslist)
        return _idproduct

    def message(registereds_ids: List):
        """show message after verification"""
        if registereds_ids:
            print(f'ATENÇÃO! Já há IDS preenchidos: {registereds_ids}')
        else:
            print('Não há nenhum ID preenchido em sua lista.')
        print()

    idproduct = get_min_id()
    num_ids = len(idslist)
    previousid = idproduct - 1
    nextid = idproduct + 1
    response_previous = get_product_id(previousid)
    response_actual = get_product_id(idproduct)
    response_next = get_product_id(nextid)
    print("Aguarde... todos os IDs serão verificados :)\n")
    if response_previous == 200 and response_actual == 404 and response_next == 404:
        print("Está tudo certo com o menor ID que você inseriu! Agora os demais serão checados... Aguarde")

    already_register = []
    sleep(1)
    with tqdm(total=num_ids) as barra_progresso:
        for i in range(num_ids):
            barra_progresso.update(1)
            id_to_verify = idslist[i]
            response = get_product_id(id_to_verify)
            if response == 200:
                already_register.append(id_to_verify)
        print()

    message(already_register)


def verify_image_link(urls: list) -> List:
    """function to verify all url status in list"""

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
