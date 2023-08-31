import json


class AccountManager:
    def __init__(self, config_file='config/account.json'):
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def get_search_config(self, account_id):
        try:
            return self.config['search'][str(account_id)]
        except KeyError:
            return None

    def get_result_config(self, account_id):
        try:
            return self.config['result'][str(account_id)]
        except KeyError:
            return None