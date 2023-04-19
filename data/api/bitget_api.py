# data/api/bitget_api.py
from .abstract_api import AbstractAPI
import requests  # 导入requests库，用于发送HTTP请求

class BitgetAPI(AbstractAPI):
    def __init__(self, api_key, secret_key):
        super().__init__(api_key, secret_key)
        self.base_url = "https://api.bitget.com"  # Bitget API的基础URL

    def get_ticker(self, symbol):
        url = f"{self.base_url}/api/spot/v1/ticker/{symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

    def get_depth(self, symbol):
        url = f"{self.base_url}/api/spot/v1/depth/{symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

    # 实现其他API方法
