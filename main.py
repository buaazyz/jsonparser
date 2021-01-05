from lexer import Lexer
from parse import Parser
from interpreter import Interpreter


def run(fn, text):
    lexer_ = Lexer(fn, text)
    tokens, error = lexer_.make_tokens()

    if error:
        return '', error
    print(text)
    print(tokens)

    parser = Parser(tokens)
    ast = parser.parse()

    print(ast.node)

    interpreter_ = Interpreter()
    res = interpreter_.visit(ast.node)

    print(res['sites'][0]['url'])

    return res, ''
