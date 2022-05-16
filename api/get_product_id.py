from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_TOKEN = os.getenv("API_TOKEN")


def get_product_id(idproduct):
    url = f"https://tfcvb6.vtexcommercestable.com.br/api/catalog/pvt/product/{idproduct}"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-VTEX-API-AppKey": f"{API_KEY}",
        "X-VTEX-API-AppToken": f"{API_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.status_code





