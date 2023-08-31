import json
import re

import requests

from utils.manger.Headers_Manger import Headers


class PDDScraper:
    def __init__(self):
        self.header = Headers.headers_opt_id_request()
        self.url = "https://mobile.yangkeduo.com/classification.html"
        self.pattern = re.compile(r'"linkUrl"\s*:\s*".*?",\s*"optId"\s*:\s*(\d+)', re.DOTALL)

    @staticmethod
    def scrape(self):
        res = requests.get(self.url, headers=self.header.headers_opt_id_request)

        matches = []

        for match in self.pattern.finditer(res.text):
            matches.append(match.group(1))

        matches = matches[:33]

        output_dict = {i: match for i, match in enumerate(matches, start=1)}

        with open('output/opt_id.json', 'w', encoding='utf-8') as file:
            json.dump(output_dict, file, ensure_ascii=False, indent=4)
