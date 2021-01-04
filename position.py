class Position(object):
    def __init__(self, index, row, col, fn, ftxt):
        """
        :param index:
        :param row:
        :param col:
        :param fn:
        :param ftxt:
        """

        self.idx = index
        self.row = row
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):

        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.row += 1
            self.col = 0

    def copy(self):
        return Position(self.idx, self.row, self.col, self.fn, self.ftxt)