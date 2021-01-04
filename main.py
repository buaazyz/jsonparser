from lexer import Lexer
from parse import Parser


def run(fn, text):
    lexer_ = Lexer(fn, text)
    tokens, error = lexer_.make_tokens()

    if error:
        return '', error
    # print(text)
    print(tokens)

    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ''
