from position import *
from tokens import *
from errors import *

class Lexer(object):

    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1,0,-1,fn,text)
        self.current_char = None
        self.advance()


    def advance(self):
        self.pos.advance(self.current_char)
        if self.pos.idx < len(self.text):
            self.current_char = self.text[self.pos.idx]
        else:
            self.current_char = None

    def make_tokens(self):
        """
        1. 遍历内容
        2. 获取内容中对应的token
        """

        tokenList = []

        while self.current_char != None:
            if self.current_char in (' ', '\t'):
                # 空格或制表符 跳过
                self.advance()
            elif self.current_char in DIGITS:
                tokenList.append(self.make_number())
            elif self.current_char in SYMBOL:
                tokenList.append(self.make_symbol())
                self.advance()
            elif self.current_char == QUOTA:
                res, error = self.make_string()
                pos_begin = self.pos.copy()
                self.advance()
                if error:
                    return [], IllegalCharError(pos_begin, self.pos, f"'{error}'")
                else:
                    tokenList.append(res)
            else:
                # 遇到非法字符 报错
                pos_begin = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_begin, self.pos, f"'{char}'")

        tokenList.append(Token(TT_EOF,pos_begin=self.pos))

        return tokenList, None


    def make_number(self):
        """
                识别整数和小数 小数包括小数点 0.1
                :return:
                """

        num_str = ''
        dot_cnt = 0

        pos_begin = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_cnt == 1:
                    break
                else:
                    dot_cnt += 1
                    num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_cnt == 0:
            return Token(TT_INT, int(num_str), pos_begin, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_begin, self.pos)


    def make_string(self):
        str = QUOTA
        self.advance()
        pos_begin = self.pos.copy()

        while self.current_char != None and self.current_char in STR:
            str += self.current_char
            self.advance()

        if self.current_char != QUOTA:
            return None, self.current_char

        str += self.current_char

        return Token(TT_STRING, str, pos_begin, self.pos), None



    def make_symbol(self):
        if self.current_char == '{':
            return Token(TT_LBRACE, pos_begin=self.pos)
        elif self.current_char == '}':
            return Token(TT_RBRACE, pos_begin=self.pos)
        elif self.current_char == '[':
            return Token(TT_LSQUARE, pos_begin=self.pos)
        elif self.current_char == ']':
            return Token(TT_RSQUARE, pos_begin=self.pos)
        elif self.current_char == ':':
            return Token(TT_COLON, pos_begin=self.pos)
        elif self.current_char == ',':
            return Token(TT_COMMA, pos_begin=self.pos)
















