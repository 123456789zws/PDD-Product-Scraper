import json
import os
import random


class ProxyManger:
    def __init__(self, proxy_json_path='config/proxies.json'):
        self.proxy_json_path = proxy_json_path
        self.proxies = self.load_proxies()

    def load_proxies(self):
        if not os.path.exists(self.proxy_json_path):
            raise FileNotFoundError(f'配置文件{self.proxy_json_path}无法找到')

        with open(self.proxy_json_path, 'r') as f:
            data = json.load(f)
        return data.get('https', {})

    def get_random_proxy(self):
        keys = list(self.proxies.keys())
        if not keys:
            raise Exception('没有这个socks5代理')

        random_key = random.choice(keys)
        proxy_url = self.proxies[random_key]

        return {
            "http": proxy_url,
            "https": proxy_url
        }