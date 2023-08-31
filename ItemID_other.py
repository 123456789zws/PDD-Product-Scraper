import json
import time

import requests

from ItemsID_first import StartRequest
# from utils.CaptchaEncoder import CaptchaEncoder
from utils.encode.Get_AntiContent import AntiContent
from utils.manger.Headers_Manger import Headers

opt_id = 25927
url = "https://mobile.yangkeduo.com/proxy/api/api/search/opt/9702/groups?"
flip, selected_matches = StartRequest.get_selected_matches(opt_id, count=20)
ITEMS = []
ITEMS.extend(selected_matches)

offset = 20
for i in range(1, 20):
    flip_parts = flip.split(";")
    flip_parts[3] = str(offset - 20)
    flip = ";".join(flip_parts)

    group_params = {
        'flip': flip,
        'offset': offset,
        'anti_content': AntiContent.get_anti_content(),
        'count': 20,
        'list_id': AntiContent.generate_random_string(),
    }

    res = requests.get(url, params=group_params, headers=Headers.headers_search_request())
    print(res.status_code)
    data = json.loads(res.text)
    goods_list = data.get('goods_list', [])
    goods_ids = [item.get('goods_id') for item in goods_list if 'goods_id' in item]
    ITEMS.extend(goods_ids)
    offset += 20
    time.sleep(3)

# print(ITEMS)
# itemid_dict = {i: v for i, v in enumerate(ITEMS)}
# with open('output/ItemsID.json', 'w', encoding='utf-8') as f:
#     json.dump(itemid_dict, f, ensure_ascii=False, indent=4)
