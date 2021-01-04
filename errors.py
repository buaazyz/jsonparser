class Error(object):
    def __init__(self, pos_begin, pos_end, error_name, details):
        self.pos_begin = pos_begin
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        res = f'{self.error_name} : {self.details}  '
        res += f'File {self.pos_begin.row}, line {self.pos_end.row + 1} '
        return res

class IllegalCharError(Error):
    def __init__(self, pos_begin, pos_end , details):
        super().__init__(pos_begin, pos_end,"Illegal Char", details)


class InvalidSyntaxError(Error):
    def __init__(self, pos_begin, pos_end , details=''):
        super().__init__(pos_begin, pos_end,"Invalid Syntax", details)