from luna import util
from luna.compiler import Compiler
from luna.parser import Parser


def compile(filepath):
    tree = parse(filepath)
    compiler = Compiler()
    return compiler.compile(tree)

def interpret(filepath):
    frame = compile(filepath)
    frame.run()

def parse(filepath):
    import os
    content = filepath
    if os.path.isfile(filepath):
        content = util.read(filepath)
    parser = Parser()
    return parser.parse_with_rule(None, content)
