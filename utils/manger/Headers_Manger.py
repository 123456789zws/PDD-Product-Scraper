class Headers:
    @staticmethod
    def headers_opt_id_request():
        return {
            'authority': 'mobile.yangkeduo.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        }

    @staticmethod
    def headers_itemid_request():
        return {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9",
            'Cookie': "api_uid=CkvXdmTBGfOIQgBygI9fAg==; webp=1; _nano_fp=XpEbX0X8n5EbXpTjXC_2YFLSreTrCKYP~hyGRk8P; jrpl=dgno0amIvqqFCJDSqknkzTHoqekcosOJ; njrpl=dgno0amIvqqFCJDSqknkzTHoqekcosOJ; dilx=5hVSnWKzPhmOAt2EsHWlS; PDDAccessToken=NVMOTPY2SNCBP34A6LDRXRLW34OWC6EHM4I3EO6EQNQVFQNOXFSA1213cbb; pdd_user_id=2857271902524; pdd_user_uin=ITQAD2AGF6VVIOQOPQWJWDFVYM_GEXDA; pdd_vds=gaLeNLOsIILNQsyutyQubLNOnbyNONLlyOOnydIendPePmaGLdtyQNoyobiO",
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
            'cache-control': "no-cache",
        }

    @staticmethod
    def headers_search_request():
        return {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9",
            'Accesstoken': 'MRUQBJJGCR63KRUHDBSWDBZXW4CYVEBHJJXBKQGM4JY6GGGRBP5A120a579',
            'Cookie': "jrpl=dgno0amIvqqFCJDSqknkzTHoqekcosOJ; njrpl=dgno0amIvqqFCJDSqknkzTHoqekcosOJ; dilx=5hVSnWKzPhmOAt2EsHWlS; api_uid=CiQ14GTBNRhK3QBAn7ewAg==; _nano_fp=XpEbX0XJXqEYn0TqX9_aLoHZJ3ak6rGEq0phggLE; webp=1; PDDAccessToken=MRUQBJJGCR63KRUHDBSWDBZXW4CYVEBHJJXBKQGM4JY6GGGRBP5A120a579; pdd_user_id=1225633957; pdd_user_uin=6OBPI7VVC4WC5EWHVTGZ6GFOQU_GEXDA; rec_list_personal=rec_list_personal_vmj00h; pdd_vds=gaVCJuWBWDJBzTWmhNWdMdJdZxMuYlJsYwkcrNFuHThBZNZuMuzCkdVNvdpB",
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
            'cache-control': "no-cache",
        }
