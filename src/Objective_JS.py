import sys
import os
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from antlr4 import *
from Grammar.Objective_JSLexer import Objective_JSLexer
from Grammar.Objective_JSParser import Objective_JSParser
from Grammar.Objective_JSListener import Objective_JSListener
from VirtualMachine import VirtualMachine
from Objective_JS_ErrorListener import Objective_JS_ErrorListener
import time
from Structures.GO import GO

"""
Remplaza todos los codigos Strings por Ints
"""
codes = {
    "GO.TO" : 1,
    "GO.TOFALSE" : 2,
    "+" : 3,
    "-" : 4,
    "=" : 5,
    "read": 6,
    "/": 7,
    "*": 8,
    "%": 9,
    "^": 10,
    "!=": 11,
    "&&": 12,
    "||": 13,
    ">": 14,
    "<": 15,
    ">=": 16,
    "<=": 17,
    "==": 18,
    "isNull": 19,
    "isNotNull": 20,
    "print": 21,
    "ERA": 22,
    "param": 23,
    "GO.SUB": 24,
    "endproc": 25,
    "return": 26,
    "save_return": 27,
    "VER": 28,
    "attribute_access": 29
}


"""
Obten el nombre de todos los archivos imports. Copia su informacion en un archivo temporal junto con el principal y luego pegalo en el archivo original
"""
def preprocess(fileName):
    with open(fileName, 'r') as original:
        lines = original.readlines()
    for line in lines:
        if re.search("import\ [a-zA-Z]+", line) is not None:
            imported_class = "Tests/" + line[7:-1] + ".Objective_JS"
            with open("Tests/temp_file.Objective_JS", "a") as temp_file:
                with open(imported_class, "r") as imported_class:
                    temp_file.write(imported_class.read())
                    temp_file.write("\n")

    with open('Tests/temp_file.Objective_JS', 'a') as temp_file:
        with open(fileName, 'r') as init_file:
            temp_file.write(init_file.read())

    with open('Tests/original_copy.Objective_JS', 'w') as output, open(fileName, 'r') as input:
        output.write(input.read())

    with open(fileName, 'w+') as output, open('Tests/temp_file.Objective_JS', 'r') as input:
        datas = input.readlines()
    with open(fileName, 'w+') as output:
        for data in datas:
            if re.search("import\ [a-zA-Z]+", data) is None:
                output.write(data)

    if os.path.exists('Tests/temp_file.Objective_JS'):
        os.remove('Tests/temp_file.Objective_JS')

"""
Manda a llamar al lexer, parser y maquina virtual con el contenido de nuestro archivo. Antes de mandar a llamar a la maquina vitual regresa el archivo con imports a su estado original para que el usuario no vea lo que se hizo con los imports.
"""
def main(argv):
    fileName = argv[1]
    preprocess(fileName)
    input = FileStream(fileName)
    lexer = Objective_JSLexer(input)
    lexer.removeErrorListeners()
    lexer._listeners = [Objective_JS_ErrorListener(fileName)]
    stream = CommonTokenStream(lexer)
    parser = Objective_JSParser(stream)
    parser._listeners = [Objective_JS_ErrorListener(fileName)]
    tree = parser.inicio()
    listener = Objective_JSListener(fileName)
    walker = ParseTreeWalker()
    if os.path.exists('Tests/original_copy.Objective_JS'):
        with open('Tests/original_copy.Objective_JS','r') as input, open(fileName, 'w+') as output:
            output.write(input.read())
    if os.path.exists('Tests/original_copy.Objective_JS'):
        os.remove('Tests/original_copy.Objective_JS')
    walker.walk(listener, tree)
    quadruples = listener.getQuadruples()

    for quadruple in quadruples:
        quadruple.setOperator(codes[str(quadruple.getOperator())])
    with open ('archivo.obj', 'w') as file:
        for quadruple in quadruples:
            file.write(str(quadruple.getId()) + "," + str(quadruple.getOperator()) + "," + str(quadruple.getOperand1()) + "," + str(quadruple.getOperand2()) + "," + str(quadruple.getResult()) + "\n")

    VirtualMachine()
    toc = time.clock()

"""
Punto de inicio del compilador
"""
if __name__ == '__main__':
    main(sys.argv) 