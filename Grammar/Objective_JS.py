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
    # for key, value in analysis.getFunctionDirectory().getDirectory().items():
    #   print("Function name: " + str(key))
    #   print("Symbol table: "  + str(len(value.getSymbolTable().getTable())))
    #   print("Returns?: " + str(value.getReturnType()))
 
if __name__ == '__main__':
    main(sys.argv) 