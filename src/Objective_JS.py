import sys
import os
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from antlr4 import *
from Grammar.Objective_JSLexer import Objective_JSLexer
from Grammar.Objective_JSParser import Objective_JSParser
from Grammar.Objective_JSListener import Objective_JSListener
from VirtualMachine import VirtualMachine

def preprocess(fileName):
    with open(fileName, 'r') as original:
        lines = original.readlines()
    for line in lines:
        if re.search("import\ [a-zA-Z]+", line) is not None:
            imported_class = line[7:-1] + ".Objective_JS"
            with open("temp_file.Objective_JS", "a") as temp_file:
                with open(imported_class, "r") as imported_class:
                    temp_file.write(imported_class.read())
                    temp_file.write("\n")

    with open('temp_file.Objective_JS', 'a') as temp_file:
        with open(fileName, 'r') as init_file:
            temp_file.write(init_file.read())

    with open('original_copy.Objective_JS', 'w') as output, open(fileName, 'r') as input:
        output.write(input.read())

    with open(fileName, 'w+') as output, open('temp_file.Objective_JS', 'r') as input:
        datas = input.readlines()
    with open(fileName, 'w+') as output:
        for data in datas:
            if re.search("import\ [a-zA-Z]+", data) is None:
                output.write(data)
    # debuging the new file
    # with open(fileName, 'r') as file:
    #     print(file.read())

    if os.path.exists('temp_file.Objective_JS'):
        os.remove('temp_file.Objective_JS')

def main(argv):
    fileName = argv[1]
    preprocess(fileName)
    # with open(fileName, "r") as file:
    #     print(file.read())
    input = FileStream(fileName)
    lexer = Objective_JSLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Objective_JSParser(stream)
    tree = parser.inicio()
    listener = Objective_JSListener(fileName)
    walker = ParseTreeWalker()
    if os.path.exists('original_copy.Objective_JS'):
        with open('original_copy.Objective_JS','r') as input, open(fileName, 'w+') as output:
            output.write(input.read())
    if os.path.exists('original_copy.Objective_JS'):
        os.remove('original_copy.Objective_JS')
    walker.walk(listener, tree)
    quadruples = listener.getQuadruples()
    # functions = listener.getFunctionDirectory()
    # for key, value in functions.getDirectory().items():
    #     print("Function: " + str(key))
    #     for key2, value2 in value.getSymbolTable().getSymbols().items():
    #         print("Var: " + str(key2))
    #         print("Address: " + str(value2.getAddress()))

    with open ('archivo.obj', 'w') as file:
        for quadruple in quadruples:
            file.write(str(quadruple.getId()) + "," + str(quadruple.getOperator()) + "," + str(quadruple.getOperand1()) + "," + str(quadruple.getOperand2()) + "," + str(quadruple.getResult()) + "\n")

    VirtualMachine()

    # function_directory = listener.getFunctionDirectory()
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
    # for key, value in listener.getFunctionDirectory().getDirectory().items():
    #   print("Function name: " + str(key))
    #   print("Symbol table: "  + str(len(value.getSymbolTable().getTable())))
    #   print("Returns?: " + str(value.getReturnType()))
 
if __name__ == '__main__':
    main(sys.argv) 