import sys
from antlr4 import *
from coffLexer import coffLexer
from coffParser import coffParser
from maquinaVirtual import *
 
def main(argv):
    input = FileStream(argv[1])
    lexer = coffLexer(input)
    stream = CommonTokenStream(lexer)
    parser = coffParser(stream)
    tree = parser.programa()
    if parser._syntaxErrors == 0:
        maquina = maquinaVirtual(parser.dirProcs, parser.cuadruplos, parser.memGlobalEntero+1, parser.memGlobalDecimal-4999, parser.memGlobalTexto-9999, parser.dirProcs['inicio',0][3][0], parser.dirProcs['inicio',0][3][1], parser.dirProcs['inicio',0][3][2])
if __name__ == '__main__':
    main(sys.argv)