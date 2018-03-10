import sys
from antlr4 import *
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JS_SymbolTableGeneration import Objective_JS_SymbolTableGeneration
 
def main(argv):
    input = FileStream(argv[1])
    lexer = Objective_JSLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Objective_JSParser(stream)
    tree = parser.inicio()
    analysis = Objective_JS_SymbolTableGeneration()
    walker = ParseTreeWalker()
    walker.walk(analysis, tree)
    for key, value in analysis.getSymbolsTable().items():
    	print("Key: " + str(key))
    	print("Tipo: "  + str(value.getType()))
    	print("Visibility: " + str(value.getVisibility()))
 
if __name__ == '__main__':
	main(sys.argv)