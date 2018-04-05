import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from antlr4 import *
from Grammar.Objective_JSLexer import Objective_JSLexer
from Grammar.Objective_JSParser import Objective_JSParser
from Grammar.Objective_JS_SymbolTableGeneration import Objective_JS_SymbolTableGeneration
 
def main(argv):
    input = FileStream(argv[1])
    lexer = Objective_JSLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Objective_JSParser(stream)
    tree = parser.inicio()
    analysis = Objective_JS_SymbolTableGeneration()
    walker = ParseTreeWalker()
    walker.walk(analysis, tree)
    quadruples = analysis.getQuadruples()
    function_directory = analysis.getFunctionDirectory()
    for key, value in function_directory.getDirectory().items():
        print("Function: " + str(key))
        print("Parameters: " + str(value.numberOfParameters()))
        print("Local variables: " + str(value.numberOfLocalVariables()))
        print("Temporary variables: " + str(value.numberofTemporaryVariables()))
    # for i in quadruples:
    #     i.print()
    # for key, value in analysis.getFunctionDirectory().getDirectory().items():
    #   print("Function name: " + str(key))
    #   print("Symbol table: "  + str(len(value.getSymbolTable().getTable())))
    #   print("Returns?: " + str(value.getReturnType()))
 
if __name__ == '__main__':
    main(sys.argv) 