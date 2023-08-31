
class Decoder:
    """
    请不要问为什么变量名这么奇怪
    pdd把变量名混淆了
    我并没有通过js来实现 我是使用python来解码
    实在不知道怎么命名变量名了 抱歉  详情见开发笔记!
    """
    def __init__(self):
        self.mapping = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, 3, -1, 20, -1, 17, 8, -1, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 22, 10, -1, -1, 15, 14, 6, -1, 5, -1, -1, 7, 18, -1, 25, 9, -1, 28, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 21, -1, 31, 13, 16, -1, 26, -1, 27, -1, 0, 19, -1, 11, 4, -1, -1, 23, -1, 29, -1, -1, -1, -1, -1, -1]

    @staticmethod
    def decode(self, encrypted_text):
        """解密函数"""
        text_length = len(encrypted_text)
        if text_length % 8 != 0:
            return None

        decoded_chars = []
        for i in range(0, text_length, 8):
            values = [self.mapping[ord(encrypted_text[i + j])] for j in range(7)]
            calculations = self._calculate_values(*values, ord(encrypted_text[i + 7]))
            decoded_chars.extend([chr(calculation) for calculation in calculations])

        decoded_text = ''.join(decoded_chars)
        decoded_text = decoded_text.replace("#", "").replace("@?", "").replace("*&%", "").replace("<$|>", "")
        return decoded_text

    def _calculate_values(self, o, i, a, c, l, d, f, last_char):
        p = (31 & o) << 3 | (31 & i) >> 2
        x = (3 & i) << 6 | (31 & a) << 1 | (31 & c) >> 4
        h = (15 & c) << 4 | (31 & l) >> 1
        m = (1 & l) << 7 | (31 & d) << 2 | (31 & f) >> 3
        g = (7 & f) << 5 | 31 & self.mapping[last_char]
        return (31 & p) << 3 | x >> 5, (31 & x) << 3 | h >> 5, (31 & h) << 3 | m >> 5, (31 & m) << 3 | g >> 5, (31 & g) << 3 | p >> 5
