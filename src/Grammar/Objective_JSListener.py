# Generated from Objective_JS.g4 by ANTLR 4.7.1
from antlr4 import *

import sys
import re
import os
import numpy as np
import fileinput
from Structures.Cube import Cube
from Structures.FunctionsDirectory import FunctionsDirectory
from Structures.GO import GO
from Structures.InfoDirectory import InfoDirectory
from Structures.Info import Info
from Structures.Stack import Stack
from Structures.SymbolTable import SymbolTable
from Structures.Quadruple import Quadruple
from Structures.Dimensions import Dimensions
from Structures.ParamTable import ParamTable
from Structures.Classes import Classes
from Structures.Atts import Atts

if __name__ is not None and "." in __name__:
    from .Objective_JSParser import Objective_JSParser
else:
    from Objective_JSParser import Objective_JSParser

CONST_GLOBAL_BOTTOM_INT = 1000
CONST_GLOBAL_BOTTOM_FLOAT = 2000
CONST_GLOBAL_BOTTOM_CHAR = 3000
CONST_GLOBAL_BOTTOM_STRING = 4000
CONST_GLOBAL_BOTTOM_BOOLEAN = 5000
CONST_GLOBAL_BOTTOM_NULL = 6000

CONST_GLOBAL_TOP_INT = 1999
CONST_GLOBAL_TOP_FLOAT = 2999
CONST_GLOBAL_TOP_CHAR = 3999
CONST_GLOBAL_TOP_STRING = 4999
CONST_GLOBAL_TOP_BOOLEAN = 5999
CONST_GLOBAL_TOP_NULL = 6999

CONST_LOCAL_BOTTOM_INT = 7000
CONST_LOCAL_BOTTOM_FLOAT = 8000
CONST_LOCAL_BOTTOM_CHAR = 9000
CONST_LOCAL_BOTTOM_STRING = 10000
CONST_LOCAL_BOTTOM_BOOLEAN = 11000
CONST_LOCAL_BOTTOM_NULL = 12000

CONST_LOCAL_TOP_INT = 7999
CONST_LOCAL_TOP_FLOAT = 8999
CONST_LOCAL_TOP_CHAR = 9999
CONST_LOCAL_TOP_STRING = 10999
CONST_LOCAL_TOP_BOOLEAN = 11999
CONST_LOCAL_TOP_NULL = 12999

CONST_TEMPORAL_BOTTOM_INT = 13000
CONST_TEMPORAL_BOTTOM_FLOAT = 14000
CONST_TEMPORAL_BOTTOM_CHAR = 15000
CONST_TEMPORAL_BOTTOM_STRING = 16000
CONST_TEMPORAL_BOTTOM_BOOLEAN = 17000
CONST_TEMPORAL_BOTTOM_NULL = 18000

CONST_TEMPORAL_TOP_INT = 13999
CONST_TEMPORAL_TOP_FLOAT = 14999
CONST_TEMPORAL_TOP_CHAR = 15999
CONST_TEMPORAL_TOP_STRING = 16999
CONST_TEMPORAL_TOP_BOOLEAN = 17999
CONST_TEMPORAL_TOP_NULL = 18999

CONST_OBJECTS_START_ADDRESS = 19000


# This class defines a complete listener for a parse tree produced by Objective_JSParser.
"""
Esta clase pasa a traves de cada regla de la gramatica y genera 2 funciones (enter y exit de la regla). A traves de cada realizamos la verificacion semantica.
Esta clase contiene:
fileName: string
functions_directory : FunctionsDirectory
type : int
accessible : boolean
does_returns : string
arguments : ParamTable()
constructores : int
cuadruplos : list
operadores : stack
operandos : stack
types : stack
while_jumps : stack
registros : int
oraculo : Cube
isListDeclared : boolean
pending_jumps : Stack
id : int
do_object : boolean
current_param_counter : int
isGlobalVar : boolean
dims : Stack
ids : Stack
imports : list
only_class : Boolean
is_arr_or_mat : boolean
clasess : dict
className : string
class_from_instance : boolean
attributes : dict
methods : FunctionDirectory()
object_counter : int
is_main_file : boolean
object_access : int
"""
class Objective_JSListener(ParseTreeListener):

    """
    Inicializa los atributos de la clase, recibe como parametro el nombre del archivo
    """
    def __init__(self, fileName):
        self.fileName = fileName
        self.functions_directory = FunctionsDirectory()
        self.type = None
        # Default visibility
        self.accessible = False
        self.does_returns = None
        self.function_name = None
        self.argumentos = ParamTable()
        self.constructores = 0
        self.cuadruplos = []
        self.operadores = Stack()
        self.operandos = Stack()
        self.types = Stack()
        self.while_jumps = Stack()
        self.registros = 1
        self.oraculo = Cube()
        self.isListDeclared = False
        self.pending_jumps = Stack()
        self.id = 1
        self.do_object = False
        self.current_param_counter = 0
        self.initMemoryAddresses()
        self.isGlobalVar = True
        self.dims = Stack()
        self.ids = Stack()
        self.imports = []
        self.only_class = False
        self.is_arr_or_mat = False
        self.reads = Stack()
        self.classes = dict()
        self.className = None
        self.class_from_instance = False
        self.attributes = dict()
        self.methods = FunctionsDirectory()
        self.object_counter = CONST_OBJECTS_START_ADDRESS
        self.is_main_file = False
        self.object_address = None


    """
    Reinicia las memorias locales y temporales
    """
    def resetMemoryAddresses(self):
        self.current_local_int_counter = CONST_LOCAL_BOTTOM_INT
        self.current_local_float_counter = CONST_LOCAL_BOTTOM_FLOAT
        self.current_local_char_counter = CONST_LOCAL_BOTTOM_CHAR
        self.current_local_string_counter = CONST_LOCAL_BOTTOM_STRING
        self.current_local_boolean_counter = CONST_LOCAL_BOTTOM_BOOLEAN
        self.current_local_null_counter = CONST_LOCAL_BOTTOM_NULL
        self.current_temp_int_counter = CONST_TEMPORAL_BOTTOM_INT
        self.current_temp_float_counter = CONST_TEMPORAL_BOTTOM_FLOAT
        self.current_temp_char_counter = CONST_TEMPORAL_BOTTOM_CHAR
        self.current_temp_string_counter = CONST_TEMPORAL_BOTTOM_STRING
        self.current_temp_boolean_counter = CONST_TEMPORAL_BOTTOM_BOOLEAN
        self.current_temp_null_counter = CONST_TEMPORAL_BOTTOM_NULL

    """
    Inicializa las direcciones de memoria
    """
    def initMemoryAddresses(self):
        self.current_global_int_counter = CONST_GLOBAL_BOTTOM_INT
        self.current_global_float_counter = CONST_GLOBAL_BOTTOM_FLOAT
        self.current_global_char_counter = CONST_GLOBAL_BOTTOM_CHAR
        self.current_global_string_counter = CONST_GLOBAL_BOTTOM_STRING
        self.current_global_boolean_counter = CONST_GLOBAL_BOTTOM_BOOLEAN
        self.current_global_null_counter = CONST_GLOBAL_BOTTOM_NULL
        self.current_local_int_counter = CONST_LOCAL_BOTTOM_INT
        self.current_local_float_counter = CONST_LOCAL_BOTTOM_FLOAT
        self.current_local_char_counter = CONST_LOCAL_BOTTOM_CHAR
        self.current_local_string_counter = CONST_LOCAL_BOTTOM_STRING
        self.current_local_boolean_counter = CONST_LOCAL_BOTTOM_BOOLEAN
        self.current_local_null_counter = CONST_LOCAL_BOTTOM_NULL
        self.current_temp_int_counter = CONST_TEMPORAL_BOTTOM_INT
        self.current_temp_float_counter = CONST_TEMPORAL_BOTTOM_FLOAT
        self.current_temp_char_counter = CONST_TEMPORAL_BOTTOM_CHAR
        self.current_temp_string_counter = CONST_TEMPORAL_BOTTOM_STRING
        self.current_temp_boolean_counter = CONST_TEMPORAL_BOTTOM_BOOLEAN
        self.current_temp_null_counter = CONST_TEMPORAL_BOTTOM_NULL

    def getFunctionDirectory(self):
        """
        Get the function directory
        """
        return self.functions_directory

    def getQuadruples(self):
        """
        Get all the quadruples generated
        """
        return self.cuadruplos

    def isFunctionDeclared(self, name):
        """
        Check if a function is already declared
        """
        if name in self.functions_directory.getDirectory():
            return True
        else:
            return False

    def isVarDeclared(self, var):
        """
        Check if the variable is already declared
        """
        table = self.functions_directory.getTable(self.function_name).getParamTable()
        exist = False

        # Check if the 'var' is a function
        exist = self.isFunctionDeclared(var)

        if var in table.getParameters():
            exist = True
        else:
            for key, value in self.functions_directory.getDirectory().items():
                if var in value.getSymbolTable().getSymbols():
                    exist = True
                    break

        if not exist:
            print(var + " is used but not defined!")
            sys.exit(0)

    def isAttributeDeclared(self, var):
        print("var: " + str(var))
        self.classes[self.className].isAttribute(var)

    def fill(self, end, next):
        """
        Fill the quadruple
        """
        quadruple = self.cuadruplos[end]
        quadruple.setResult(next)

    def getTypeFromVariable(self, var):
        """
        Check the var table of the function
        for the type of variable
        """
        # First check in the local scope
        if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var):
            return self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getType()
        elif self.functions_directory.getTable(self.function_name).getParamTable().getParam(var):
                return self.functions_directory.getTable(self.function_name).getParamTable().getType(var)
        # Then check in the global scope
        for key, value in self.functions_directory.getDirectory().items():
            if var in value.getSymbolTable().getSymbols():
                return value.getSymbolTable().getContent(var).getType()

    def getMemoryAddressFromVariable(self, var):
        """
        Check the var table of the function
        for the type of variable
        """
        # First check in the local scope
        if self.className is not None and self.function_name != "main":
            if var not in self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters().keys():
                table = self.methods.getTable(self.function_name).getSymbolTable().getSymbols()
            else:
                table = self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters()
            return table[var].getAddress()
        else:
            if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var):
                address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getAddress()
                return address
            elif self.functions_directory.getTable(self.function_name).getParamTable().getParam(var):
                return self.functions_directory.getTable(self.function_name).getParamTable().getAddress(var)
            # Then check in the global scope
            for key, value in self.functions_directory.getDirectory().items():
                if var in value.getSymbolTable().getSymbols():
                    return value.getSymbolTable().getContent(var).getAddress()

    def getDimsFromVariable(self, var):
        if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var):
            dimension = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getDimensions()
            return dimension
        elif var in self.functions_directory.getTable(self.function_name).getParamTable().getParameters():
            return self.functions_directory.getTable(self.function_name).getParamTable().getDimensions(var)
        # Then check in the global scope
        for key, value in self.functions_directory.getDirectory().items():
            if var in value.getSymbolTable().getSymbols():
                return value.getSymbolTable().getContent(var).getDimensions()

    def newClass(self, className):
        """
        Create a new class in the funtion
        """

        if className in self.classes.keys():
            print("The class was already defined")
            sys.exit(0)
        else:
            self.className = className
            self.classes[className] = Classes()
            self.classes[className].setName(className)


    """
    Parsea la informacion de una lista que recibe como parametro
    regresa el tamano total, el numero de dimensiones y una lista de Dimensiones
    """
    def parseList(self, type):
        totalSize = 1
        number_dimensions = 0
        dimensions = []
        isFirst = True
        start = 0
        for i in range(0, len(type)):
            if type[i] == '[':
                size = 1
                while (type[i+1] != ']'):
                    if isFirst:
                        start = i + 1
                        isFirst = not isFirst
                    size += 1
                    i += 1
                number_dimensions += 1
                dim = int(type[start : start+size-1])
                dimension = Dimensions(0, dim)
                dimensions.append(dimension)
                totalSize *= dim
                isFirst = True
        if number_dimensions == 2: # Matrix:
            dimensions[0].setM(dimensions[1].getUpperBound()+1)
            dimensions[1].setM(0)
        else: # List
            dimensions[0].setM(0)
        return totalSize, number_dimensions, dimensions

    """
    Agrega una nueva variable al directorio de funciones o a la tabla de atributos de una clase
    """
    def newVars(self, id, type, mat_or_arr):
        if self.className is None and self.is_main_file:
            if id in self.functions_directory.getTable(self.function_name).getSymbolTable().getSymbols().items():
                print("Syntax error!! Variable: " + id + " is already defined")
                sys.exit(0)
        elif self.function_name is None:
            if id in self.attributes.keys():
                print("Attribute: " + id + " is already defined")
                sys.exit(0)
        else:
            if id in self.methods.getDirectory():
                if id in self.methods.getTable(self.function_name).getSymbolTable().getSymbols().keys():
                    print("Syntax error!! Variable: " + id + " is already defined")
                    sys.exit(0)
        isList = False
        total_size = 1
        dimensions = []
        number_dimensions = 0
        if type == "int" or type == 0 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None or self.is_main_file:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_int_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_int_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_int_counter)
                self.current_global_int_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_int_counter += 1
        elif type == "float" or type == 1 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_float_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_float_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_float_counter)
                self.current_global_float_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_float_counter += 1
        elif type == "char" or type == 2 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None or self.is_main_file:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_char_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_char_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_char_counter)
                self.current_global_char_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_char_counter += 1
        elif type == "string" or type == 3 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_string_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_string_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_string_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_string_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_string_counter)
                self.current_global_string_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_string_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_string_counter += 1

        elif type == "bool" or type == 4 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_boolean_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_boolean_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_boolean_counter)
                self.current_global_boolean_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_boolean_counter += 1
        elif type == "null" or type == 5 and not mat_or_arr:
            number_dimensions += 1
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_null_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_global_null_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_null_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.current_local_null_counter += 1
            elif self.function_name is None:
                self.attributes[id] = Atts(id, type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_null_counter)
                self.current_global_null_counter += 1
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_null_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_null_counter += 1
        elif re.search("list(\[.*\])+int", self.type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(self.type)
            isList = True
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_int_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, self.type, isList, total_size, number_dimensions, dimensions)

                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_int_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_int_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_int_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_int_counter += (dimensions[0].getUpperBound())
            elif self.function_name is None:
                self.attributes[id] = Atts(id, self.type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_int_counter)
                if len(dimensions) == 2:
                    self.current_global_int_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_global_int_counter += (dimensions[0].getUpperBound())
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    self.current_local_int_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_int_counter += (dimensions[0].getUpperBound())
        elif re.search("list(\[.*\])+float", self.type) is not None:
            isList = True
            total_size, number_dimensions, dimensions = self.parseList(self.type)
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_float_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, self.type, isList, total_size, number_dimensions, dimensions)

                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_float_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_float_counter += (dimensions[0].getUpperBound())
            elif self.function_name is None:
                self.attributes[id] = Atts(id, self.type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_float_counter)
                if len(dimensions) == 2:
                    self.current_global_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_global_float_counter += (dimensions[0].getUpperBound())
            elif self.is_main_file:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_float_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, self.type, isList, total_size, number_dimensions, dimensions)

                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_float_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_float_counter += (dimensions[0].getUpperBound())
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    self.current_local_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_float_counter += (dimensions[0].getUpperBound())

        elif re.search("list(\[.*\])+char", self.type) is not None:
            isList = True
            total_size, number_dimensions, dimensions = self.parseList(self.type)
            if self.className is None:
                if self.isGlobalVar:
                    # print(id + " - " + str(self.current_global_char_counter))
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_char_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                    # print(id + " - " + str(self.current_local_char_counter))
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, self.type, isList, total_size, number_dimensions, dimensions)

                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_char_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_char_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_char_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_char_counter += (dimensions[0].getUpperBound())
            elif self.function_name is None:
                self.attributes[id] = Atts(id, self.type, self.accessible, isList, total_size, number_dimensions, dimension, self.current_global_char_counter)
                if len(dimensions) == 2:
                    self.current_global_char_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_global_char_counter += (dimensions[0].getUpperBound())
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    self.current_local_char_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_char_counter += (dimensions[0].getUpperBound())

        elif re.search("list(\[.*\])+string", self.type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(self.type)
            isList = True
            if self.className is None:
                if self.isGlobalVar:                
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_string_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_string_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_string_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_string_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_string_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_string_counter += (dimensions[0].getUpperBound())
            elif self.function_name is None:
                self.attributes[id] = Atts(id, self.type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_string_counter)
                if len(dimensions) == 2:
                    self.current_global_string_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_global_string_counter += (dimensions[0].getUpperBound())
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_string_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    self.current_local_string_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_string_counter += (dimensions[0].getUpperBound())


        elif re.search("list(\[.*\])+bool", self.type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(self.type)
            isList = True
            if self.className is None:
                if self.isGlobalVar:
                   
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_boolean_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                else:
                   
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    if self.isGlobalVar:
                        self.current_global_boolean_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                    else:
                        self.current_local_boolean_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    if self.isGlobalVar:
                        self.current_global_boolean_counter += (dimensions[0].getUpperBound())
                    else:
                        self.current_local_boolean_counter += (dimensions[0].getUpperBound())
            elif self.function_name is None:
                self.attributes[id] = Atts(id, self.type, self.accessible, isList, total_size, number_dimensions, dimensions, self.current_global_boolean_counter)
                if len(dimensions) == 2:
                    self.current_global_boolean_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_global_boolean_counter += (dimensions[0].getUpperBound())
            else:
                self.methods.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, self.type, isList, total_size, number_dimensions, dimensions)
                if len(dimensions) == 2:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound())
        elif re.search("list(\[[0-9]+\])+[A-Z][a-z]*", self.type) is not None:
            print("Sorry we don't support list of objects as parameters")
            sys.exit()
        else: # It's an object
            number_dimensions += 1
            if self.className is None:
                if self.isGlobalVar:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.object_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.object_counter += 1
                else:
                    self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.object_counter, id, type, isList, total_size, number_dimensions, dimensions)
                    self.object_counter += 1
            else:
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.object_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.object_counter += 1

    """
    Agrega una nueva funcion al directorio de funciones de clases o de la clase principal
    """
    def newFunction(self):
        if self.className is None and self.is_main_file:
            if self.function_name not in self.functions_directory.getDirectory():
                self.functions_directory.create_table(self.function_name, InfoDirectory(SymbolTable()))
                self.functions_directory.getTable(self.function_name).setParamTable(self.argumentos)
                start_address = len(self.cuadruplos) + 1
                self.functions_directory.getTable(self.function_name).setStartAddress(start_address)
                for key, value in self.argumentos.getParameters().items():
                    if value.getType() == 0:
                        self.functions_directory.addParam(self.function_name, key, "int", value.getListSize())
                    elif value.getType() == 1:
                        self.functions_directory.addParam(self.function_name, key, "float", value.getListSize())
                    elif value.getType() == 2:
                        self.functions_directory.addParam(self.function_name, key, "char", value.getListSize())
                    elif value.getType() == 3:
                        self.functions_directory.addParam(self.function_name, key, "string", value.getListSize())
                    elif value.getType() == 4:
                        self.functions_directory.addParam(self.function_name, key, "bool", value.getListSize())
            else:
                print("Syntax error!! Function: " + self.function_name + " is already defined")
                sys.exit(0)
        elif self.is_main_file:
            if self.function_name not in self.functions_directory.getDirectory():
                self.functions_directory.create_table(self.function_name, InfoDirectory(SymbolTable()))
                self.functions_directory.getTable(self.function_name).setParamTable(self.argumentos)
                start_address = len(self.cuadruplos) + 1
                self.functions_directory.getTable(self.function_name).setStartAddress(start_address)
                for key, value in self.argumentos.getParameters().items():
                    if value.getType() == 0:
                        self.functions_directory.addParam(self.function_name, key, "int", value.getListSize())
                    elif value.getType() == 1:
                        self.functions_directory.addParam(self.function_name, key, "float", value.getListSize())
                    elif value.getType() == 2:
                        self.functions_directory.addParam(self.function_name, key, "char", value.getListSize())
                    elif value.getType() == 3:
                        self.functions_directory.addParam(self.function_name, key, "string", value.getListSize())
                    elif value.getType() == 4:
                        self.functions_directory.addParam(self.function_name, key, "bool", value.getListSize())
            else:
                print("Syntax error!! Function: " + self.function_name + " is already defined")
                sys.exit(0)
        else:
            start_address = len(self.cuadruplos) + 1
            self.methods.getTable(self.function_name).setStartAddress(start_address)
            for key, value in self.argumentos.getParameters().items():
                if value.getType() == 0:
                    self.methods.addParam(self.function_name, key, "int", value.getListSize())
                elif value.getType() == 1:
                    self.methods.addParam(self.function_name, key, "float", value.getListSize())
                elif value.getType() == 2:
                    self.methods.addParam(self.function_name, key, "char", value.getListSize())
                elif value.getType() == 3:
                    self.methods.addParam(self.function_name, key, "string", value.getListSize())
                elif value.getType() == 4:
                    self.methods.addParam(self.function_name, key, "bool", value.getListSize())

    """
    Convierte un tipo de dato string a int
    """
    def convertIntToStringType(self, type):
        if type == 0:
            return "int"
        elif type == 1:
            return "float"
        elif type == 2:
            return "char"
        elif type == 3:
            return "string"
        elif type == 4:
            return "boolean"
        elif type == 5:
            return "null"

    """
    Convierte un tipo de dato o lista a int
    """
    def getTypeFromFactor(self, ctx, value):
        if ctx.varCte().TYPE_INT() is not None or re.search("list(\[.*\])+int", value) is not None:
            return 0
        elif ctx.varCte().TYPE_FLOAT() is not None or  re.search("list(\[.*\])+float", value) is not None:
            return 1
        elif ctx.varCte().TYPE_CHAR() is not None or  re.search("list(\[.*\])+char", value) is not None:
            return 2
        elif ctx.varCte().TYPE_STRING() is not None or re.search("list(\[.*\])+string", value) is not None:
            return 3
        elif ctx.varCte().TYPE_BOOL() is not None or re.search("list(\[.*\])+bool", value) is not None:
            return 4
        else:
            return self.getTypeFromVariable(value)

    """
    Convierte un tipo de dato o lista a int
    """
    def convertTypeToInt(self, type):
        if type is not None and not isinstance(type, int):
            if type == "int" or re.search("list(\[.*\])+int", type) is not None:
                return 0
            elif type == "float" or re.search("list(\[.*\])+float", type) is not None:
                return 1
            elif type == "char" or re.search("list(\[.*\])+char", type) is not None:
                return 2
            elif type == "string" or re.search("list(\[.*\])+string", type) is not None:
                return 3
            elif type == "bool" or re.search("list(\[.*\])+bool", type) is not None:
                return 4
            elif type == "null":
                return 5
        return type

    # Enter a parse tree produced by Objective_JSParser#inicio.
    """
    Marca el inicio de una clase y noe l main
    """
    def enterInicio(self, ctx:Objective_JSParser.InicioContext):
        if ctx.main() is None:
            self.only_class = True

    # Exit a parse tree produced by Objective_JSParser#inicio.
    """
    Marca el inicio de la clase
    """
    def exitInicio(self, ctx:Objective_JSParser.InicioContext):
        if  self.only_class:
            end = self.pending_jumps.pop()
            self.fill(end, len(self.cuadruplos) + 1)

    # Enter a parse tree produced by Objective_JSParser#main.
    """
    Genera el cuadruplo para ir a la funcion principal
    """
    def enterMain(self, ctx:Objective_JSParser.MainContext):
        quadruple = Quadruple(self.id, GO.TO, None, None, None)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos) - 1)

    # Exit a parse tree produced by Objective_JSParser#main.
    """
    Marca el fin de la funcion principal
    """
    def exitMain(self, ctx:Objective_JSParser.MainContext):
        self.is_main_file = True

    # Enter a parse tree produced by Objective_JSParser#clase.
    """
    Genera el cuadruplo para el inicio de una clase
    """
    def enterClase(self, ctx:Objective_JSParser.ClaseContext):
        if self.only_class:
            quadruple = Quadruple(self.id, GO.TO, None, None, None)
            self.cuadruplos.append(quadruple)
            self.id += 1
            self.pending_jumps.push(len(self.cuadruplos) - 1)

        className = ctx.CLASSNAME().getText()
        self.newClass(className)

    # Exit a parse tree produced by Objective_JSParser#clase.
    def exitClase(self, ctx:Objective_JSParser.ClaseContext):
        # self.is_main_file = True
        pass

    """
    Al final de cada clase, agrega los metodos y atributos a su diccionario corresponiente
    """
    def exitEndClase(self, ctx):
        self.classes[self.className].updateMethods(self.methods)
        if self.classes[self.className].getInherits() is not None:
            self.classes[self.className].copyMethods(self.classes[self.classes[self.className].getInherits()])
        self.methods = FunctionsDirectory()
        self.argumentos = ParamTable()
        self.function_name = None
        self.attributes = dict()
        self.className = None

    # Enter a parse tree produced by Objective_JSParser#imports.
    def enterImports(self, ctx:Objective_JSParser.ImportsContext):
        pass

    def enterPasteImports(self, ctx):
        pass

    # Exit a parse tree produced by Objective_JSParser#imports.
    def exitImports(self, ctx:Objective_JSParser.ImportsContext):
        pass

    # Enter a parse tree produced by Objective_JSParser#class_declaration.
    def enterClass_declaration(self, ctx:Objective_JSParser.Class_declarationContext):
        if ctx.CLASSNAME() is not None:
            self.function_name = ctx.CLASSNAME().getText()
            self.functions_directory.create_table(self.function_name, InfoDirectory(None))
            self.is_main_file = True

    # Exit a parse tree produced by Objective_JSParser#class_declaration.
    def exitClass_declaration(self, ctx:Objective_JSParser.Class_declarationContext):
        pass

    """
    MArca el inicio de la funcion main, inicia la tabla de funciones de la clase
    """
    # Enter a parse tree produced by Objective_JSParser#main_header.
    def enterMain_header(self, ctx:Objective_JSParser.Main_headerContext):
        self.is_main_file = True
        self.function_name = "main"
        self.functions_directory.create_table("main", InfoDirectory(None))

    """
    MArca el inicio de la clase main
    """
    # Exit a parse tree produced by Objective_JSParser#main_header.
    def exitMain_header(self, ctx:Objective_JSParser.Main_headerContext):
        self.registros = 1
        main = self.pending_jumps.pop()
        self.fill(main, len(self.cuadruplos)+1)


    # Enter a parse tree produced by Objective_JSParser#bloque.
    def enterBloque(self, ctx:Objective_JSParser.BloqueContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloque.
    def exitBloque(self, ctx:Objective_JSParser.BloqueContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#preEstatuto.
    def enterPreEstatuto(self, ctx:Objective_JSParser.PreEstatutoContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#preEstatuto.
    def exitPreEstatuto(self, ctx:Objective_JSParser.PreEstatutoContext):
        pass


    """
    Verifica la herencia de una clase
    """
    # Enter a parse tree produced by Objective_JSParser#claseAux.
    def enterClaseAux(self, ctx:Objective_JSParser.ClaseAuxContext):
        if ctx.INHERITS() is not None:
            inherits = ctx.CLASSNAME().getText()
            if self.className == inherits:
                print("Class " + self.className + " cannot inherits from himself")
                sys.exit(0)
            elif inherits in self.classes.keys():
                self.classes[self.className].setInherits(inherits)
            else:
                print("Class " + inherits + " not defined")
                sys.exit(0)

    # Exit a parse tree produced by Objective_JSParser#claseAux.
    def exitClaseAux(self, ctx:Objective_JSParser.ClaseAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#bloqueClase.
    def enterBloqueClase(self, ctx:Objective_JSParser.BloqueClaseContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueClase.
    def exitBloqueClase(self, ctx:Objective_JSParser.BloqueClaseContext):
        pass


    """
    Verifica que el constructor tenga el mismo nombre de la clase
    """
    # Enter a parse tree produced by Objective_JSParser#constructor.
    def enterConstructor(self, ctx:Objective_JSParser.ConstructorContext):
        if ctx.CLASSNAME().getText() != self.className:
            print("The constructor has a different name")
            sys.exit(0)


    # Exit a parse tree produced by Objective_JSParser#constructor.
    def exitConstructor(self, ctx:Objective_JSParser.ConstructorContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#constructorAux.
    def enterConstructorAux(self, ctx:Objective_JSParser.ConstructorAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#constructorAux.
    def exitConstructorAux(self, ctx:Objective_JSParser.ConstructorAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#constructorAux2.
    def enterConstructorAux2(self, ctx:Objective_JSParser.ConstructorAux2Context):
        pass

    # Exit a parse tree produced by Objective_JSParser#constructorAux2.
    def exitConstructorAux2(self, ctx:Objective_JSParser.ConstructorAux2Context):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributos.
    def enterAtributos(self, ctx:Objective_JSParser.AtributosContext):
        self.function_name = None

    """
    Agrega todos los atributos a la clase y reinicia las direcciones
    """
    # Exit a parse tree produced by Objective_JSParser#atributos.
    def exitAtributos(self, ctx:Objective_JSParser.AtributosContext):
        self.classes[self.className].setAttributes(self.attributes)
        self.resetMemoryAddresses()

    """
    Marca la visibilidad como verdadera
    """
    # Enter a parse tree produced by Objective_JSParser#atributosPublic.
    def enterAtributosPublic(self, ctx:Objective_JSParser.AtributosPublicContext):
        self.accessible = True

    # Exit a parse tree produced by Objective_JSParser#atributosPublic.
    def exitAtributosPublic(self, ctx:Objective_JSParser.AtributosPublicContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosPublicAux.
    def enterAtributosPublicAux(self, ctx:Objective_JSParser.AtributosPublicAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#atributosPublicAux.
    def exitAtributosPublicAux(self, ctx:Objective_JSParser.AtributosPublicAuxContext):
        pass

    """
    Marca la visibilidad como falsa
    """
    # Enter a parse tree produced by Objective_JSParser#atributosPrivate.
    def enterAtributosPrivate(self, ctx:Objective_JSParser.AtributosPrivateContext):
        self.accessible = False

    # Exit a parse tree produced by Objective_JSParser#atributosPrivate.
    def exitAtributosPrivate(self, ctx:Objective_JSParser.AtributosPrivateContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosPrivateAux.
    def enterAtributosPrivateAux(self, ctx:Objective_JSParser.AtributosPrivateAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#atributosPrivateAux.
    def exitAtributosPrivateAux(self, ctx:Objective_JSParser.AtributosPrivateAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosProtected.
    def enterAtributosProtected(self, ctx:Objective_JSParser.AtributosProtectedContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#atributosProtected.
    def exitAtributosProtected(self, ctx:Objective_JSParser.AtributosProtectedContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodos.
    def enterMetodos(self, ctx:Objective_JSParser.MetodosContext):
        pass

    """
    Agrega los metodos de una clase a su directorio de funciones
    """
    # Exit a parse tree produced by Objective_JSParser#metodos.
    def exitMetodos(self, ctx:Objective_JSParser.MetodosContext):
        self.classes[self.className].addMethodsTable(self.methods)
        if self.classes[self.className].getInherits() is not None:
            self.classes[self.className].copyAtts(self.classes[self.classes[self.className].getInherits()])

        self.argumentos = ParamTable()
        self.methods = FunctionsDirectory()


    # Enter a parse tree produced by Objective_JSParser#metodosPublicos.
    """
    Marca la visibildad de los metodos como publica
    """
    def enterMetodosPublicos(self, ctx:Objective_JSParser.MetodosPublicosContext):
        self.accessible = True

    # Exit a parse tree produced by Objective_JSParser#metodosPublicos.
    def exitMetodosPublicos(self, ctx:Objective_JSParser.MetodosPublicosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPublicosAux.
    def enterMetodosPublicosAux(self, ctx:Objective_JSParser.MetodosPublicosAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPublicosAux.
    def exitMetodosPublicosAux(self, ctx:Objective_JSParser.MetodosPublicosAuxContext):
        pass

    """
    Marca la visibilidad de los metodos como privada
    """
    # Enter a parse tree produced by Objective_JSParser#metodosPrivados.
    def enterMetodosPrivados(self, ctx:Objective_JSParser.MetodosPrivadosContext):
        self.accessible = False

    # Exit a parse tree produced by Objective_JSParser#metodosPrivados.
    def exitMetodosPrivados(self, ctx:Objective_JSParser.MetodosPrivadosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPrivadosAux.
    def enterMetodosPrivadosAux(self, ctx:Objective_JSParser.MetodosPrivadosAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPrivadosAux.
    def exitMetodosPrivadosAux(self, ctx:Objective_JSParser.MetodosPrivadosAuxContext):
        pass


    """
    Crea un nuevo directorio de funciones para la funcion
    """
    # Enter a parse tree produced by Objective_JSParser#func.
    def enterFunc(self, ctx:Objective_JSParser.FuncContext):
        self.function_name = ctx.ID().getText()
        self.argumentos = ParamTable()

    """
    Al final de la funcion reinicia las direcciones
    """
    # Exit a parse tree produced by Objective_JSParser#func.
    def exitFunc(self, ctx:Objective_JSParser.FuncContext):
        self.resetMemoryAddresses()
        pass


    # Enter a parse tree produced by Objective_JSParser#funcAux.
    def enterFuncAux(self, ctx:Objective_JSParser.FuncAuxContext):
        pass

    """
    Almacena toda la informacion de la informacion al termino de su parseo.
    """
    # Exit a parse tree produced by Objective_JSParser#funcAux.
    def exitFuncAux(self, ctx:Objective_JSParser.FuncAuxContext):
        if self.function_name in self.methods.getDirectory().keys():
            print("Function already defined")
            sys.exit(0)
            
        self.methods.create_table(self.function_name, InfoDirectory(None))
        self.methods.getTable(self.function_name).setParamTable(self.argumentos)
        self.methods.getTable(self.function_name).setAccessibility(self.accessible)
        if ctx.RETURNS() is None:
            self.does_returns = None
        else:
            self.does_returns = "returns"
            return_type = ctx.tipo_dato_no_list().getText()
            if return_type[0].isupper():
                print("Sorry we don't support returning objects")
                sys.exit()
            self.methods.getTable(self.function_name).setReturnType(self.normalizeTypes(return_type))


    # Enter a parse tree produced by Objective_JSParser#argumentosDecl.
    """
    Guarda los argumentos de una funcion un lugar correspondiente. Actualmente no soportamos objetos como argumentos
    """
    def enterArgumentosDecl(self, ctx:Objective_JSParser.ArgumentosDeclContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            if self.type[0].isupper():
                print("Sorry we don't support Objects as parameters")
                sys.exit()
            self.newArgument(id, self.type)

    # Exit a parse tree produced by Objective_JSParser#argumentosDecl.
    def exitArgumentosDecl(self, ctx:Objective_JSParser.ArgumentosDeclContext):
        pass

    """
    Agrega los argumentos de un constructor a la lista y reinicia las direcciones
    """
    def enterAddConsTable(self,  ctx:Objective_JSParser.AddConsTableContext):
        self.classes[self.className].addConstructorParams(self.argumentos)
        self.resetMemoryAddresses()
        self.argumentos = ParamTable()


    # Enter a parse tree produced by Objective_JSParser#argumentosDeclAux.
    """
    Verifica los tipos de los argumentos, actualmente no soportamos Objetos
    """
    def enterArgumentosDeclAux(self, ctx:Objective_JSParser.ArgumentosDeclAuxContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            if self.type[0].isupper():
                print("Sorry we don't support Objects as parameters")
                sys.exit()
            self.newArgument(id, self.type)

    # Exit a parse tree produced by Objective_JSParser#argumentosDeclAux.
    def exitArgumentosDeclAux(self, ctx:Objective_JSParser.ArgumentosDeclAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impConstructores.
    """
    Agrega la direccion de inicio de cada constructor
    """
    def enterImpConstructores(self, ctx:Objective_JSParser.ImpConstructoresContext):
        self.classes[self.className].addConstructorStartAddress(len(self.cuadruplos)+1)

    # Exit a parse tree produced by Objective_JSParser#impConstructores.
    """
    Limpia la tabla de funciones al termino de los constructor
    """
    def exitImpConstructores(self, ctx:Objective_JSParser.ImpConstructoresContext):
        self.methods = FunctionsDirectory()


    # Enter a parse tree produced by Objective_JSParser#impConstructor.
    """
    Verifica el nombre del constructor
    """
    def enterImpConstructor(self, ctx:Objective_JSParser.ImpConstructorContext):
        self.function_name = self.className
        if ctx.CLASSNAME().getText() != self.className:
            print("Function name: " + str(self.function_name)) 
            print("The constructor name is wrong")
            sys.exit()

    # Exit a parse tree produced by Objective_JSParser#impConstructor.
    def exitImpConstructor(self, ctx:Objective_JSParser.ImpConstructorContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#emptyRule.
    def enterEmptyRule(self, ctx:Objective_JSParser.EmptyRuleContext):
        pass

    def enterVerificaConstructores(self, ctx:Objective_JSParser.VerificaConstructoresContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#emptyRule.
    def exitEmptyRule(self, ctx:Objective_JSParser.EmptyRuleContext):
        pass

    # Enter a parse tree produced by Objective_JSParser#impFunc.
    """
    Guarda el nombre de la funcion
    """
    def enterImpFunc(self, ctx:Objective_JSParser.ImpFuncContext):
        if ctx.FUNCTION() is not None:
            self.function_name = ctx.ID().getText()

    # Exit a parse tree produced by Objective_JSParser#impFunc.
    def exitImpFunc(self, ctx:Objective_JSParser.ImpFuncContext):
        pass

    def exitDeleteFunctions(self, ctx:Objective_JSParser.DeleteFunctionsContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impFuncAux2.
    """
    Obten el el valor de retorno de una funcion. Actualmente no soportamos objetos
    """
    def enterImpFuncAux2(self, ctx:Objective_JSParser.ImpFuncAux2Context):
        if self.className is None and self.is_main_file:
            self.newFunction()
            if ctx.RETURNS() is None:
                self.does_returns = None
            elif self.className is None:
                self.does_returns = "returns"
                return_type = ctx.tipo_dato_no_list().getText()
                if return_type[0].isupper():
                    print("Sorry we don't support returning objects")
                    sys.exit()
                self.functions_directory.getTable(self.function_name).setReturnType(self.normalizeTypes(return_type))
            else:
                self.functions_directory.getTable(self.function_name).setReturnType(self.normalizeTypes(return_type))
            # quadruple = Quadruple(self.id, "endproc", None, None)
            # self.id += 1
            # self.cuadruplos.append(quadruple)
        elif self.is_main_file:
            self.newFunction()
            if ctx.RETURNS() is None:
                self.does_returns = None
            elif self.className is None:
                self.does_returns = "returns"
                return_type = ctx.tipo_dato_no_list().getText()
                if return_type[0].isupper():
                    print("Sorry we don't support returning objects")
                    sys.exit()
                self.functions_directory.getTable(self.function_name).setReturnType(self.normalizeTypes(return_type))
        else:
            if self.function_name in self.methods.getDirectory().keys():
                print("Function " + self.function_name + " already implemented")
                sys.exit(0)

            acc = self.classes[self.className].getMethods().getTable(self.function_name).getAccessibility()
            
            if ctx.RETURNS() is None:
                self.does_returns = None
                return_type = None
            else:
                self.does_returns = "returns"
                return_type = ctx.tipo_dato_no_list().getText()
                if return_type[0].isupper():
                    print("Sorry we don't support returning objects")
                    sys.exit()
                return_type = self.normalizeTypes(return_type)
            self.classes[self.className].verifyMethod(self.function_name, self.argumentos, return_type)
            self.methods.create_table(self.function_name, InfoDirectory(SymbolTable()))
            self.methods.getTable(self.function_name).setParamTable(self.argumentos)
            self.methods.getTable(self.function_name).setAccessibility(acc)
            self.methods.getTable(self.function_name).setReturnType(return_type)
            self.newFunction()

    # Exit a parse tree produced by Objective_JSParser#impFuncAux2.
    def exitImpFuncAux2(self, ctx:Objective_JSParser.ImpFuncAux2Context):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentos.
    """
    Agrega los argumentos de los constructores. Actualmente no soportamos objetos
    """
    def enterArgumentos(self, ctx:Objective_JSParser.ArgumentosContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            if self.type[0].isupper():
                print("Sorry we don't support Objects as parameters")
                sys.exit()
            self.newArgument(id, self.type)

    # Exit a parse tree produced by Objective_JSParser#argumentos.
    def exitArgumentos(self, ctx:Objective_JSParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentosAux.
    """
    Agrega los argumentos de los constructores. Actualmente no soportamos objetos
    """
    def enterArgumentosAux(self, ctx:Objective_JSParser.ArgumentosAuxContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            if self.type[0].isupper():
                print("Sorry we don't support Objects as parameters")
                sys.exit()
            self.newArgument(id, self.type)

    # Exit a parse tree produced by Objective_JSParser#argumentosAux.
    def exitArgumentosAux(self, ctx:Objective_JSParser.ArgumentosAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#bloqueConstructor.
    def enterBloqueConstructor(self, ctx:Objective_JSParser.BloqueConstructorContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueConstructor.
    """
    Genera el cuadruplo para la terminacion de los constructores
    """
    def exitBloqueConstructor(self, ctx:Objective_JSParser.BloqueConstructorContext):
        if ctx.SEMICOLON() is None:
            self.classes[self.className].verifyConstructorParams(self.argumentos)
            self.argumentos = ParamTable()
            self.resetMemoryAddresses()
            quadruple = Quadruple(self.id, "endproc", None, None, None)
            self.id += 1
            self.cuadruplos.append(quadruple)
            self.registros = 1


    # Enter a parse tree produced by Objective_JSParser#bloqueFunc.
    def enterBloqueFunc(self, ctx:Objective_JSParser.BloqueFuncContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueFunc.
    """
    Genera el cuadruplo para la terminacion de funciones
    """
    def exitBloqueFunc(self, ctx:Objective_JSParser.BloqueFuncContext):
        self.argumentos = ParamTable()
        quadruple = Quadruple(self.id, "endproc", None, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)
        self.registros = 1
        self.resetMemoryAddresses()
        self.function_name = None

    # Enter a parse tree produced by Objective_JSParser#bloqueFuncAux.
    def enterBloqueFuncAux(self, ctx:Objective_JSParser.BloqueFuncAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueFuncAux.
    def exitBloqueFuncAux(self, ctx:Objective_JSParser.BloqueFuncAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#bloqueFuncAux2.
    def enterBloqueFuncAux2(self, ctx:Objective_JSParser.BloqueFuncAux2Context):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueFuncAux2.
    """
    Remueve la informacion de la funcion al termino de su parseo. No es necesario almacenarla
    """
    def exitBloqueFuncAux2(self, ctx:Objective_JSParser.BloqueFuncAux2Context):
        if self.className is None:
            self.functions_directory.remove_info(self.function_name)
        self.function_name = None

    """
    Obten el valor de retorno de una funcion. Actualmetne no soportamos clases o nulos como valores de retornos
    """
    def enterGetReturnType(self, ctx):
        return_value = self.operandos.pop()
        if isinstance(return_value, str):
            if return_value[0] != "%":
                if (return_value == [] or return_value == "null") or 12000 <=return_value <= 12999:
                    print("Sorry, we don't support that datat type as return value")
                    sys.exit()
        else:
            if (return_value == [] or return_value == "null") or 12000 <=return_value <= 12999:
                print("Sorry, we don't support that datat type as return value")
                sys.exit()
        quadruple = Quadruple(self.id, "return", return_value, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)



    # Enter a parse tree produced by Objective_JSParser#preVars.
    def enterPreVars(self, ctx:Objective_JSParser.PreVarsContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#preVars.
    def exitPreVars(self, ctx:Objective_JSParser.PreVarsContext):
        self.isGlobalVar = False


    # Enter a parse tree produced by Objective_JSParser#vars_.
    """
    Obten el tipo de dato de una variabel
    """
    def enterVars_(self, ctx:Objective_JSParser.Vars_Context):
        id = ctx.ID().getText()
        self.type = ctx.tipo_dato().getText() 
        type_number = -1
        # Checar los tipos con sus respectivos números
        if self.type == "int":
            type_number = 0
        elif self.type == "float":
            type_number = 1
        elif self.type == "char":
            type_number = 2
        elif self.type == "string":
            type_number = 3
        elif self.type == "bool":
            type_number = 4
        elif self.type == "null":
            type_number = 5
        elif re.search("list(\[.*\])+int", self.type) is not None:
            type_number = 0
            self.is_arr_or_mat = True
        elif re.search("list(\[.*\])+float", self.type) is not None:
            type_number = 1
            self.is_arr_or_mat = True
        elif re.search("list(\[.*\])+char", self.type) is not None:
            type_number = 2
            self.is_arr_or_mat = True
        elif re.search("list(\[.*\])+string", self.type) is not None:
            type_number = 3
            self.is_arr_or_mat = True
        elif re.search("list(\[.*\])+bool", self.type) is not None:
            type_number = 4
            self.is_arr_or_mat = True
        elif self.type in self.classes:
            type_number = self.type
        else:
            sys.exit(0)

        self.newVars(id, type_number, self.is_arr_or_mat)

    """
    Agrega los argumentos de funciones a su lugar correspondiente
    """
    def newArgument(self, id, type):
        """
        Adds a new parameter into the parameter table
        """
        if id in self.argumentos.getParameters():
            print("Syntax error!! Variable: " + id + " is already defined")
            sys.exit(0)
        else:
            isList = False
            total_size = 1
            dimensions = []
            number_dimensions = 0
            if type == "int":
                type_number = 0
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_int_counter)
                self.current_local_int_counter += 1
            elif type == "float":
                type_number = 1
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_float_counter)
                self.current_local_float_counter += 1
            elif type == "char":
                type_number = 2
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_char_counter)
                self.current_local_char_counter += 1
            elif type == "string":
                type_number = 3
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_string_counter)
                self.current_local_string_counter += 1
            elif type == "bool":
                type_number = 4
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_boolean_counter)
                self.current_local_boolean_counter += 1
            elif type == "null":
                type_number = 5
                number_dimensions += 1
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_null_counter)
                self.current_local_null_counter += 1
            elif re.search("list(\[[0-9]+\])+int", type) is not None:
                type_number = 0
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_int_counter)
                if len(dimensions) == 2:
                    self.current_local_int_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_int_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+float", type) is not None:
                type_number = 1
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_float_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_float_counter)
                if len(dimensions) == 2:
                    self.current_local_float_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_float_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+char", type) is not None:
                type_number = 2
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_char_counter)
                if len(dimensions) == 2:
                    self.current_local_char_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_char_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+string", type) is not None:
                type_number = 3
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_string_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_string_counter)
                if len(dimensions) == 2:
                    self.current_local_string_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_string_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+bool", type) is not None:
                type_number = 4
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_boolean_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_boolean_counter)
                if len(dimensions) == 2:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound()) * (dimensions[1].getUpperBound())
                else:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+[A-Z][a-z]*", type) is not None:
                print("Sorry we don't support list of objects as parameters")
                sys.exit()

    # Exit a parse tree produced by Objective_JSParser#vars_.
    def exitVars_(self, ctx:Objective_JSParser.Vars_Context):
        pass


    # Enter a parse tree produced by Objective_JSParser#varsAux.
    """
    Agrega una nueva variable al directorio de funciones o de atributos correspondiente
    """
    def enterVarsAux(self, ctx:Objective_JSParser.VarsAuxContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.newVars(id, self.type, self.is_arr_or_mat)

    # Exit a parse tree produced by Objective_JSParser#varsAux.
    def exitVarsAux(self, ctx:Objective_JSParser.VarsAuxContext):
        self.is_arr_or_mat = False

    """
    Verifica si un tipo es lista
    """
    def isList(self, string):
        pos = string.find('list')
        return pos >= 0

    """
    Verifica si un tipo es int
    """
    def isInt(self, string):
        pos = string.find('int')
        return pos >= 0
    """
    Verifica si un tipo es float
    """
    def isFloat(self, string):
        pos = string.find('float')
        return pos >= 0
    """
    Verifica si un tipo es char
    """
    def isChar(self, string):
        pos = string.find('char')
        return pos >= 0

    """
    Verifica si un tipo es string
    """
    def isString(self, string):
        pos = string.find('string')
        return pos >= 0

    """
    Verifica si un tipo es boolean
    """
    def isBool(self, string):
        pos = string.find('bool')
        return pos >= 0


    # Enter a parse tree produced by Objective_JSParser#varsRepeated.
    """
    Verifica el tipo de datos de una variable
    """
    def enterVarsRepeated(self, ctx:Objective_JSParser.VarsRepeatedContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            type_number = -1
            # Checar los tipos con sus respectivos números
            if self.type == "int":
                type_number = 0
            elif self.type == "float":
                type_number = 1
            elif self.type == "char":
                type_number = 2
            elif self.type == "string":
                type_number = 3
            elif self.type == "bool":
                type_number = 4
            elif self.type == "null":
                type_number = 5
            elif self.isList(self.type) and self.isInt(self.type):
                type_number = 0
                self.is_arr_or_mat = True
            elif self.isList(self.type) and self.isFloat(self.type):
                type_number = 1
                self.is_arr_or_mat = True
            elif self.isList(self.type) and self.isChar(self.type):
                type_number = 2
                self.is_arr_or_mat = True
            elif self.isList(self.type) and self.isString(self.type):
                type_number = 3
                self.is_arr_or_mat = True
            elif self.isList(self.type) and self.isBool(self.type):
                type_number = 4
                self.is_arr_or_mat = True
            elif self.type in self.classes:
                type_number = self.type
            else:
                print("The type is not supported")
                sys.exit(0)
            self.newVars(id, type_number, self.is_arr_or_mat)

    # Exit a parse tree produced by Objective_JSParser#varsRepeated.
    def exitVarsRepeated(self, ctx:Objective_JSParser.VarsRepeatedContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#tipo_dato.
    def enterTipo_dato(self, ctx:Objective_JSParser.Tipo_datoContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#tipo_dato.
    def exitTipo_dato(self, ctx:Objective_JSParser.Tipo_datoContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#tipo_dato_list.
    """
    Set the variable, en este punto ya sabemos que es una lista
    """
    def enterTipo_dato_list(self, ctx:Objective_JSParser.Tipo_dato_listContext):
        self.isListDeclared = True

    # Exit a parse tree produced by Objective_JSParser#tipo_dato_list.
    """
    Ya se acabo la lista
    """
    def exitTipo_dato_list(self, ctx:Objective_JSParser.Tipo_dato_listContext):
        self.isListDeclared = False


    # Enter a parse tree produced by Objective_JSParser#dim.
    def enterDim(self, ctx:Objective_JSParser.DimContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#dim.
    def exitDim(self, ctx:Objective_JSParser.DimContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#dimMatrix.
    def enterDimMatrix(self, ctx:Objective_JSParser.DimMatrixContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#dimMatrix.
    def exitDimMatrix(self, ctx:Objective_JSParser.DimMatrixContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#tipo_dato_no_list.
    def enterTipo_dato_no_list(self, ctx:Objective_JSParser.Tipo_dato_no_listContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#tipo_dato_no_list.
    def exitTipo_dato_no_list(self, ctx:Objective_JSParser.Tipo_dato_no_listContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#tipo.
    def enterTipo(self, ctx:Objective_JSParser.TipoContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#tipo.
    def exitTipo(self, ctx:Objective_JSParser.TipoContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#estatuto.
    def enterEstatuto(self, ctx:Objective_JSParser.EstatutoContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#estatuto.
    def exitEstatuto(self, ctx:Objective_JSParser.EstatutoContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#asignacion.
    def enterAsignacion(self, ctx:Objective_JSParser.AsignacionContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#asignacion.
    """
    Obten el tipo de dato de la variable que queremos asignar y el del valor de la expresion si son posibles genera el cuadruplo correspondiente
    """
    def exitAsignacion(self, ctx:Objective_JSParser.AsignacionContext):
        valor = self.operandos.pop()
        id = self.getId(ctx.objeto().getText())
        variableType = None

        if self.operandos.empty():
            if id.find('.') != -1:
                id = id[5:]
                if id not in self.attributes.keys():
                    print("Var " + id + " used but not defined")
                    sys.exit(0)
                else:
                    address = self.attributes[id].getAddress()
                    variableType = self.attributes[id].getType()
                    variableType = self.convertTypeToInt(variableType)
            elif self.className is not None and  not self.is_main_file:
                if self.function_name == self.className: # Constructor
                    # Searching in the param table
                    for paramTable in self.classes[self.function_name].getConstructorParams():
                        for param, info in paramTable.getParameters().items():
                            if param == id:
                                address = info.getAddress()
                                variableType = info.getType()
                                variableType = self.convertTypeToInt(variableType)
                                break
                    for attributes, info in self.classes[self.function_name].getAttributes().items():
                        if id == attributes:
                            address = info.getAddress()
                            variableType = info.getType()
                            variableType = self.convertTypeToInt(variableType)
                            break
                elif id not in self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters().keys():
                    if id not in self.methods.getTable(self.function_name).getSymbolTable().getSymbols().keys():
                        print("Var " + id + " used but not defined")
                        sys.exit(0)
                    else:
                        table = self.methods.getTable(self.function_name).getSymbolTable().getSymbols()
                        address = table[id].getAddress()
                        variableType = table[id].getType()
                        variableType = self.convertTypeToInt(variableType)
                else:
                    table = self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters()
                    address = table[id].getAddress()
                    variableType = table[id].getType()
                    variableType = self.convertTypeToInt(variableType)
            else:
               address = self.getMemoryAddressFromVariable(id)
        else:
            address = self.operandos.pop()

        possibleType = self.types.pop()
        if variableType is None:
            variableType = self.getTypeFromVariable(id)
            variableType = self.convertTypeToInt(variableType)

        new_type = np.int64(self.oraculo.getDataType(variableType, 14, possibleType))
        if new_type == -1:
            print("Data type mismatch")
            sys.exit(0)

        cuadruplo = Quadruple(self.id, "=", valor, None, address)
        self.cuadruplos.append(cuadruplo)
        self.id += 1


    # Enter a parse tree produced by Objective_JSParser#condicion.
    def enterCondicion(self, ctx:Objective_JSParser.CondicionContext):
        self.pending_jumps.push(-1)

    # Exit a parse tree produced by Objective_JSParser#condicion.
    def exitCondicion(self, ctx:Objective_JSParser.CondicionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#endIf.
    def enterEndIf(self, ctx:Objective_JSParser.EndIfContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#endIf.
    """
    Llena todos los cuadruplos pendientes para la terminacion del if
    """
    def exitEndIf(self, ctx:Objective_JSParser.EndIfContext):
        end = self.pending_jumps.pop()
        while (end != -1):
            self.fill(end, len(self.cuadruplos)+1)
            end = self.pending_jumps.pop()
        if end == -1:
            self.pending_jumps.pop


    # Enter a parse tree produced by Objective_JSParser#exitIfExpresion.
    """
    Inicio de una expresion de IFs, guarda el valor y genera el cuadruplo GO.TOFALSE
    """
    def enterExitIfExpresion(self, ctx:Objective_JSParser.ExitIfExpresionContext):
        condition_type = self.types.pop()
        if condition_type != 4:
            print("The result of the expression must be boolean")
            sys.exit(0)

        condition = self.operandos.pop()
        quadruple = Quadruple(self.id, GO.TOFALSE, condition , None, None)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos) - 1)

    # Exit a parse tree produced by Objective_JSParser#exitIfExpresion.
    def exitExitIfExpresion(self, ctx:Objective_JSParser.ExitIfExpresionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#condicionAux.
    def enterCondicionAux(self, ctx:Objective_JSParser.CondicionAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#condicionAux.
    def exitCondicionAux(self, ctx:Objective_JSParser.CondicionAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#condicionChoice.
    def enterCondicionChoice(self, ctx:Objective_JSParser.CondicionChoiceContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#condicionChoice.
    def exitCondicionChoice(self, ctx:Objective_JSParser.CondicionChoiceContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#enterElse.
    def enterEnterElse(self, ctx:Objective_JSParser.EnterElseContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#enterElse.
    """
    Final de un bloque de if, sigue un ELSE, genera el cuadruplo GOTO para la terminacion del bloque.
    """
    def exitEnterElse(self, ctx:Objective_JSParser.EnterElseContext):
        quadruple = Quadruple(self.id, GO.TO, None, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)
        false = self.pending_jumps.pop()
        self.pending_jumps.push(len(self.cuadruplos) - 1)
        self.fill(false, len(self.cuadruplos)+1)


    # Enter a parse tree produced by Objective_JSParser#escritura.
    def enterEscritura(self, ctx:Objective_JSParser.EscrituraContext):
        pass

    """
    Genera el cuadruplo para imprimr una expresion
    """
    def enterPrintAfterExpresion(self, ctx:Objective_JSParser.EscrituraContext):
        exp = self.operandos.pop()
        quadruple = Quadruple(self.id, "print", exp, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)

    # Exit a parse tree produced by Objective_JSParser#escritura.
    def exitEscritura(self, ctx:Objective_JSParser.EscrituraContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#escrituraAux.
    def enterEscrituraAux(self, ctx:Objective_JSParser.EscrituraAuxContext):
        pass

    """
    Genera el cuadruplo para imprimr una expresion
    """
    def enterPrintAfterExpresionAux(self, ctx:Objective_JSParser.EscrituraAuxContext):
        quadruple = Quadruple(self.id, "print",  self.operandos.pop(), None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)

    # Exit a parse tree produced by Objective_JSParser#escrituraAux.
    def exitEscrituraAux(self, ctx:Objective_JSParser.EscrituraAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#ciclos.
    def enterCiclos(self, ctx:Objective_JSParser.CiclosContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#ciclos.
    def exitCiclos(self, ctx:Objective_JSParser.CiclosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#afterDo.
    def enterAfterDo(self, ctx:Objective_JSParser.AfterDoContext):
        pass

    """
    Asigna el cuadruplo del contador para el ciclo Do n times
    """
    # Exit a parse tree produced by Objective_JSParser#afterDo.
    def exitAfterDo(self, ctx:Objective_JSParser.AfterDoContext):
        cuadruplo = Quadruple(self.id, '=', "%1", None, self.current_temp_int_counter)
        self.operandos.push(self.current_temp_int_counter)
        self.while_jumps.push(self.current_temp_int_counter)
        self.current_temp_int_counter += 1
        self.cuadruplos.append(cuadruplo)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos) + 1)


    # Enter a parse tree produced by Objective_JSParser#afterCondition.
    def enterAfterCondition(self, ctx:Objective_JSParser.AfterConditionContext):
        pass

    """
    Genera el cuadruplo para cuando sea el termino de la condicion de un ciclo
    """
    # Exit a parse tree produced by Objective_JSParser#afterCondition.
    def exitAfterCondition(self, ctx:Objective_JSParser.AfterConditionContext):
        condition = self.operandos.pop()
        quadruple = Quadruple(self.id, GO.TOFALSE, condition, None, None)
        self.operandos.push(condition)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos)-1)


    # Enter a parse tree produced by Objective_JSParser#afterDoLoop.
    def enterAfterDoLoop(self, ctx:Objective_JSParser.AfterDoLoopContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#afterDoLoop.
    """
    Al final de cada ciclo incrementa el contador en + 1
    """
    def exitAfterDoLoop(self, ctx:Objective_JSParser.AfterDoLoopContext):
        registro = "r" + str(self.registros)
        addressIter = self.operandos.pop()
        dest = self.while_jumps.pop()
        self.while_jumps.push(dest)
        quadruple = Quadruple(self.id, '+', dest, "%1", self.current_temp_int_counter)
        self.operandos.push(self.current_temp_int_counter)
        self.types.push(0)
        self.current_temp_int_counter += 1
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.registros += 1

        registro = "r" + str(self.registros)

        address = self.operandos.pop()
        dest = self.while_jumps.pop()
        quadruple = Quadruple(self.id, '=', address, None, dest)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.registros += 1

        end = self.pending_jumps.pop()
        ret = self.pending_jumps.pop()
        quadruple = Quadruple(self.id, GO.TO, None, None, ret)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.fill(end, len(self.cuadruplos) + 1)



    # Enter a parse tree produced by Objective_JSParser#afterWhile.
    def enterAfterWhile(self, ctx:Objective_JSParser.AfterWhileContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#afterWhile.
    def exitAfterWhile(self, ctx:Objective_JSParser.AfterWhileContext):
        self.pending_jumps.push(len(self.cuadruplos))


    # Enter a parse tree produced by Objective_JSParser#afterWhileExpression.
    """
    Compara el resultado de la expresion del ciclo. Si es booleana genera el cuadruplo apropiado, en caso contrario fin del programa.
    """
    def enterAfterWhileExpression(self, ctx:Objective_JSParser.AfterWhileExpressionContext):
        condition = self.operandos.pop()
        exp_type = self.types.pop()
        if exp_type != 4:
            print("The result of the expression must be boolean")
            sys.exit(0)

        quadruple = Quadruple(self.id, GO.TOFALSE, condition, None, None)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos)-1)

    # Exit a parse tree produced by Objective_JSParser#afterWhileExpression.
    def exitAfterWhileExpression(self, ctx:Objective_JSParser.AfterWhileExpressionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#exitWhile.
    """
    Genera el cuadruplo GO.TO para regresar a la verificacion del while
    """
    def enterExitWhile(self, ctx:Objective_JSParser.ExitWhileContext):
        end = self.pending_jumps.pop()
        ret = self.pending_jumps.pop()
        quadruple = Quadruple(self.id, GO.TO, None, None, ret + 1)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.fill(end, len(self.cuadruplos) + 1)

    # Exit a parse tree produced by Objective_JSParser#exitWhile.
    def exitExitWhile(self, ctx:Objective_JSParser.ExitWhileContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#doAux.
    """
    Genera el cuadruplo de comparacion para la terminacion del ciclo DO n TImes
    """
    def enterDoAux(self, ctx:Objective_JSParser.DoAuxContext):
        if ctx.objeto() is not None:
            self.do_object = True
        elif ctx.TYPE_INT() is not None:
            cte = ctx.TYPE_INT().getText()
            registro = "r" + str(self.registros)
            # cuadruplo = Quadruple(self.id, '<=', 'temp-while', cte, registro)
            address = self.operandos.pop()
            cuadruplo = Quadruple(self.id, '<=', address, "%" + str(cte), self.current_temp_int_counter)
            # self.operandos.push(registro)
            self.operandos.push(self.current_temp_int_counter)
            self.types.push(0)
            self.registros += 1
            self.current_temp_int_counter += 1
            self.cuadruplos.append(cuadruplo)
            self.id += 1
        else:
            print("Do while parameter wrong")
            sys.exit(0)

    # Exit a parse tree produced by Objective_JSParser#doAux.
    def exitDoAux(self, ctx:Objective_JSParser.DoAuxContext):
        self.do_object = False


    # Enter a parse tree produced by Objective_JSParser#llamadaFunc.
    """
    Verifica la llamada funcion, si la funcion existe, y si proviene de un objeto genera el ERA apropiado.
    """
    def enterLlamadaFunc(self, ctx:Objective_JSParser.LlamadaFuncContext):
        self.call_from_instance = False
        if (len(ctx.ID()) == 2): # Check if you are trying to call a class method from a primitive
            var_type = self.functions_directory.getInfoDirectory(self.function_name).getContent(ctx.ID()[0].getText()).getType()
            if not isinstance(var_type, str):
                print("Trying to call a class method from a primitive")
                sys.exit(0)

        if (ctx.THIS() is not None or len(ctx.ID()) == 1) and ctx.CLASSNAME() is None: #Local method
            self.current_method_name = ctx.ID()[0].getText()
            if self.className is None or self.is_main_file:
                if self.current_method_name not in self.functions_directory.getDirectory():
                    print("The function: " + str(self.current_method_name)+ " doesn't exist")
                    sys.exit(0)
            else:
                if self.current_method_name not in self.methods.getDirectory():
                    print("The function: " + str(self.current_method_name)+ " doesn't exist")
                    sys.exit(0)
            quadruple = Quadruple(self.id, "ERA", self.current_method_name, None, None)
            self.id += 1
            self.cuadruplos.append(quadruple)
        elif ctx.THIS() is None and len(ctx.ID()) == 2 is not None: #Class method
            self.call_from_instance = True
            self.current_method_name = ctx.ID()[1].getText()
            var = ctx.ID()[0].getText()
            var_type = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getType()
            self.type = var_type
            if self.current_method_name not in self.classes[var_type].getMethods().getDirectory():
                print("The function: " + str(self.current_method_name) + " doesn't exist at class")
                sys.exit(0)

            if not self.classes[var_type].getMethods().getTable(self.current_method_name).getAccessibility():
                print(self.classes[var_type].getMethods().getTable(self.current_method_name).getAccessibility())
                print("Can't access private method " + str(self.current_method_name) + " from class " + type)
                sys.exit(0)
            object_address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getAddress()
            quadruple = Quadruple(self.id, "ERA", self.current_method_name, object_address, None)
            self.cuadruplos.append(quadruple)
            self.id += 1
        elif ctx.THIS() is None and len(ctx.ID()) == 1 and ctx.CLASSNAME() is not None: #Constructor
            var = ctx.ID()[0].getText()
            self.current_method_name = self.className
            self.object_address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getAddress()
            self.className = ctx.CLASSNAME().getText()
            var_type = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getType()
            if var_type != self.className:
                print("Error, trying to call a constructor from a different class")
                sys.exit()
            self.argumentos = ParamTable()

    """
    Almacena los argumentos de la llamada a constructores y obten su tipo
    """
    def exitStoreParamConstructor(self, ctx):
        id = self.operandos.pop()
        if self.function_name in self.functions_directory.getDirectory():
            if isinstance(id, str):
                if self.functions_directory.getInfoDirectory(self.function_name).getContent(id) == []:
                    var_type = self.types.pop()
                    var_type = self.convertIntToStringType(var_type)
                else:
                    var_type = self.functions_directory.getInfoDirectory(self.function_name).getContent(id).getType()
            else:
                var_type = self.types.pop()
                var_type = self.functions_directory.getInfoDirectory(self.function_name).getContent(self.getVarNameFromMemoryAddress(id)).getType()
                var_type = self.convertIntToStringType(var_type)
        self.newArgument(id, var_type)

    """
    Verifica que el constructor que estamos llamando este implementado correctamente.Si es asi, genera los cuadruplos para mandar a llamar al constructor
    """
    def exitVerifyConstructor(self, ctx):
        number_constructors = self.classes[self.className].getNumberOfConstructors()
        constructor = None
        for i in range(number_constructors):
            if self.classes[self.className].isConstructorCorrectlyImplemented(self.argumentos, i):
                constructor = i;
                break
        if constructor is None:
            print("No constructor was found that matched parameters")
            sys.exit()
        else:
            self.start_address = self.classes[self.className].getStartAddress(constructor)
            quadruple = Quadruple(self.id, "ERA", None, self.object_address, None)
            self.cuadruplos.append(quadruple)
            self.id += 1
            for (var1, info1), (var2, info2) in zip(self.argumentos.getParameters().items(), self.classes[self.className].getConstructorParam(constructor).getParameters().items()):
                if isinstance(var1, str):
                    if var1[0] == "%":
                        quadruple = Quadruple(self.id, "param", var1, info2.getListSize(), info2.getAddress())
                else:
                    quadruple = Quadruple(self.id, "param", var1, info2.getListSize(), info2.getAddress())
                self.cuadruplos.append(quadruple)
                self.id += 1
            quadruple = Quadruple(self.id, "GO.SUB", self.className, None, self.start_address)
            self.cuadruplos.append(quadruple)
            self.id += 1


    """
    Convierte los tipos de datos Strings a Int
    """
    def normalizeTypes(self, type):
        if isinstance(type, str):
            if type == "int":
                return 0
            elif type == "float":
                return 1
            elif type == "char":
                return 2
            elif type == "string":
                return 3
            elif type == "bool":
                return 4
            elif type == "null":
                return 5
            elif re.search("list(\[.*\])+int", type) is not None:
                return 0
            elif re.search("list(\[.*\])+float", type) is not None:
                return 1
            elif re.search("list(\[.*\])+char", type) is not None:
                return 2
            elif re.search("list(\[.*\])+string", type) is not None:
                return 3
            elif re.search("list(\[.*\])+bool", type) is not None:
                return 4
        return type

    # Exit a parse tree produced by Objective_JSParser#llamadaFunc.
    """
    Al termino del parseo de una funcion verifica los parametros y si hay error termina el programa. Si no genera los cuadruplos correspondientes.
    """
    def exitLlamadaFunc(self, ctx:Objective_JSParser.LlamadaFuncContext):
        var = ctx.ID()[0].getText()
        if self.object_address is None:
            if (len(ctx.ID()) > 1):
                type = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getType()
            else:
                type = self.className
            if self.current_method_name in self.functions_directory.getDirectory():
                if self.current_param_counter != len(self.functions_directory.getTable(self.current_method_name).getParams()):
                    print("The function call: " + self.current_method_name + " doesn't have the same number of arguments")
                    print(str(self.current_param_counter) + " were given, but " + str(len(self.functions_directory.getTable(self.current_method_name).getParams())) + " were expected")
                    sys.exit(0)
                start_address = self.functions_directory.getTable(self.current_method_name).getStartAddress()
                quadruple = Quadruple(self.id, GO.SUB, self.current_method_name, None, start_address)
                self.cuadruplos.append(quadruple)
                self.id += 1
                self.current_param_counter = 0
                if self.functions_directory.getTable(self.current_method_name).getReturnType() is not None:
                    return_type =  self.functions_directory.getTable(self.current_method_name).getReturnType()
                    self.saveReturnType(return_type, self.current_method_name, "None")
            elif self.current_method_name in self.classes[type].getMethods().getDirectory():
                if self.current_param_counter != len(self.classes[type].getMethods().getTable(self.current_method_name).getParams()):
                    print("The function call: " + self.current_method_name + " doesn't have the same number of arguments")
                    print(str(self.current_param_counter) + " were given, but " + str(len(self.classes[type].getMethods().getTable(self.current_method_name).getParams())) + " were expected")
                    sys.exit(0)
                start_address = self.classes[type].getMethods().getTable(self.current_method_name).getStartAddress()
                if start_address is None:
                    for name, info in self.methods.getDirectory().items():
                        if name == self.current_method_name:
                            start_address = info.getStartAddress()
                            break


                if self.object_address is None:
                    quadruple = Quadruple(self.id, GO.SUB, self.current_method_name, None, start_address)
                else:
                    quadruple = Quadruple(self.id, GO.SUB, self.className, None, start_address)
                self.cuadruplos.append(quadruple)
                self.id += 1
                self.current_param_counter = 0
                if self.classes[type].getMethods().getTable(self.current_method_name).getReturnType() is not None:
                    quadruple = Quadruple(self.id, "save_return", self.current_method_name, None, self.current_temp_int_counter)
                    self.operandos.push(self.current_temp_int_counter)
                    self.id += 1
                    self.current_temp_int_counter += 1
                    self.cuadruplos.append(quadruple)
        else:
            self.object_address = None


    # Enter a parse tree produced by Objective_JSParser#argumentosLlamada.
    """
    Agrega los fondos falsos para los parametros
    """
    def enterArgumentosLlamada(self, ctx:Objective_JSParser.ArgumentosLlamadaContext):
        self.operadores.push(')')

    # Exit a parse tree produced by Objective_JSParser#argumentosLlamada.
    """
    Elimina el fondo falso para los parametros
    """
    def exitArgumentosLlamada(self, ctx:Objective_JSParser.ArgumentosLlamadaContext):
        self.operadores.pop()


    # Enter a parse tree produced by Objective_JSParser#addArgument.
    def enterAddArgument(self, ctx:Objective_JSParser.AddArgumentContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#addArgument.
    """
    Actualiza el contador de parametros
    """
    def exitAddArgument(self, ctx:Objective_JSParser.AddArgumentContext):
        self.current_param_counter += 1


    # Enter a parse tree produced by Objective_JSParser#verifyArgument.
    def enterVerifyArgument(self, ctx:Objective_JSParser.VerifyArgumentContext):
        pass

    """
    Obten el nombre de una variable dada su direccion
    """
    def getVarNameFromMemoryAddress(self, address):
        for funtion_name, info in self.functions_directory.getDirectory().items():
            for var1, info2 in info.getSymbolTable().getSymbols().items():
                if address == info2.getAddress() and self.function_name == funtion_name:
                    return var1
        for var, info2 in self.functions_directory.getTable(self.function_name).getParamTable().getParameters().items():
            if address == info2.getAddress():
                return var
            # for var2, info3 in info.getParamTable().getParameters().items():
            #     print("Par: " + str(var2) + " with address: " + str(info3.getAddress()))
            #     if address == info3.getAddress() and funtion_name == self.current_method_name:
            #         return var2

    # Exit a parse tree produced by Objective_JSParser#verifyArgument.
    """
    Verifica el argumento que se esta mandando a una funcion. Si no corresponden termina el programaen caso contrario genera el cuadruplo correspondiente.
    """
    def exitVerifyArgument(self, ctx:Objective_JSParser.VerifyArgumentContext):
        if self.call_from_instance:
            table = self.classes[self.type].getMethods().getTable(self.current_method_name)
            directory = self.classes[self.type].getMethods().getDirectory()
        else:
            table = self.functions_directory.getTable(self.current_method_name)
            directory = self.functions_directory.getDirectory()

        argument = self.operandos.pop()
        argument_address = argument
        argument_type = self.types.pop()
        argument_type = self.normalizeTypes(argument_type)
        parameter = table.getParams()[self.current_param_counter][0]
        parameter_type = table.getParams()[self.current_param_counter][1]
        parameter_type = self.normalizeTypes(parameter_type)
        parameter_address = table.getParamTable().getAddress(parameter)
        dimensions_param = table.getParamTable().getParam(parameter).getRows()
        dimensions_argument = 0
        all_dimensions_argument = []
        argument = self.getVarNameFromMemoryAddress(argument)
        for key, value in directory.items():
            if argument in value.getSymbolTable().getSymbols():
                dimensions_argument = len(value.getSymbolTable().getContent(argument).getDimensions())
                all_dimensions_argument = value.getSymbolTable().getContent(argument).getDimensions()
                break
            if argument in value.getParamTable().getParameters():
                dimensions_argument = len(value.getParamTable().getParam(argument).getDimensions())
                all_dimensions_argument = value.getParamTable().getParam(argument).getDimensions()

        all_dimensions_param = table.getParamTable().getParam(parameter).getDimensions()
        if argument_type != parameter_type:
            print("The function " + str(self.current_method_name) + " was expecting an " + str(self.convertIntToStringType(parameter_type)) + " but received a " + str(self.convertIntToStringType(argument_type)))
            sys.exit(0)

        if dimensions_param != dimensions_argument:
            if dimensions_param > dimensions_argument:
                print("The function " + str(self.current_method_name) + " was expecting a matrix but received a list")
                sys.exit(0)
            else:
                print("The function " + str(self.current_method_name) + " was expecting a list but received a matrix")
            sys.exit(0)

        for dimP, dimA in zip(all_dimensions_param, all_dimensions_argument):
            if dimP.getUpperBound() != dimA.getUpperBound():
                if len(all_dimensions_argument) == 2:
                    print("The function " + str(self.current_method_name) + " was expecting a matrix of: " + str(all_dimensions_param[0].getUpperBound()) + " x " + str(all_dimensions_param[1].getUpperBound()) + " but received a matrix of: " + str(all_dimensions_argument[0].getUpperBound()) + " x " + str(all_dimensions_argument[1].getUpperBound()))
                    sys.exit(0)
                else:
                    print("The function " + str(self.current_method_name) + " was expecting a list of " + str(dimP.getUpperBound()) + " but received a list of " + str(dimA.getUpperBound()))
                sys.exit(0)

        size = table.getParamTable().getParam(parameter).getListSize()
        quadruple = Quadruple(self.id, "param", argument_address, size, parameter_address)
        #quadruple.print()
        self.cuadruplos.append(quadruple)
        self.id += 1



    # Enter a parse tree produced by Objective_JSParser#argumentosLlamadaAux.
    """
    Agrega un fondo falso para los parametros
    """
    def enterArgumentosLlamadaAux(self, ctx:Objective_JSParser.ArgumentosLlamadaAuxContext):
        pass
        self.operandos.push(')')

    # Exit a parse tree produced by Objective_JSParser#argumentosLlamadaAux.
    """
    Elimina el fondo falso de los parametros
    """
    def exitArgumentosLlamadaAux(self, ctx:Objective_JSParser.ArgumentosLlamadaAuxContext):
        pass
        self.operandos.pop()


    # Enter a parse tree produced by Objective_JSParser#lectura.
    def enterLectura(self, ctx:Objective_JSParser.LecturaContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#lectura.
    """
    general el cuadruplo correspondient ede lectura
    """
    def exitLectura(self, ctx:Objective_JSParser.LecturaContext):
        if self.operandos.empty():
            address = self.getMemoryAddressFromVariable(ctx.objeto().getText())
        else:
            address = self.operandos.pop()
            
        quadruple = Quadruple(self.id, "read", address, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)

        while not self.reads.empty():
            quadruple = self.reads.pop()
            self.cuadruplos.append(quadruple)


    # Enter a parse tree produced by Objective_JSParser#lecturaAux.
    def enterLecturaAux(self, ctx:Objective_JSParser.LecturaAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#lecturaAux.
    """
    Genera el cuadruplo correspondiente para lectura
    """
    def exitLecturaAux(self, ctx:Objective_JSParser.LecturaAuxContext):
        if ctx.INPUT_STREAM() is not None:
            if self.operandos.empty():
                address = self.getMemoryAddressFromVariable(ctx.objeto().getText())
            else:
                address = self.operandos.pop()
            
            quadruple = Quadruple(self.id, "read",  address, None, None)
            self.id += 1
            self.reads.push(quadruple)


    # Enter a parse tree produced by Objective_JSParser#decInc.
    """
    Realiza la verificacion  para realizar la operacion ++ o -- de una variable entera. En caso de error termina el programa en caso contrario genera el cuadruplo correspondiente
    """
    def enterDecInc(self, ctx:Objective_JSParser.DecIncContext):
        var = ctx.objeto().getText()
        if ctx.decIncAux().INCREMENT_OPERATOR() is not None:
            type = self.getTypeFromVariable(var)
            type = self.convertTypeToInt(type)
            new_type = np.int64(self.oraculo.getDataType(type, 0, 0))
            if new_type == -1:
                print("Data type mismatch")
                sys.exit(0)

            registro = "r" + str(self.registros)
            address = self.getMemoryAddressFromVariable(var)
            quadruple = Quadruple(self.id, '+', address, "%1", self.current_temp_int_counter)
            self.operandos.push(self.current_temp_int_counter)
            self.current_temp_int_counter += 1
            self.cuadruplos.append(quadruple)
            self.registros += 1
            self.id += 1


            registro = "r" + str(self.registros)
            quadruple = Quadruple(self.id, '=', self.operandos.pop(), None, address)
            self.cuadruplos.append(quadruple)
            self.registros += 1
            self.id += 1
        else:
            type = self.getTypeFromVariable(var)
            type = self.convertTypeToInt(type)
            new_type = np.int64(self.oraculo.getDataType(type, 1, 0))
            if new_type == -1:
                print("Data type mismatch")
                sys.exit(0)

            registro = "r" + str(self.registros)
            address = self.getMemoryAddressFromVariable(var)
            quadruple = Quadruple(self.id, '-', address, "%1", self.current_temp_int_counter)
            self.operandos.push(self.current_temp_int_counter)
            self.current_temp_int_counter += 1
            self.cuadruplos.append(quadruple)
            self.registros += 1
            self.id += 1


            registro = "r" + str(self.registros)
            quadruple = Quadruple(self.id, '=', self.operandos.pop(), None, address)
            self.cuadruplos.append(quadruple)
            self.registros += 1
            self.id += 1

    # Exit a parse tree produced by Objective_JSParser#decInc.
    def exitDecInc(self, ctx:Objective_JSParser.DecIncContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#decIncAux.
    def enterDecIncAux(self, ctx:Objective_JSParser.DecIncAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#decIncAux.
    def exitDecIncAux(self, ctx:Objective_JSParser.DecIncAuxContext):
        pass

    """
    Obten el Id de una lista o matriz
    """
    def getId(self, id):
        size = len(id)
        i = 0
        var = ""

        while(i < size):
            if(id[i] == '['):
                break
            else:
                var += id[i]
            i += 1
        return var


    """
    Verifica si un atributo existe
    """
    def isAttributeDeclared(self, id):
        self.classes[self.className].isAttribute(id)

    """
    Genera el cuadruplo correspondiente para el valor de retorno de una funcion
    """
    def saveReturnType(self, type, operand1, operand2):
        if type == 0: # int
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_int_counter)
            self.id += 1
            self.operandos.push(self.current_temp_int_counter)
            self.current_temp_int_counter += 1
            self.cuadruplos.append(quadruple)
        elif type == 1: # float
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_float_counter)
            self.id += 1
            self.operandos.push(self.current_temp_float_counter)
            self.current_temp_float_counter += 1
            self.cuadruplos.append(quadruple)
        elif type == 2: # char
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_char_counter)
            self.id += 1
            self.operandos.push(self.current_temp_char_counter)
            self.current_temp_char_counter += 1
            self.cuadruplos.append(quadruple)
        elif type == 3: # string
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_string_counter)
            self.id += 1
            self.operandos.push(self.current_temp_string_counter)
            self.current_temp_string_counter += 1
            self.cuadruplos.append(quadruple)
        elif type == 4: # boolean
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_boolean_counter)
            self.id += 1
            self.operandos.push(self.current_temp_boolean_counter)
            self.current_temp_boolean_counter += 1
            self.cuadruplos.append(quadruple)
        elif type == 5: # null
            quadruple = Quadruple(self.id, "save_return", operand1, operand2, self.current_temp_null_counter)
            self.id += 1
            self.operandos.push(self.current_temp_null_counter)
            self.current_temp_null_counter += 1
            self.cuadruplos.append(quadruple)

    # Enter a parse tree produced by Objective_JSParser#objeto.
    """
    Genera el cuadruplo correspondiente para el acceso a objetos
    """
    def enterObjeto(self, ctx:Objective_JSParser.ObjetoContext):
        if ctx.objetoAux() is not None:
            if ctx.objetoAux().LEFT_SQUARE_BRACKET() is not None:
                id = self.getId(ctx.objetoAux().getText())
                self.isVarDeclared(id)
            elif ctx.objetoAux().THIS() is not None:
                id = ctx.objetoAux().getText()[5:]
                self.isAttributeDeclared(id)
            else:
                id = ctx.objetoAux().getText()
                if len(ctx.objetoAux().ID()) == 2: # ID . ID
                    var = ctx.objetoAux().ID()[0].getText()
                    old_class_name = self.className
                    self.className = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getType()
                    attribute = ctx.objetoAux().ID()[1].getText()
                    self.isAttributeDeclared(attribute)
                    if not self.classes[self.className].getAttributes()[attribute].isAccessible():
                        print("Can't access private attribute " + attribute + " from class " + self.className)
                        sys.exit(0)
                    var_address = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getAddress()
                    attribute_address = self.classes[self.className].getAttributes()[attribute].getAddress()
                    attribute_type = self.classes[self.className].getAttributes()[attribute].getType()
                    self.className = old_class_name
                    if attribute_type == 0:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_int_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    elif attribute_type == 1:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_float_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    elif attribute_type == 2:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_char_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    elif attribute_type == 3:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_string_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    elif attribute_type == 4:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_boolean_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    elif attribute_type == 5:
                        quadruple = Quadruple(self.id, "attribute_access", var_address, attribute_address, self.current_temp_null_counter)
                        self.id += 1
                        self.cuadruplos.append(quadruple)
                    self.saveReturnType(attribute_type, var_address, attribute_address)
                elif self.className is None:
                    self.isVarDeclared(id)
                else:
                    if self.function_name == self.className:
                        # TODO(jorge o santiago): Checar si el objeto existe en la tabla de constructores
                        pass
                    elif self.function_name != "main" and self.className is not None:
                        if self.function_name in self.classes[self.className].getMethods().getDirectory():
                            if id not in self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters().keys():
                                if id not in self.methods.getTable(self.function_name).getSymbolTable().getSymbols().keys():
                                    print("Var " + id + " used but not defined")
                                    sys.exit(0)

            if self.do_object:
                type = self.getTypeFromVariable(id)
                type = self.convertTypeToInt(type)
                new_type = np.int64(self.oraculo.getDataType(type, 9, 0))
                if new_type == -1:
                    print("Data type mismatch")
                    sys.exit(0)

                registro = "r" + str(self.registros)
                cuadruplo = Quadruple(self.id, '<=', 'temp-while', id, registro)
                self.operandos.push(registro)
                self.registros += 1
                self.cuadruplos.append(cuadruplo)
                self.id += 1

    # Exit a parse tree produced by Objective_JSParser#objeto.
    def exitObjeto(self, ctx:Objective_JSParser.ObjetoContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#objetoAux.
    def enterObjetoAux(self, ctx:Objective_JSParser.ObjetoAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#objetoAux.
    def exitObjetoAux(self, ctx:Objective_JSParser.ObjetoAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#megaExpresion.
    def enterMegaExpresion(self, ctx:Objective_JSParser.MegaExpresionContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#megaExpresion.
    def exitMegaExpresion(self, ctx:Objective_JSParser.MegaExpresionContext):
        pass

    """
    Agrega ^ a la pila de operaadores
    """
    def enterHyperExpresionAux(self, ctx):
        if ctx.POWER_OPERATOR() is not None:
            self.operadores.push('^')

    """
    Si hay una operacion ^ pendiente resolverla, si el tipo de dato no coresponde termina el programa
    """
    def exitHyperExpresionAux(self, ctx):
        if self.operadores.top() == '^':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()
            number_op = 4


            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))

            if new_type == -1:
                print("Data type mismatch")
                sys.exit(0)
            else:
                registro = "r" + str(self.registros)
                self.types.push(new_type)
                if new_type == 0: #int
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_int_counter)
                    self.operandos.push(self.current_temp_int_counter)
                    self.current_temp_int_counter += 1
                else: #Float
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_float_counter)
                    self.operandos.push(self.current_temp_float_counter)
                    self.current_temp_float_counter += 1
                self.cuadruplos.append(cuadruplo)
                self.id += 1
                self.registros += 1



    # Enter a parse tree produced by Objective_JSParser#megaExpresionAux.
    """
    Agrega && o || a la pila de operadoress
    """
    def enterMegaExpresionAux(self, ctx:Objective_JSParser.MegaExpresionAuxContext):
        if ctx.LOGICAL_AND_OPERATOR() is not None:
            self.operadores.push('&&')
        elif ctx.LOGICAL_OR_OPERATOR() is not None:
            self.operadores.push('||')

    # Exit a parse tree produced by Objective_JSParser#megaExpresionAux.
    """
    Si hay una operacion && o || pendiente resuelvela. Si hay un error termina la ejecuion del programa
    """
    def exitMegaExpresionAux(self, ctx:Objective_JSParser.MegaExpresionAuxContext):
        if self.operadores.top() == '&&' or self.operadores.top() == '||':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()
            if operador == '&&':
                number_op = 12
            elif operador == '||':
                number_op = 13

            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))

            if new_type == -1.0:
                print("Data type mismatch")
                sys.exit(0)
            else:
                self.operandos.push(self.current_temp_boolean_counter)
                self.types.push(new_type)
                cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_boolean_counter)
                self.current_temp_boolean_counter += 1
                self.cuadruplos.append(cuadruplo)
                self.registros += 1
                self.id += 1


    # Enter a parse tree produced by Objective_JSParser#superExpresion.
    def enterSuperExpresion(self, ctx:Objective_JSParser.SuperExpresionContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#superExpresion.
    def exitSuperExpresion(self, ctx:Objective_JSParser.SuperExpresionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#superExpresionOperadores.
    """
    Agrega el operador relacional correspondiente a la pila de operadores
    """
    def enterSuperExpresionOperadores(self, ctx:Objective_JSParser.SuperExpresionOperadoresContext):
        if ctx.GREATER_THAN_OPERATOR() is not None:
            self.operadores.push('>')
        elif ctx.GREATER_OR_EQUAL_THAN_OPERATOR() is not None:
            self.operadores.push('>=')
        elif ctx.LESS_THAN_OPERATOR() is not None:
            self.operadores.push('<')
        elif ctx.LESS_THAN_OR_EQUAL_OPERATOR() is not None:
            self.operadores.push('<=')
        elif ctx.NOT_EQUAL_OPERATOR() is not None:
            self.operadores.push('!=')
        elif ctx.EQUAL_OPERATOR() is not None:
            self.operadores.push('==')

    # Exit a parse tree produced by Objective_JSParser#superExpresionOperadores.
    """
    Si hay un operador relacional pendiente resuelvelo. Si hay un error termina el programa
    """
    def exitSuperExpresionOperadores(self, ctx:Objective_JSParser.SuperExpresionOperadoresContext):
        if self.operadores.top() == '>' or self.operadores.top() == '>=' or self.operadores.top() == '<' or self.operadores.top() == '<=' or self.operadores.top() == '!=' or self.operadores.top() == '==':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()

            if operador == '>':
                number_op = 6
            elif operador == '<':
                number_op = 7
            elif operador == '>=':
                number_op = 8
            elif operador == '<=':
                number_op = 9
            elif operador == '==':
                number_op = 10
            elif operador == '!=':
                number_op = 11

            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))
            if new_type == -1.0:
                print("Data type mismatch")
                sys.exit(0)
            elif tipo1 == 5 and number_op == 10:
                self.operandos.push(self.current_temp_boolean_counter)
                self.types.push(new_type)
                cuadruplo = Quadruple(self.id, "isNull", operando1, None, self.current_temp_boolean_counter)
                self.current_temp_boolean_counter += 1
                self.cuadruplos.append(cuadruplo)
                self.registros += 1
                self.id += 1
            elif tipo1 == 5 and number_op == 11:
                self.operandos.push(self.current_temp_boolean_counter)
                self.types.push(new_type)
                cuadruplo = Quadruple(self.id, "isNotNull", operando1, None, self.current_temp_boolean_counter)
                self.current_temp_boolean_counter += 1
                self.cuadruplos.append(cuadruplo)
                self.registros += 1
                self.id += 1
            else:
                self.operandos.push(self.current_temp_boolean_counter)
                self.types.push(new_type)
                cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_boolean_counter)
                self.current_temp_boolean_counter += 1
                self.cuadruplos.append(cuadruplo)
                self.registros += 1
                self.id += 1


    # Enter a parse tree produced by Objective_JSParser#expresion.
    def enterExpresion(self, ctx:Objective_JSParser.ExpresionContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#expresion.
    def exitExpresion(self, ctx:Objective_JSParser.ExpresionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#expresionOperadores.
    """
    Agrega el operador + o - a la pila de operadores
    """
    def enterExpresionOperadores(self, ctx:Objective_JSParser.ExpresionOperadoresContext):
        if ctx.SUM_OPERATOR() is not None: 
            self.operadores.push('+')
        elif ctx.SUBSTRACTION_OPERATOR() is not None:
            self.operadores.push('-')

    # Exit a parse tree produced by Objective_JSParser#expresionOperadores.
    def exitExpresionOperadores(self, ctx:Objective_JSParser.ExpresionOperadoresContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#termino.
    def enterTermino(self, ctx:Objective_JSParser.TerminoContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#termino.
    """
    Si hay una + o una - pendiente resuelvela y agregala a la pila de operadores
    """
    def exitTermino(self, ctx:Objective_JSParser.TerminoContext):
        if self.operadores.top() == '+' or self.operadores.top() == '-':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()
            if operador == '+':
                number_op = 0
            else:
                number_op = 1

            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))
            if new_type == -1.0:
                print("Data type mismatch")
                sys.exit(0)
            else:
                if new_type == 0: # Int
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_int_counter)
                    self.operandos.push(self.current_temp_int_counter)
                    self.current_temp_int_counter += 1
                elif new_type == 1: # Float
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_float_counter)
                    self.operandos.push(self.current_temp_float_counter)
                    self.current_temp_float_counter += 1
                elif new_type == 2: # Char
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_char_counter)
                    self.operandos.push(self.current_temp_char_counter)
                    self.current_temp_char_counter += 1
                elif new_type == 3: # String
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_string_counter)
                    self.operandos.push(self.current_temp_string_counter)
                    self.current_temp_string_counter += 1
                registro = "r" + str(self.registros)
                # self.operandos.push(registro)
                self.types.push(new_type)
                self.cuadruplos.append(cuadruplo)
                self.registros += 1
                self.id += 1



    # Enter a parse tree produced by Objective_JSParser#terminoOperadores.
    """
    Si hay una *, / o % agregalo a la pila de operadores
    """
    def enterTerminoOperadores(self, ctx:Objective_JSParser.TerminoOperadoresContext):
        if ctx.MULTIPLICATION_OPERATOR() is not None:
            self.operadores.push('*')
        elif ctx.DIVISION_OPERATOR() is not None:
            self.operadores.push('/')
        elif ctx.MODULUS_OPERATOR() is not None:
            self.operadores.push('%')

    # Exit a parse tree produced by Objective_JSParser#terminoOperadores.
    def exitTerminoOperadores(self, ctx:Objective_JSParser.TerminoOperadoresContext):
        pass

    # Enter a parse tree produced by Objective_JSParser#factor.
    """
    Verifica si el factor existe, y si lo podemos acceder
    """
    def enterFactor(self, ctx:Objective_JSParser.FactorContext):
        address = None
        if ctx.varCte() is not None:
            if ctx.varCte().llamadaFunc() is not None:
                if ctx.varCte().llamadaFunc().THIS() is None and len(ctx.varCte().llamadaFunc().ID()) == 2:
                    self.call_from_instance = True
                    self.current_method_name = ctx.varCte().llamadaFunc().ID()[1].getText()
                    var = ctx.varCte().llamadaFunc().ID()[0].getText()
                    type = self.functions_directory.getInfoDirectory(self.function_name).getContent(var).getType()
                    self.type = type
                    if self.current_method_name not in self.classes[type].getMethods().getDirectory():
                        print("The function: " + str(self.current_method_name) + " doesn't exist at class")
                        sys.exit(0)
                    if not self.classes[type].getMethods().getTable(self.current_method_name).getAccessibility():
                        print("Can't access private method " + str(self.current_method_name) + " from class " + type)
                        sys.exit(0)
                    object_address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getAddress()
                    # quadruple = Quadruple(self.id, "ERA", self.current_method_name, object_address, None)
                    # self.cuadruplos.append(quadruple)
                    # self.id += 1
                else:
                    function_name = ctx.varCte().getText().split('(')[0]
                    if not self.isFunctionDeclared(function_name):
                        print("The function: " + str(function_name) + " doesn't exist")
                        sys.exit(0)
                    else:
                        return_type = self.functions_directory.getTable(function_name).getReturnType()
                        self.types.push(return_type)
            elif ctx.varCte() is not None and ctx.varCte().TYPE_STRING() is None and ctx.varCte().TYPE_CHAR() is None:
                value = ctx.varCte().getText()
                if value.find('.') != -1 and self.className is not None and value[0] == 't':
                    value = value[5:]
                    self.classes[self.className].isAttribute(value)
                    type = self.attributes[value].getType()
                    type = self.convertTypeToInt(type)
                    address = self.attributes[value].getAddress()
                elif self.className is not None and ctx.varCte().TYPE_INT() is None and ctx.varCte().TYPE_FLOAT() is None and self.function_name != "main" and ctx.varCte().NULL() is None:
                    if self.function_name == self.className: # Constructor
                        address_found = False
                        for paramTable in self.classes[self.function_name].getConstructorParams():
                            for param, info in paramTable.getParameters().items():
                                if param == value:
                                    address = info.getAddress()
                                    type = info.getType()
                                    type = self.convertTypeToInt(type)
                                    address_found = True
                                    break
                            if address_found:
                                break
                        if not address_found:
                            for attributes, info in self.classes[self.function_name].getAttributes().items():
                                if value == attributes:
                                    address = info.getAddress()
                                    type = info.getType()
                                    type = self.convertTypeToInt(type)
                                    break
                    elif value in self.classes[self.className].getMethods().getDirectory():
                        if value not in self.methods.getTable(self.function_name).getSymbolTable().getSymbols().keys():
                            print("Var " + value + " used but not defined")
                            sys.exit(0)
                        else:
                            table = self.methods.getTable(self.function_name).getSymbolTable().getSymbols()
                            type = table[value].getType()
                            type = self.convertTypeToInt(type)
                            address = table[value].getAddress()
                    else:
                        if self.function_name in self.functions_directory.getDirectory():
                            if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(value) != []:
                                type = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(value).getType()
                                type = self.convertTypeToInt(type)
                                address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(value).getAddress()
                            elif self.functions_directory.getTable(self.function_name).getParamTable().getParam(value) != []:
                                type = self.functions_directory.getTable(self.function_name).getParamTable().getParam(value).getType()
                                type = self.convertTypeToInt(type)
                                address =self.functions_directory.getTable(self.function_name).getParamTable().getParam(value).getAddress()
                            else:
                                print("Var " + value + " used but not defined")
                                sys.exit(0)
                        else:
                            table = self.classes[self.className].getMethodTable(self.function_name).getParamTable().getParameters()
                            table2 = self.classes[self.className].getMethodTable(self.function_name).getSymbolTable().getSymbols()
                            if table == {}:
                                for attribute, info in self.classes[self.className].getAttributes().items():
                                    if attribute == value:
                                        type = info.getType()
                                        type = self.convertTypeToInt(type)
                                        address = info.getAddress()
                            else:
                                if value in table:
                                    type = table[value].getType()
                                    address = table[value].getAddress()
                                else:
                                    type = table2[value].getType()
                                    address = table2[value].getAddress()

                                type = self.convertTypeToInt(type)
                elif ctx.varCte().NULL() is not None:
                    type = 5
                else:
                    type = self.getTypeFromFactor(ctx, value)
                    type = self.convertTypeToInt(type)
                    
                try:
                    number = int(value)
                    self.operandos.push('%'+str(number))
                    self.current_local_int_counter += 1
                except ValueError:
                    try:
                        number = float(value)
                        self.operandos.push('%'+str(number))
                        self.current_local_float_counter += 1
                    except ValueError:
                        if value == "true":
                            self.operandos.push('%'+str(value))
                            self.current_local_boolean_counter += 1
                        elif value == "false":
                            self.operandos.push('%'+str(value))
                            self.current_local_boolean_counter += 1
                        elif type == 0:
                            if address is None:
                                address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_int_counter += 1
                        elif type == 1:
                            if address is None:
                                address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_float_counter += 1
                        elif type == 2:
                            if address is None:
                                address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_char_counter += 1
                        elif type == 3:
                            if address is None:
                                address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_string_counter += 1
                        elif type == 4:
                            if address is None:
                                address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_boolean_counter += 1
                        elif type == 5:
                            if ctx.varCte().NULL() is None:
                                if address is None:
                                    address = self.getMemoryAddressFromVariable(value)
                                self.operandos.push(address)
                            else:
                                self.operandos.push("null")
                            # self.current_local_null_counter += 1
                self.types.push(type)
            elif ctx.factorParentesis() is not None:
                # Fondo falso
                self.operadores.push('(')
            elif not self.isListDeclared:
                value = ctx.varCte().getText()
                self.operandos.push("%" + value)

                type = self.getTypeFromFactor(ctx, value)
                type = self.convertTypeToInt(type)
                self.types.push(type)

    # Exit a parse tree produced by Objective_JSParser#factor.
    """
    Si hay un operador * o / pendiente resuelvelo. Si la operacion es incorrecta termina el programa.
    """
    def exitFactor(self, ctx:Objective_JSParser.FactorContext):
        if self.operadores.top() == '/' or self.operadores.top() == '*' or self.operadores.top() == '%':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()

            if operador == '/':
                number_op = 3
            elif operador == '*':
                number_op = 2
            else:
                number_op = 5

            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))

            if new_type == -1:
                print("Data type mismatch")
                sys.exit(0)
            else:
                registro = "r" + str(self.registros)
                # self.operandos.push(registro)
                self.types.push(new_type)
                if new_type == 0: #int
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_int_counter)
                    self.operandos.push(self.current_temp_int_counter)
                    self.current_temp_int_counter += 1
                else: #Float
                    cuadruplo = Quadruple(self.id, operador, operando1, operando2, self.current_temp_float_counter)
                    self.operandos.push(self.current_temp_float_counter)
                    self.current_temp_float_counter += 1
                # cuadruplo = Quadruple(self.id, operador, operando1, operando2, registro)
                self.cuadruplos.append(cuadruplo)
                #cuadruplo.print()
                self.id += 1
                self.registros += 1

    # Enter a parse tree produced by Objective_JSParser#factorParentesis.
    def enterFactorParentesis(self, ctx:Objective_JSParser.FactorParentesisContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#factorParentesis.
    """
    Elimina el fondo falso
    """
    def exitFactorParentesis(self, ctx:Objective_JSParser.FactorParentesisContext):
        self.operadores.pop()


    # Enter a parse tree produced by Objective_JSParser#varCte.
    def enterVarCte(self, ctx:Objective_JSParser.VarCteContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#varCte.
    def exitVarCte(self, ctx:Objective_JSParser.VarCteContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#matrix.
    def enterMatrix(self, ctx:Objective_JSParser.MatrixContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#matrix.
    def exitMatrix(self, ctx:Objective_JSParser.MatrixContext):
        pass

    """
    Verifica si un ID es una matriz o lista
    """
    def enterVerifica_id(self, ctx:Objective_JSParser.Verifica_idContext):
        id = ctx.ID().getText()
        self.isVarDeclared(id)
        dimensions = self.getDimsFromVariable(id)

        if(len(dimensions) == 0):
            print("Var " + id + " is not an array or matrix")
            sys.exit(0)

        self.ids.push(id)
        self.dims.push(1)

        type = self.normalizeTypes(self.getTypeFromVariable(id))
        self.types.push(type)
        self.operadores.push('[')

    """
    Verifica la primera indexacion de una lista o matriz
    """
    def enterVerifica_dim1(self, ctx:Objective_JSParser.Verifica_dim1Context):
        id = self.ids.top()
        dim = self.dims.top()
        dimensions = self.getDimsFromVariable(id)

        if self.types.top() != 0:
            print("The index of the var " + id + " is not an integer")
            sys.exit(0)

        cuadruplo = Quadruple(self.id, 'VER', self.operandos.top(), "%" + str(0), "%" + str(dimensions[0].getUpperBound()))
        self.cuadruplos.append(cuadruplo)
        self.id += 1

    """
    Verifica un arreglo, si es correcto sumale la direccion base
    """
    def enterVerifica_arreglo(self, ctx:Objective_JSParser.Verifica_arregloContext):
        id = self.ids.pop()
        dim = self.dims.pop()
        dimensions = self.getDimsFromVariable(id)

        if(len(dimensions) != dim):
            print("The var " + id + " is not of size 1")
            sys.exit(0)

        aux = self.operandos.pop()
        self.types.pop()

        cuadruplo = Quadruple(self.id, "+", aux, "%" + str(self.getMemoryAddressFromVariable(id)), self.current_temp_int_counter)
        self.cuadruplos.append(cuadruplo)
        self.id += 1

        self.operandos.push("(" + str(self.current_temp_int_counter) + ")")
        self.types.push(0)
        self.current_temp_int_counter += 1

        self.operadores.pop()

    """
    Verifica la indexacion de la matriz, y multiplicalo por el indice pasado para generar el salto.
    """
    def enterMatriz_aux(self, ctx:Objective_JSParser.Matriz_auxContext):
        id = self.ids.pop()
        dim = self.dims.pop()
        dimensions = self.getDimsFromVariable(id)

        type = self.types.pop()
        aux = self.operandos.pop()

        if type != 0:
            print("The index of the var " + id + " is not an integer")
            sys.exit(0)

        cuadruplo = Quadruple(self.id, '*', aux, "%" + str(dimensions[0].getM()-1), self.current_temp_int_counter)
        self.cuadruplos.append(cuadruplo)
        self.id += 1
        self.operandos.push(self.current_temp_int_counter)
        self.types.push(0)
        self.current_temp_int_counter += 1

        dim += 1
        self.ids.push(id)
        self.dims.push(dim)

    """
    Verifica la segunda dimension de una matriz
    """
    def enterVerifica_dim2(self, ctx:Objective_JSParser.Verifica_dim2Context):
        id = self.ids.pop()
        dim = self.dims.pop()
        dimensions = self.getDimsFromVariable(id)

        if dim != len(dimensions):
            print("The var " + id + " is not of size 2")
            sys.exit(0)

        aux2 = self.operandos.pop()
        type = self.types.pop()
        aux1 = self.operandos.pop()
        # self.types.pop()

        if type != 0:
            print("The index of the var " + id + " is not an integer")
            sys.exit(0)

        cuadruplo = Quadruple(self.id, 'VER', aux2,"%" + str(0), "%" + str(dimensions[1].getUpperBound()))
        self.cuadruplos.append(cuadruplo)
        self.id += 1

        cuadruplo = Quadruple(self.id, "+", aux1, aux2, self.current_temp_int_counter)
        self.cuadruplos.append(cuadruplo)
        self.id += 1
        self.operandos.push(self.current_temp_int_counter)
        self.current_temp_int_counter += 1

        aux = self.operandos.pop()
        cuadruplo = Quadruple(self.id, "+", aux, "%" + str(self.getMemoryAddressFromVariable(id)), self.current_temp_int_counter)
        self.cuadruplos.append(cuadruplo)
        self.id += 1
        self.operandos.push("(" + str(self.current_temp_int_counter) + ")")
        self.types.push(0)
        self.current_temp_int_counter += 1

        self.operadores.pop()

    def exitGetValue(self, ctx):
        pass