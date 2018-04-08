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
    # for key, value in function_directory.getDirectory().items():
    #     print("Function: " + str(key))
    #     parameters = value.getParams()
    #     for parameter in parameters:
    #         print("Parameter: " + str(parameter[0]))
    #         print("Value: " + str(parameter[1]))
    #         print("Size: " + str(parameter[2]))
    #     print("Parameters: " + str(value.numberOfParameters()))
    #     print("Local variables: " + str(value.numberOfLocalVariables()))
    #     print("Temporary variables: " + str(value.numberofTemporaryVariables()))

    #     # Variables
    #     print("Variables")
    #     print("Number int of variables: " + str(value.numberOfVariablesInt()))
    #     print("Number float of variables: " + str(value.numberOfVariablesFloat()))
    #     print("Number char of variables: " + str(value.numberOfVariablesChar()))
    #     print("Number string of variables: " + str(value.numberOfVariablesString()))
    #     print("Number bool of variables: " + str(value.numberOfVariablesBool()))
    #     # Parameters
    #     print("Parameters")
    #     print("Number int of parameters: " + str(value.numberOfParametersInt()))
    #     print("Number float of parameters: " + str(value.numberOfParametersFloat()))
    #     print("Number char of parameters: " + str(value.numberOfParametersChar()))
    #     print("Number string of parameters: " + str(value.numberOfParametersString()))
    #     print("Number bool of parameters: " + str(value.numberOfParametersBool()))
    #     # Temporaries
    #     print("Temporal")
    #     print("Number int of temporary: " + str(value.numberOfTemporaryInt()))
    #     print("Number float of temporary: " + str(value.numberOfTemporaryFloat()))
    #     print("Number char of temporary: " + str(value.numberOfTemporaryChar()))
    #     print("Number string of temporary: " + str(value.numberOfTemporaryString()))
    #     print("Number bool of temporary: " + str(value.numberOfTemporaryBool()))
    # for i in quadruples:
    #     i.print()
    # for key, value in analysis.getFunctionDirectory().getDirectory().items():
    #   print("Function name: " + str(key))
    #   print("Symbol table: "  + str(len(value.getSymbolTable().getTable())))
    #   print("Returns?: " + str(value.getReturnType()))
 
if __name__ == '__main__':
    main(sys.argv) 