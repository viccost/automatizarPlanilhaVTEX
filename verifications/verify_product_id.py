"""module to verify if the first id on list of products that will be registered is the correct ID.
    The ID must be the last one on VTEX. So the previous must be filled and next unfilled."""
from api.get_product_id import get_product_id
from tqdm import tqdm
from typing import List


def verify_id(idslists: List[int]) -> None:
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
