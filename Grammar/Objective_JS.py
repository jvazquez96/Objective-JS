import sys
from antlr4 import *
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = Objective_JSLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Objective_JSParser(stream)
    tree = parser.inicio()
 
if __name__ == '__main__':
	main(sys.argv)