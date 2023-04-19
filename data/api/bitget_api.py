# data/api/bitget_api.py  
import requests  # 导入requests库，用于发送HTTP请求

class BitgetAPI():
    def __init__(self, api_key, secret_key):
        # super().__init__(api_key, secret_key)
        self.base_url = "https://api.bitget.com"  # Bitget API的基础URL

    def get_ticker(self, symbol):
        url = f"{self.base_url}/api/spot/v1/market/ticker?{symbol}"
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

# 参数名	参数类型	是否必须	描述
# symbol	String	是	产品ID
# period	String	是	K线的时间单位,粒度（取值参考如下列表)
# after	String	否	ms,返回大于等于本时间之后的
# before	String	否	ms,返回小于等于本时间之前的
# limit	String	否	查询条数 默认100，最大1000
    def get_klines(self, symbol, period, after=None, before=None, limit=None):
        url = f"{self.base_url}api/spot/v1/market/candles?symbol={symbol}&period={period}"
        print(url)
        if after != None:
            after = int(after.timestamp())
            url = f"{url}&after={after}"
        if before != None:
            before = int(before.timestamp())
            url = f"{url}&before={before}"
        if limit != None:
            url = f"{url}&limit={limit}"

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

    # 实现其他API方法
