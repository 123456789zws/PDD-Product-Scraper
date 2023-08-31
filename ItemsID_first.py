import re

import requests

from utils.manger.Headers_Manger import Headers


class StartRequest:
    def __init__(self, opt_id):
        self.header = Headers.headers_itemid_request()
        self.opt_id = opt_id
        self.ItemPattern = re.compile(r'"goodsID":(\d+),"imgUrl":')
        self.FlipPattern = re.compile(r'"flip"\s*:\s*"([^"]*)')
        self.url = f"https://mobile.yangkeduo.com/relative_goods.html?__rp_name=search_catgoods_tab&" \
                   f"opt_id={self.opt_id}"

    def get_matches(self):
        response = requests.get(self.url, headers=self.header.headers_itemid_request)
        matches = self.ItemPattern.findall(response.text)

        flip_values = self.FlipPattern.findall(response.text)
        flip = None

        for value in flip_values:
            if value != "":
                flip = value
                break

        if flip is None:
            raise SystemExit("错误:所有flip为空值，请检查账号是否风控或者cookie是否过期")

        return flip, matches

    @staticmethod
    def get_selected_matches(self, count):
        flip, matches = self.get_matches()
        selected_matches = matches[:count]
        return flip, selected_matches
