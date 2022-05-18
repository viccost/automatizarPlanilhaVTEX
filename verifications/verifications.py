
from api.get_product_id import get_product_id
from tqdm import tqdm
from typing import List
import requests


def verify_id(idslists: List[int]) -> None:
    """module to verify if the first id on list of products that will be registered is the correct ID.
    The ID must be the last one on VTEX. So the previous must be filled and next unfilled."""
    idproduct = min(idslists)
    num_ids = len(idslists)
    previousid = idproduct - 1
    nextid = idproduct + 1
    response_previous = get_product_id(previousid)
    response_actual = get_product_id(idproduct)
    response_next = get_product_id(nextid)
    print("Estoou verificando IDs :)\n")
    if response_previous == 200 and response_actual == 404 and response_next == 404:
        print("Aparentemente está tudo certo com seus ID's... Vou dar só mais uma olhadinha")
        with tqdm(total=num_ids) as barra_progresso:
            for i in range(num_ids):
                barra_progresso.update(1)
                id_to_verify = idslists[i]
                response = get_product_id(id_to_verify)
                if response == 200:
                    print(f"\nHuuum! Encontreei um ID [{id_to_verify}] já cadastrados na VTEX! Melhor recomeçar"
                          "\nPRESS ENTER\n")
                    break

    elif response_previous == 404:
        anchor = previousid
        while True:
            anchor -= 1
            if get_product_id(anchor) == 200:
                input(f"\nhEy MAN! Suponho que o primeiro ID seja {anchor + 1}!\n"
                      f"Tem um ou mais ids anteriores ainda não foram cadastrados. Melhor recomeçar\n"
                      f"PRESS ENTER\n")
                break
    elif response_next == 200:
        anchor = nextid
        while True:
            anchor += 1
            if get_product_id(anchor) == 404:
                input(f"\nhEy MAN! Suponho que o primeiro ID seja {anchor}!\n"
                      "Tem um ou mais id's dessa planilha já foram cadastrados. Melhor recomeçar\n"
                      f"PRESS ENTER\n")
                break


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
