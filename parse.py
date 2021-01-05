from tokens import *
from ast_node import *
from errors import *

class ParseResult(object):
    def __init__(self):
        self.error = None
        self.node = None
        self.advance_count = 0

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self

    def register_advance(self):
        self.advance_count += 1

    def register(self, res):
        self.advance_count += res.advance_count
        if res.error:
            self.error = res.error
        return res.node


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()


    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_token = self.tokens[self.tok_idx]

        return self.current_token

    def parse(self):
        res = self.kvs()
        if res.error or self.current_token != TT_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_begin, self.current_token.pos_end, "Unexpected char"
            ))

        return res



    def kvs(self):
        """
            kvs -> LBRACE pair (COMMA pair)* RBRACE
        """

        res = ParseResult()

        element_nodes = []
        pos_begin = self.current_token.pos_begin.copy()

        if not self.current_token.type == TT_LBRACE:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_begin,self.current_token.pos_end, "Expected '{' "
            ))

        res.register_advance()
        self.advance()


        # if empty key-value dict or not

        if self.current_token.type == TT_RBRACE:
            res.register_advance()
            self.advance()

        else:
            element_nodes.append(res.register(self.pair()))
            if res.error: return res

            while self.current_token.type == TT_COMMA:
                res.register_advance()
                self.advance()
                element_nodes.append(res.register(self.pair()))

                if res.error: return res

            if self.current_token.type != TT_RBRACE:
                res.failure(InvalidSyntaxError(
                    self.current_token.pos_begin, self.current_token.pos_end, "Expected ',' or '}' "
                ))

            res.register_advance()
            self.advance()

        return res.success(KvsNode(element_nodes,pos_begin, self.current_token.pos_end.copy()))


    def pair(self):

        res = ParseResult()

        pos_begin = self.current_token.pos_begin.copy()

        if not self.current_token.type == TT_STRING:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_begin, self.current_token.pos_end, "Expected string "
            ))

        pair_key = self.current_token

        res.register_advance()
        self.advance()


        if self.current_token.type != TT_COLON:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_begin, self.current_token.pos_end, "Expected ':' "
            ))

        res.register_advance()
        self.advance()

        pair_value = res.register(self.val())

        if res.error: return res


        return res.success(PairNode(pair_key,pair_value, pos_begin, self.current_token.pos_end.copy()))


    def val(self):

        res = ParseResult()

        pos_begin = self.current_token.pos_begin.copy()

        value = None

        if self.current_token.type == TT_LBRACE:
            value = res.register(self.kvs())
            if res.error: return res

        elif self.current_token.type == TT_LSQUARE:
            value = res.register(self.entry())
            if res.error: return res

        else:
            value = res.register(self.atom())
            if res.error: return res

        return res.success(ValNode(value, pos_begin, self.current_token.pos_end))



    def entry(self):

        """
            kvs -> LBRACE pair (COMMA pair)* RBRACE
        """

        res = ParseResult()

        element_nodes = []
        pos_begin = self.current_token.pos_begin.copy()

        if not self.current_token.type == TT_LSQUARE:
            return res.failure(InvalidSyntaxError(
                self.current_token.pos_begin, self.current_token.pos_end, "Expected '[' "
            ))

        res.register_advance()
        self.advance()

        # if empty list or not

        if self.current_token.type == TT_RSQUARE:
            res.register_advance()
            self.advance()

        else:
            element_nodes.append(res.register(self.val()))
            if res.error: return res

            while self.current_token.type == TT_COMMA:
                res.register_advance()
                self.advance()
                element_nodes.append(res.register(self.val()))

                if res.error: return res

            if self.current_token.type != TT_RSQUARE:
                res.failure(InvalidSyntaxError(
                    self.current_token.pos_begin, self.current_token.pos_end, "Expected ',' or ']' "
                ))

            res.register_advance()
            self.advance()

        return res.success(ListNode(element_nodes, pos_begin, self.current_token.pos_end.copy()))


    def atom(self):

        res = ParseResult()

        tok = self.current_token

        if self.current_token.type == TT_STRING or self.current_token.type == TT_INT or self.current_token.type == TT_FLOAT:
            res.register_advance()
            self.advance()
            return res.success(AtomNode(tok))

        return res.failure(InvalidSyntaxError(
            tok.pos_begin, tok.pos_end, "UnExpected char"
        ))































