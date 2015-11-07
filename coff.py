import sys
from antlr4 import *
from coffLexer import coffLexer
from coffParser import coffParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = coffLexer(input)
    stream = CommonTokenStream(lexer)
    parser = coffParser(stream)
    tree = parser.programa()
if __name__ == '__main__':
    main(sys.argv)