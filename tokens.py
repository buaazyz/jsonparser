import string

DIGITS = '0123456789'
QUOTA = '"'

STR = string.ascii_letters + string.digits + string.punctuation
STR = STR.replace('"','')


SYMBOL = '{}[]:,'

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_LBRACE = "LBRACE"
TT_RBRACE = "RBRACE"
TT_LSQUARE = "LSQUARE"
TT_RSQUARE = "RSQUARE"
TT_COMMA = "COMMA"
TT_COLON = "COLON"
TT_STRING = "STRING"

TT_EOF ="EOF"

class Token(object):
    def __init__(self, type_, value=None, pos_begin=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_begin:
            self.pos_begin = pos_begin.copy()
            self.pos_end = pos_begin.copy()
            self.pos_end.advance(self.value)

        if pos_end:
            self.pos_end = pos_end.copy()


    def matches(self, type_, value=None):
        """
        判断是否相同
        :param type_:
        :param value:
        :return:
        """
        return self.type == type_ and self.value == value



    def __repr__(self):
        if self.value:
            return f'{self.type}: {self.value}'
        else:
            return f'{self.type}'