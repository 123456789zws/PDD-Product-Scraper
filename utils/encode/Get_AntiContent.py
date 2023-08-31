import random
import subprocess


class AntiContent:
    @staticmethod
    def get_anti_content():
        """运行js 获取anti_content(需要node js环境)"""
        command = "node dist/anti_content.js"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode('utf-8').strip()

    @staticmethod
    def generate_random_string(length=10):
        """
        生成一个指定长度的随机字符串，包含大写字母、小写字母和数字
        length: 随机字符串的长度，默认10位
        return: 返回一个指定长度的随机字符串
        """
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        result_string = "".join(random.choice(characters) for _ in range(length))
        return result_string
