# Generated from Objective_JS.g4 by ANTLR 4.7.1
from antlr4 import *

import sys
import re
import numpy as np
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
CONST_TEMPORAL_TOP_NULL = 17999


# This class defines a complete listener for a parse tree produced by Objective_JSParser.
class Objective_JSListener(ParseTreeListener):

    def __init__(self):
        self.functions_directory = FunctionsDirectory()
        self.type = None
        # Default visibility
        self.visibility = "private"
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
        (I don't understand this function Santiago did it)
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
        # for key, value in self.functions_directory.getDirectory().items():
        #     print("Function: " + str(key))
        #     for key2, value2 in value.getSymbolTable().getSymbols().items():
        #         print("Var: " + str(key2))
        #         print("Address: " + str(value2.getAddress()))
        if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var):
            address = self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getAddress()
            return address
        elif self.functions_directory.getTable(self.function_name).getParamTable().getParam(var):
            return self.functions_directory.getTable(self.function_name).getParamTable().getAddress(var)
        # Then check in the global scope
        for key, value in self.functions_directory.getDirectory().items():
            if var in value.getSymbolTable().getSymbols():
                return value.getSymbolTable().getContent(var).getAddress()

    def newClass(self, className):
        """
        Create a new class in the funtion
        """
        self.function_name = className
        self.functions_directory.create_table(self.function_name, InfoDirectory())

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
            dimensions[0].setM(dimensions[1].getUpperBound())
            dimensions[1].setM(0)
        else: # List
            dimensions[0].setM(0)
        return totalSize, number_dimensions, dimensions

    def newVars(self, id, type, visibility):
        """
        Adds a new variable into the function_directory
        """
        if id in self.functions_directory.getTable(self.function_name).getSymbolTable().getSymbols().items():
            print("Syntax error!! Variable: " + id + " is already defined")
            sys.exit(0)

        isList = False
        total_size = 1
        dimensions = []
        number_dimensions = 0
        if type == "int" or type == 0:
            number_dimensions += 1
            self.functions_directory.addInt(self.function_name, False, 1)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_int_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_global_int_counter += 1
            else:
                # print(id + " - " + str(self.current_local_int_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_int_counter += 1
        elif type == "float" or type == 1:
            number_dimensions += 1
            self.functions_directory.addFloat(self.function_name, False, 1)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_float_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_global_float_counter += 1
            else:
                # print(id + " - " + str(self.current_local_float_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_float_counter += 1
        elif type == "char" or type == 2:
            number_dimensions += 1
            self.functions_directory.addChar(self.function_name, False, 1)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_char_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_global_char_counter += 1
            else:
                # print(id + " - " + str(self.current_local_char_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_char_counter += 1
        elif type == "string" or type == 3:
            number_dimensions += 1
            self.functions_directory.addString(self.function_name, False, 1)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_string_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_string_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_global_string_counter += 1
            else:
                # print(id + " - " + str(self.current_local_string_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_string_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_string_counter += 1
        elif type == "bool" or type == 4:
            number_dimensions += 1
            self.functions_directory.addBool(self.function_name, False, 1)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_bool_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_global_boolean_counter += 1
            else:
                # print(id + " - " + str(self.current_local_boolean_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
                self.current_local_boolean_counter += 1
        elif re.search("list(\[.*\])+int", type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(type)
            isList = True
            self.functions_directory.addInt(self.function_name, False, total_size)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_int_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_int_counter, id, type, isList, total_size, number_dimensions, dimensions)
            else:
                # print(id + " - " + str(self.current_local_int_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_int_counter, id, type, isList, total_size, number_dimensions, dimensions)

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
        elif re.search("list(\[.*\])+float", type) is not None:
            isList = True
            total_size, number_dimensions, dimensions = self.parseList(type)
            self.functions_directory.addFloat(self.function_name, False, total_size)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_float_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_float_counter, id, type, isList, total_size, number_dimensions, dimensions)
            else:
                # print(id + " - " + str(self.current_local_float_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_float_counter, id, type, isList, total_size, number_dimensions, dimensions)

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
        elif re.search("list(\[.*\])+char", type) is not None:
            isList = True
            total_size, number_dimensions, dimensions = self.parseList(type)
            self.functions_directory.addChar(self.function_name, False, total_size)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_char_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_char_counter, id, type, isList, total_size, number_dimensions, dimensions)
            else:
                # print(id + " - " + str(self.current_local_char_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_char_counter, id, type, isList, total_size, number_dimensions, dimensions)

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

        elif re.search("list(\[.*\])+string", type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(type)
            isList = True
            self.functions_directory.addString(self.function_name, False, total_size)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_string_counter))
                self.functions_directory.getInfoDirectory(self.current_global_string_counter, self.function_name).push_frame(id, type, isList, total_size, number_dimensions, dimensions)
            else:
                # print(id + " - " + str(self.current_local_string_counter))
                self.functions_directory.getInfoDirectory(self.current_local_string_counter, self.function_name).push_frame(id, type, isList, total_size, number_dimensions, dimensions)
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
        elif re.search("list(\[.*\])+bool", type) is not None:
            total_size, number_dimensions, dimensions = self.parseList(type)
            isList = True
            self.functions_directory.addBool(self.function_name, False, total_size)
            if self.isGlobalVar:
                # print(id + " - " + str(self.current_global_bool_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_global_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
            else:
                # print(id + " - " + str(self.current_local_boolean_counter))
                self.functions_directory.getInfoDirectory(self.function_name).push_frame(self.current_local_boolean_counter, id, type, isList, total_size, number_dimensions, dimensions)
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

    def newFunction(self):
        """
        Adds a new function into the function directory
        """
        if self.function_name not in self.functions_directory.getDirectory():
            self.functions_directory.create_table(self.function_name, InfoDirectory(SymbolTable()))
            self.functions_directory.getTable(self.function_name).setParamTable(self.argumentos)
            start_address = len(self.cuadruplos) + 1
            self.functions_directory.getTable(self.function_name).setStartAddress(start_address)
            for key, value in self.argumentos.getParameters().items():
                if value.getType() == 0:
                    self.functions_directory.addInt(self.function_name, True, 1)
                    self.functions_directory.addParam(self.function_name, key, "int", value.getListSize())
                elif value.getType() == 1:
                    self.functions_directory.addFloat(self.function_name, True, 1)
                    self.functions_directory.addParam(self.function_name, key, "float", value.getListSize())
                elif value.getType() == 2:
                    self.functions_directory.addChar(self.function_name, True, 1)
                    self.functions_directory.addParam(self.function_name, key, "char", value.getListSize())
                elif value.getType() == 3:
                    self.functions_directory.addString(self.function_name, True, 1)
                    self.functions_directory.addParam(self.function_name, key, "string", value.getListSize())
                elif value.getType() == 4:
                    self.functions_directory.addBool(self.function_name, True, 1)
                    self.functions_directory.addParam(self.function_name, key, "bool", value.getListSize())

            # Test
            # size = len(self.functions_directory.getTable(self.function_name).getParamTable().getParameters())
            # print(self.function_name + " - size: " + str(size))
        else:
            print("Syntax error!! Function: " + self.function_name + " is already defined")
            sys.exit(0)

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

    def convertTypeToInt(self, type):
        if not isinstance(type, int):
            if type == "int":
                return 0
            elif type == "float":
                return 1
            elif type == "char":
                return 2
            elif type == "string":
                return 3
            elif type == "bool" or re.search("list(\[.*\])+bool", type) is not None:
                return 4
            elif type == "null":
                return 5
        return type

    # Enter a parse tree produced by Objective_JSParser#inicio.
    def enterInicio(self, ctx:Objective_JSParser.InicioContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#inicio.
    def exitInicio(self, ctx:Objective_JSParser.InicioContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#main.
    def enterMain(self, ctx:Objective_JSParser.MainContext):
        quadruple = Quadruple(self.id, GO.TO, None, None, None)
        self.cuadruplos.append(quadruple)
        self.id += 1
        self.pending_jumps.push(len(self.cuadruplos) - 1)

    # Exit a parse tree produced by Objective_JSParser#main.
    def exitMain(self, ctx:Objective_JSParser.MainContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#clase.
    def enterClase(self, ctx:Objective_JSParser.ClaseContext):
        className = ctx.CLASSNAME().getText()
        self.newClass(className)

    # Exit a parse tree produced by Objective_JSParser#clase.
    def exitClase(self, ctx:Objective_JSParser.ClaseContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#imports.
    def enterImports(self, ctx:Objective_JSParser.ImportsContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#imports.
    def exitImports(self, ctx:Objective_JSParser.ImportsContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#class_declaration.
    def enterClass_declaration(self, ctx:Objective_JSParser.Class_declarationContext):
        self.function_name = ctx.CLASSNAME().getText()
        self.functions_directory.create_table(self.function_name, InfoDirectory())

        # Test
        # size = len(self.functions_directory.getTable(self.function_name).getSymbolTable().getSymbols())
        # print(self.function_name + " - size: " + str(size))

    # Exit a parse tree produced by Objective_JSParser#class_declaration.
    def exitClass_declaration(self, ctx:Objective_JSParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#main_header.
    def enterMain_header(self, ctx:Objective_JSParser.Main_headerContext):
        self.function_name = "main"
        self.functions_directory.create_table("main", InfoDirectory())

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


    # Enter a parse tree produced by Objective_JSParser#claseAux.
    def enterClaseAux(self, ctx:Objective_JSParser.ClaseAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#claseAux.
    def exitClaseAux(self, ctx:Objective_JSParser.ClaseAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#bloqueClase.
    def enterBloqueClase(self, ctx:Objective_JSParser.BloqueClaseContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueClase.
    def exitBloqueClase(self, ctx:Objective_JSParser.BloqueClaseContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#constructor.
    def enterConstructor(self, ctx:Objective_JSParser.ConstructorContext):
        pass

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
        pass

    # Exit a parse tree produced by Objective_JSParser#atributos.
    def exitAtributos(self, ctx:Objective_JSParser.AtributosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosPublic.
    def enterAtributosPublic(self, ctx:Objective_JSParser.AtributosPublicContext):
        self.visibility = ctx.PUBLIC().getText()

    # Exit a parse tree produced by Objective_JSParser#atributosPublic.
    def exitAtributosPublic(self, ctx:Objective_JSParser.AtributosPublicContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosPublicAux.
    def enterAtributosPublicAux(self, ctx:Objective_JSParser.AtributosPublicAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#atributosPublicAux.
    def exitAtributosPublicAux(self, ctx:Objective_JSParser.AtributosPublicAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#atributosPrivate.
    def enterAtributosPrivate(self, ctx:Objective_JSParser.AtributosPrivateContext):
        self.visibility = ctx.PRIVATE().getText()

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

    # Exit a parse tree produced by Objective_JSParser#metodos.
    def exitMetodos(self, ctx:Objective_JSParser.MetodosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPublicos.
    def enterMetodosPublicos(self, ctx:Objective_JSParser.MetodosPublicosContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPublicos.
    def exitMetodosPublicos(self, ctx:Objective_JSParser.MetodosPublicosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPublicosAux.
    def enterMetodosPublicosAux(self, ctx:Objective_JSParser.MetodosPublicosAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPublicosAux.
    def exitMetodosPublicosAux(self, ctx:Objective_JSParser.MetodosPublicosAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPrivados.
    def enterMetodosPrivados(self, ctx:Objective_JSParser.MetodosPrivadosContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPrivados.
    def exitMetodosPrivados(self, ctx:Objective_JSParser.MetodosPrivadosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#metodosPrivadosAux.
    def enterMetodosPrivadosAux(self, ctx:Objective_JSParser.MetodosPrivadosAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#metodosPrivadosAux.
    def exitMetodosPrivadosAux(self, ctx:Objective_JSParser.MetodosPrivadosAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#func.
    def enterFunc(self, ctx:Objective_JSParser.FuncContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#func.
    def exitFunc(self, ctx:Objective_JSParser.FuncContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#funcAux.
    def enterFuncAux(self, ctx:Objective_JSParser.FuncAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#funcAux.
    def exitFuncAux(self, ctx:Objective_JSParser.FuncAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentosDecl.
    def enterArgumentosDecl(self, ctx:Objective_JSParser.ArgumentosDeclContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#argumentosDecl.
    def exitArgumentosDecl(self, ctx:Objective_JSParser.ArgumentosDeclContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentosDeclAux.
    def enterArgumentosDeclAux(self, ctx:Objective_JSParser.ArgumentosDeclAuxContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#argumentosDeclAux.
    def exitArgumentosDeclAux(self, ctx:Objective_JSParser.ArgumentosDeclAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impConstructores.
    def enterImpConstructores(self, ctx:Objective_JSParser.ImpConstructoresContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#impConstructores.
    def exitImpConstructores(self, ctx:Objective_JSParser.ImpConstructoresContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impConstructor.
    def enterImpConstructor(self, ctx:Objective_JSParser.ImpConstructorContext):
        self.function_name = ctx.CLASSNAME().getText()
        self.function_name += "Constructor"
        if self.function_name in self.functions_directory.getDirectory():
            self.constructores = self.constructores + 1
            self.function_name += str(self.constructores)

    # Exit a parse tree produced by Objective_JSParser#impConstructor.
    def exitImpConstructor(self, ctx:Objective_JSParser.ImpConstructorContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#emptyRule.
    def enterEmptyRule(self, ctx:Objective_JSParser.EmptyRuleContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#emptyRule.
    def exitEmptyRule(self, ctx:Objective_JSParser.EmptyRuleContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impFunc.
    def enterImpFunc(self, ctx:Objective_JSParser.ImpFuncContext):
        if ctx.FUNCTION() is not None:
            self.function_name = ctx.ID().getText()
            # print(self.function_name)

    # Exit a parse tree produced by Objective_JSParser#impFunc.
    def exitImpFunc(self, ctx:Objective_JSParser.ImpFuncContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#impFuncAux2.
    def enterImpFuncAux2(self, ctx:Objective_JSParser.ImpFuncAux2Context):
        self.newFunction()
        if ctx.RETURNS() is None:
            self.does_returns = None
        else:
            self.does_returns = "returns"
            return_type = ctx.tipo_dato_no_list().getText()
            self.functions_directory.getTable(self.function_name).setReturnType(self.normalizeTypes(return_type))

    # Exit a parse tree produced by Objective_JSParser#impFuncAux2.
    def exitImpFuncAux2(self, ctx:Objective_JSParser.ImpFuncAux2Context):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentos.
    def enterArgumentos(self, ctx:Objective_JSParser.ArgumentosContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            self.newArgument(id, self.type, self.visibility)

    # Exit a parse tree produced by Objective_JSParser#argumentos.
    def exitArgumentos(self, ctx:Objective_JSParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#argumentosAux.
    def enterArgumentosAux(self, ctx:Objective_JSParser.ArgumentosAuxContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            self.newArgument(id, self.type, self.visibility)

    # Exit a parse tree produced by Objective_JSParser#argumentosAux.
    def exitArgumentosAux(self, ctx:Objective_JSParser.ArgumentosAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#bloqueConstructor.
    def enterBloqueConstructor(self, ctx:Objective_JSParser.BloqueConstructorContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueConstructor.
    def exitBloqueConstructor(self, ctx:Objective_JSParser.BloqueConstructorContext):
        self.argumentos = ParamTable()
        self.functions_directory.remove_info(self.function_name)


    # Enter a parse tree produced by Objective_JSParser#bloqueFunc.
    def enterBloqueFunc(self, ctx:Objective_JSParser.BloqueFuncContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#bloqueFunc.
    def exitBloqueFunc(self, ctx:Objective_JSParser.BloqueFuncContext):
        self.argumentos = ParamTable()
        quadruple = Quadruple(self.id, "endproc", None, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)
        self.registros = 1
        self.resetMemoryAddresses()
        quadruple = Quadruple(self.id, "resetAddress", None, None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)
        self.registros = 1

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
    def exitBloqueFuncAux2(self, ctx:Objective_JSParser.BloqueFuncAux2Context):
        self.functions_directory.remove_info(self.function_name)
        self.function_name = None

    def enterGetReturnType(self, ctx):
        return_value = self.operandos.pop()
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
    def enterVars_(self, ctx:Objective_JSParser.Vars_Context):
        id = ctx.ID().getText()
        self.type = ctx.tipo_dato().getText() 
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
        elif re.search("list(\[.\])+int", self.type) is not None:
            type_number = 0
        elif re.search("list(\[.\])+float", self.type) is not None:
            type_number = 1
        elif re.search("list(\[.\])+char", self.type) is not None:
            type_number = 2
        elif re.search("list(\[.\])+string", self.type) is not None:
            type_number = 3
        elif re.search("list(\[.\])+bool", self.type) is not None:
            type_number = 4

        self.newVars(id, type_number, self.visibility)

    def newArgument(self, id, type, visibility):
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
                    self.current_local_int_counter += (dimensions[0].getUpperBound()) + (dimensions[1].getUpperBound())
                else:
                    self.current_local_int_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+float", type) is not None:
                type_number = 1
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_float_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_float_counter)
                if len(dimensions) == 2:
                    self.current_local_float_counter += (dimensions[0].getUpperBound()) + (dimensions[1].getUpperBound())
                else:
                    self.current_local_float_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+char", type) is not None:
                type_number = 2
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_char_counter)
                if len(dimensions) == 2:
                    self.current_local_char_counter += (dimensions[0].getUpperBound()) + (dimensions[1].getUpperBound())
                else:
                    self.current_local_char_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+string", type) is not None:
                type_number = 3
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_string_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_string_counter)
                if len(dimensions) == 2:
                    self.current_local_string_counter += (dimensions[0].getUpperBound()) + (dimensions[1].getUpperBound())
                else:
                    self.current_local_string_counter += (dimensions[0].getUpperBound())
            elif re.search("list(\[[0-9]+\])+bool", type) is not None:
                type_number = 4
                isList = True
                total_size, number_dimensions, dimensions = self.parseList(type)
                # print(id + " - " + str(self.current_local_boolean_counter))
                self.argumentos.push_param(id, type_number, isList, total_size, number_dimensions, dimensions, self.current_local_boolean_counter)
                if len(dimensions) == 2:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound()) + (dimensions[1].getUpperBound())
                else:
                    self.current_local_boolean_counter += (dimensions[0].getUpperBound())

    # Exit a parse tree produced by Objective_JSParser#vars_.
    def exitVars_(self, ctx:Objective_JSParser.Vars_Context):
        pass


    # Enter a parse tree produced by Objective_JSParser#varsAux.
    def enterVarsAux(self, ctx:Objective_JSParser.VarsAuxContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.newVars(id, self.type, self.visibility)

    # Exit a parse tree produced by Objective_JSParser#varsAux.
    def exitVarsAux(self, ctx:Objective_JSParser.VarsAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#varsRepeated.
    def enterVarsRepeated(self, ctx:Objective_JSParser.VarsRepeatedContext):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            self.type = ctx.tipo_dato().getText()
            self.newVars(id, self.type, self.visibility)

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
    def enterTipo_dato_list(self, ctx:Objective_JSParser.Tipo_dato_listContext):
        self.isListDeclared = True

    # Exit a parse tree produced by Objective_JSParser#tipo_dato_list.
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
    def exitAsignacion(self, ctx:Objective_JSParser.AsignacionContext):
        string = True
        char = True
        id = ctx.objeto().getText()
        valor = self.operandos.pop()
        possibleType = self.types.pop()
        variableType = self.getTypeFromVariable(id)
        variableType = self.convertTypeToInt(variableType)
        new_type = np.int64(self.oraculo.getDataType(variableType, 10, possibleType))
        if new_type == -1:
            print("Data type mismatch")
            sys.exit(0)
            print("Error")
        address = self.getMemoryAddressFromVariable(id)
        self.operadores.pop()
        cuadruplo = Quadruple(self.id, "=", valor, None, address)
        #cuadruplo.print()
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
    def exitEndIf(self, ctx:Objective_JSParser.EndIfContext):
        end = self.pending_jumps.pop()
        while (end != -1):
            self.fill(end, len(self.cuadruplos)+1)
            end = self.pending_jumps.pop()
        if end == -1:
            self.pending_jumps.pop


    # Enter a parse tree produced by Objective_JSParser#exitIfExpresion.
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

    def enterPrintAfterExpresion(self, ctx:Objective_JSParser.EscrituraContext):
        # print("PRINT: " + str(self.operandos.pop()))
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


    def enterPrintAfterExpresionAux(self, ctx:Objective_JSParser.EscrituraAuxContext):
        # print("PRINT aux: " + str(self.operandos.pop()))
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
    def enterLlamadaFunc(self, ctx:Objective_JSParser.LlamadaFuncContext):
        if ctx.THIS() is not None or len(ctx.ID()) == 1: #Local method
            self.current_method_name = ctx.ID()[0].getText()
            if self.current_method_name not in  self.functions_directory.getDirectory():
                print("The function: " + str(self.current_method_name)+ " doesn't exist")
                sys.exit(0)
            quadruple = Quadruple(self.id, "ERA", self.current_method_name, None, None)
            self.id += 1
            self.cuadruplos.append(quadruple)

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
    def exitLlamadaFunc(self, ctx:Objective_JSParser.LlamadaFuncContext):
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
            quadruple = Quadruple(self.id, "save_return",self.current_method_name, None,self.current_temp_int_counter)
            self.operandos.push(self.current_temp_int_counter)
            self.id += 1
            self.current_temp_int_counter += 1
            self.cuadruplos.append(quadruple)


    # Enter a parse tree produced by Objective_JSParser#argumentosLlamada.
    def enterArgumentosLlamada(self, ctx:Objective_JSParser.ArgumentosLlamadaContext):
        self.operadores.push(')')

    # Exit a parse tree produced by Objective_JSParser#argumentosLlamada.
    def exitArgumentosLlamada(self, ctx:Objective_JSParser.ArgumentosLlamadaContext):
        self.operadores.pop()


    # Enter a parse tree produced by Objective_JSParser#addArgument.
    def enterAddArgument(self, ctx:Objective_JSParser.AddArgumentContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#addArgument.
    def exitAddArgument(self, ctx:Objective_JSParser.AddArgumentContext):
        self.current_param_counter += 1


    # Enter a parse tree produced by Objective_JSParser#verifyArgument.
    def enterVerifyArgument(self, ctx:Objective_JSParser.VerifyArgumentContext):
        pass

    def getVarNameFromMemoryAddress(self, address):
        for funtion_name, info in self.functions_directory.getDirectory().items():
            for var, info2 in info.getSymbolTable().getSymbols().items():
                if address == info2.getAddress():
                    return var

    # Exit a parse tree produced by Objective_JSParser#verifyArgument.
    def exitVerifyArgument(self, ctx:Objective_JSParser.VerifyArgumentContext):
        argument = self.operandos.pop()
        argument_address = argument
        argument_type = self.types.pop()


        argument_type = self.normalizeTypes(argument_type)
        parameter_type = self.functions_directory.getTable(self.current_method_name).getParams()[self.current_param_counter][1]
        parameter_type = self.normalizeTypes(parameter_type)
        parameter = self.functions_directory.getTable(self.current_method_name).getParams()[self.current_param_counter][0]  
        parameter_address = self.functions_directory.getTable(self.current_method_name).getParamTable().getAddress(parameter)
        dimensions_param = self.functions_directory.getTable(self.current_method_name).getParamTable().getParam(parameter).getRows()
        dimensions_argument = 1
        all_dimensions_argument = []
        argument = self.getVarNameFromMemoryAddress(argument)
        for key, value in self.functions_directory.getDirectory().items():
            if argument in value.getSymbolTable().getSymbols():
                dimensions_argument = value.getSymbolTable().getContent(argument).getListSize()
                all_dimensions_argument = value.getSymbolTable().getContent(argument).getDim()
                break

        all_dimensions_param = self.functions_directory.getTable(self.current_method_name).getParamTable().getParam(parameter).getDimensions()
        if argument_type != parameter_type:
            print("The function " + str(self.current_method_name) + " was expecting an " + str(self.convertIntToStringType(parameter_type)) + " but received an " + str(self.convertIntToStringType(argument_type)) + " at: " + str(argument))
            sys.exit(0)
        if dimensions_param != dimensions_argument:
            if dimensions_param > dimensions_argument:
                print("The function " + str(self.current_method_name) + " was expecting a matrix but received a list")
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

        quadruple = Quadruple(self.id, "param", argument_address, None, parameter_address)
        self.cuadruplos.append(quadruple)
        self.id += 1



    # Enter a parse tree produced by Objective_JSParser#argumentosLlamadaAux.
    def enterArgumentosLlamadaAux(self, ctx:Objective_JSParser.ArgumentosLlamadaAuxContext):
        pass
        self.operandos.push(')')

    # Exit a parse tree produced by Objective_JSParser#argumentosLlamadaAux.
    def exitArgumentosLlamadaAux(self, ctx:Objective_JSParser.ArgumentosLlamadaAuxContext):
        pass
        self.operandos.pop()


    # Enter a parse tree produced by Objective_JSParser#lectura.
    def enterLectura(self, ctx:Objective_JSParser.LecturaContext):
        quadruple = Quadruple(self.id, "read", ctx.ID().getText(), None, None)
        self.id += 1
        self.cuadruplos.append(quadruple)

    # Exit a parse tree produced by Objective_JSParser#lectura.
    def exitLectura(self, ctx:Objective_JSParser.LecturaContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#lecturaAux.
    def enterLecturaAux(self, ctx:Objective_JSParser.LecturaAuxContext):
        if ctx.INPUT_STREAM() is not None:
            quadruple = Quadruple(self.id, "read",  ctx.ID().getText(), None, None)
            self.id += 1
            self.cuadruplos.append(quadruple)

    # Exit a parse tree produced by Objective_JSParser#lecturaAux.
    def exitLecturaAux(self, ctx:Objective_JSParser.LecturaAuxContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#decInc.
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


    # Enter a parse tree produced by Objective_JSParser#objeto.
    def enterObjeto(self, ctx:Objective_JSParser.ObjetoContext):
        if ctx.objetoAux() is not None:
            id = ctx.objetoAux().getText()
            self.isVarDeclared(id)
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

    def enterHyperExpresionAux(self, ctx):
        if ctx.POWER_OPERATOR() is not None:
            self.operadores.push('^')

    def exitHyperExpresionAux(self, ctx):
        if self.operadores.top() == '^':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()
            number_op = 4


            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))

            if new_type == 0:
                self.functions_directory.addTempInt(self.function_name, 1)
            elif new_type == 1:
                self.functions_directory.addTempFloat(self.function_name, 1)
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
    def enterMegaExpresionAux(self, ctx:Objective_JSParser.MegaExpresionAuxContext):
        if ctx.LOGICAL_AND_OPERATOR() is not None:
            self.operadores.push('&&')
        elif ctx.LOGICAL_OR_OPERATOR() is not None:
            self.operadores.push('||')

    # Exit a parse tree produced by Objective_JSParser#megaExpresionAux.
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
            if new_type == 0:
                self.functions_directory.addTempInt(self.function_name, 1)
            elif new_type == 1:
                self.functions_directory.addTempFloat(self.function_name, 1)


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
            self.functions_directory.addTempBool(self.function_name, 1)
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


    # Enter a parse tree produced by Objective_JSParser#expresion.
    def enterExpresion(self, ctx:Objective_JSParser.ExpresionContext):
        pass

    # Exit a parse tree produced by Objective_JSParser#expresion.
    def exitExpresion(self, ctx:Objective_JSParser.ExpresionContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#expresionOperadores.
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
            if new_type == 0:
                self.functions_directory.addTempInt(self.function_name, 1)
            elif new_type == 1:
                self.functions_directory.addTempFloat(self.function_name, 1)

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
    def enterTerminoOperadores(self, ctx:Objective_JSParser.TerminoOperadoresContext):
        if ctx.MULTIPLICATION_OPERATOR() is not None:
            self.operadores.push('*')
        elif ctx.DIVISION_OPERATOR() is not None:
            self.operadores.push('/')

    # Exit a parse tree produced by Objective_JSParser#terminoOperadores.
    def exitTerminoOperadores(self, ctx:Objective_JSParser.TerminoOperadoresContext):
        pass


    # Enter a parse tree produced by Objective_JSParser#factor.
    def enterFactor(self, ctx:Objective_JSParser.FactorContext):
        if ctx.varCte() is not None:
            if ctx.varCte().llamadaFunc() is not None:
                function_name = ctx.varCte().getText().split('(')[0]
                if not self.isFunctionDeclared(function_name):
                    print("The function: " + str(function_name) + " doesn't exist")
                    sys.exit(0)
                else:
                    return_type = self.functions_directory.getTable(function_name).getReturnType()
                    self.types.push(return_type)
            elif ctx.varCte() is not None and ctx.varCte().TYPE_STRING() is None and ctx.varCte().TYPE_CHAR() is None:
                value = ctx.varCte().getText()
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
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_int_counter += 1
                        elif type == 1:
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_float_counter += 1
                        elif type == 2:
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_char_counter += 1
                        elif type == 3:
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_string_counter += 1
                        elif type == 4:
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
                            # self.current_local_boolean_counter += 1
                        elif type == 5:
                            address = self.getMemoryAddressFromVariable(value)
                            self.operandos.push(address)
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
    def exitFactor(self, ctx:Objective_JSParser.FactorContext):
        if self.operadores.top() == '/' or self.operadores.top() == '*':
            operando2 = self.operandos.pop()
            tipo1 = self.types.pop()
            operando1 = self.operandos.pop()
            tipo2 = self.types.pop()
            operador = self.operadores.pop()

            if operador == '/':
                number_op = 3
            else:
                number_op = 2

            new_type = np.int64(self.oraculo.getDataType(tipo1, number_op, tipo2))
            if new_type == 0:
                self.functions_directory.addTempInt(self.function_name, 1)
            elif new_type == 1:
                self.functions_directory.addTempFloat(self.function_name, 1)
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

    def exitGetValue(self, ctx):
        # print("After return")
        # print(ctx.tipo_dato_no_list().getText())
        # print("Return value: " + str(return_value))
        # return_type = self.getTypeFromAddress(return_value)
        # print("Return type: " + str(return_type))
        # print("Function: " + str(self.function_name))
        # self.functions_directory.getTable(self.function_name).setReturnType(return_type)
        # quadruple = Quadruple(self.id, "return", return_value, None, None)
        # self.id += 1
        # self.cuadruplos.append(quadruple)
        pass

    def getTypeFromAddress(self, address):
        if isinstance(address, str):
            if address[0] == "%":
                value = address[1:]
                try:
                    number = int(value)
                    return 0
                except ValueError:
                    try:
                        number = float(value)
                        return 1
                    except ValueError:
                        if value == "true" or value == "false":
                            return 4
                        if len(address) > 1:
                            return 3
                        else:
                            return 2
        address = int(address)
        if 7000 <= address <= 7999 or 13000 <= address <= 13999:
            return 0
        elif 8000 <= address <= 8999 or 14000 <= address <= 14999:
            return 1
        elif 9000 <= address <= 9999 or 15000 <= address <= 15999:
            return 2
        elif 10000 <= address <= 10999 or 16000 <= address <= 16999:
            return 3
        elif 11000 <= address <= 11999 or 17000 <= address <= 17999:
            return 4
        elif 12000 <= address <= 12999 or 18000 <= address <= 18999:
            return 5