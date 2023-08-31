import base64
import gzip
import json
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class CaptchaEncoder:
    KEY = 'bN3%cH2$H1@*jCo$'    # 定值 详情见开发笔记(excaildraw文件 不是md文件)
    IV = 'gl3-w^dN72ce72b6'

    @staticmethod
    def get_milli_time():
        """获取毫秒级的时间戳"""
        time.sleep(0.32)    # 这里的休眠是因为经过我的测试 pdd获取俩次时间戳大概相差300~400毫秒
        return int(round(time.time() * 1000))

    def encode_captcha_collect(self, environment):
        """生成验证码所需的密文"""
        key = self.KEY.encode('utf-8')
        iv = self.IV.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        environment_to_string = json.dumps(environment)    # 拼多多是把环境转为string → gzip → stringify 详情见开发笔记
        compressed_env_bytes = gzip.compress(environment_to_string.encode('utf-8'))
        compressed_env_str = compressed_env_bytes.decode('latin1')

        padded_env = pad(compressed_env_str.encode('utf-8'), AES.block_size)
        encrypted_env = cipher.encrypt(padded_env)

        return base64.b64encode(encrypted_env).decode('utf-8')

    @staticmethod
    def get_captcha_collect(self):
        """获取验证码所需的环境密文"""
        environment_data = {
            "v": "a",
            "ts": self.get_milli_time(),
            "t0": self.get_milli_time(),
            "tp": 3,
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "rf": "",
            "hl": "000000000001010",
            "sc": {
                "w": 1920,
                "h": 1080
            },
            "ihs": 1,
            "platform": 1
        }

        captcha_collect = self.encode_captcha_collect(environment_data)
        while len(captcha_collect) != 428:
            captcha_collect = self.encode_captcha_collect(environment_data)

        return captcha_collect