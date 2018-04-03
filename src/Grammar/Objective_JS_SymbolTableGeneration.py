import sys
import re
import numpy as np
from antlr4 import *
from Grammar.Objective_JSListener import Objective_JSListener
from Structures.Cube import Cube
from Structures.FunctionsDirectory import FunctionsDirectory
from Structures.GO import GO
from Structures.InfoDirectory import InfoDirectory
from Structures.Info import Info
from Structures.Stack import Stack
from Structures.SymbolTable import SymbolTable
from Structures.Quadruple import Quadruple

class Objective_JS_SymbolTableGeneration(Objective_JSListener):

	def __init__(self):
		self.functions_directory = FunctionsDirectory()
		self.type = None
		# Default visibility
		self.visibility = "private"
		self.does_returns = None
		self.function_name = None
		self.argumentos = SymbolTable()
		self.constructores = 0
		self.cuadruplos = []
		self.operadores = Stack()
		self.operandos = Stack()
		self.types = Stack()
		self.registros = 1
		self.oraculo = Cube()
		self.isListDeclared = False;
		self.pending_jumps = Stack()
		self.id = 1;

	def getFunctionDirectory(self):
		return self.functions_directory

	def getQuadruples(self):
		return self.cuadruplos

	def isFunctionDeclared(self, name):
		if name in self.functions_directory.getDirectory():
			return True
		else:
			return False

	def isVarDeclared(self, var):
		exist = False
		tabla = self.functions_directory.getSymbolTable(self.function_name)

		# Check if the 'var' is a function
		exist = self.isFunctionDeclared(var)

		if var in tabla.getTable():
			exist = True
		else:
			for key, value in self.functions_directory.getDirectory().items():
				if var in value.getSymbolTable().getTable():
					exist = True
					break	

		if not exist:
			print(var + " is used but not defined!")
			sys.exit(0)

	def fill(self, end, next):
		quadruple = self.cuadruplos[end]
		quadruple.setResult(next)

	def getTypeFromVariable(self, var):
		# First check in the local scope
		# print("Getting type for: " + var)
		if self.functions_directory.getSymbolTable(self.function_name).getContent(var):
			# print("Found it on local scope")
			# print("Type: " + str(self.functions_directory.getSymbolTable(self.function_name).getContent(var).getType()))
			return self.functions_directory.getSymbolTable(self.function_name).getContent(var).getType()
		# Then check in the global scope
		# print("Found it on global scope")
		for key, value in self.functions_directory.getDirectory().items():
			if var in value.getSymbolTable().getTable():
				return value.getSymbolTable().getContent(var).getType()

	def getSymbolsTables(self):
		return self.functions_directory.getDirectory()

	def getCuadruplos(self):
		return self.cuadruplos

	# Se crea una clase en el directorio de funciones
	def newClass(self, className):
		self.function_name = className
		self.functions_directory.create_table(self.function_name, InfoDirectory())

	# Se añade una variable al directorio de símbolos de la función correspondiente
	def newVars(self, id, type, visibility):
		if id in self.functions_directory.getSymbolTable(self.function_name).getTable():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		self.functions_directory.getSymbolTable(self.function_name).push_frame(id, type, visibility)

	# Se añade una función al directorio de funciones
	def newFunction(self):
		if self.function_name not in self.functions_directory.getDirectory():
			self.functions_directory.create_table(self.function_name, InfoDirectory(self.argumentos, self.does_returns))
		else:
			print("Syntax error!! Function: " + self.function_name + " is already defined")
			sys.exit(0)

	# Sirve para crear la variable, obtiene el tipo y el ID
	def enterVars_(self, ctx):
		id = ctx.ID().getText()
		#print("ID: " + str(id))
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
		elif re.search("list(\[.\])+int", type) is not None:
			type_number = 0
		elif re.search("list(\[.\])+float", type) is not None:
			type_number = 1

		self.newVars(id, type_number, self.visibility)

	# Método que invoca a la función encargada de añadir la clase al directorio de funciones
	def enterClase(self, ctx):
		className = ctx.CLASSNAME().getText()
		self.newClass(className)

	# Función que invoca al método que añade una variable al directorio de símbolos
	def enterVarsAux(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.newVars(id, self.type, self.visibility)

	# Función que invoca al método que añade una variable al directorio de símbolos
	def enterVarsRepeated(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.type = ctx.tipo_dato().getText()
			self.newVars(id, self.type, self.visibility)

	# Se asigna la visibilidad publica
	def enterAtributosPublic(self, ctx):
		self.visibility = ctx.PUBLIC().getText()

	# Se asigna la visibilidad privada
	def enterAtributosPrivate(self, ctx):
		self.visibility = ctx.PRIVATE().getText()

	# Se asigna un nuevo contexto (nombre de la función)
	def enterImpFunc(self, ctx):
		if ctx.FUNCTION() is not None:
			self.function_name = ctx.ID().getText()

	# Se encarga de crear una nueva función con el tipo correspondiente (si regresa o no algo)
	def enterImpFuncAux2(self, ctx):
		if ctx.RETURNS() is None:
			self.does_returns = None
		else:
			self.does_returns = "returns"
		self.newFunction()

	# Se asigna nuevo contexto y se agrega la clase al directorio de funciones
	def enterClass_declaration(self, ctx):
		self.function_name = ctx.CLASSNAME().getText()
		self.functions_directory.create_table(self.function_name, InfoDirectory())

	# Se asigna nuevo contexto y se agrega la clase al directorio de funciones
	def enterMain_header(self, ctx):
		self.function_name = "main"
		self.functions_directory.create_table("main", InfoDirectory())

	# Se elimina la tabla de símbolos asociada al contexto actual
	def exitBloqueFuncAux2(self, ctx):
		self.functions_directory.remove_info(self.function_name)
		self.function_name = None

	# Sirve para almacenar las variables de los argumentos (aun no se crea la funcion en el directorio de funciones)
	def newArgument(self, id, type, visibility):
		if id in self.argumentos.getTable():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		else:
			if type == "int":
				type_number = 0
			elif type == "float":
				type_number = 1
			elif type == "char":
				type_number = 2
			elif type == "string":
				type_number = 3
			elif type == "bool":
				type_number = 4
			elif type == "null":
				type_number = 5
			elif re.search("list(\[.\])+int", type) is not None:
				type_number = 0
			elif re.search("list(\[.\])+float", type) is not None:
				type_number = 1

			self.argumentos.push_frame(id, type_number, visibility)

	# Se agregan argumentos de una funcion en la tabla de símbolos
	def enterArgumentos(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.type = ctx.tipo_dato().getText()
			self.newArgument(id, self.type, self.visibility)

	# Se agregan argumentos de uan funcion en la tabla de símbolos
	def enterArgumentosAux(self, ctx):
		if ctx.ID() is not None:
			id = ctx.ID().getText()
			self.type = ctx.tipo_dato().getText()
			self.newArgument(id, self.type, self.visibility)

	# Se crea el constructor en la tabla de funciones (si ya existe, sino solo se crea de nuevo)
	def enterImpConstructor(self, ctx):
		self.function_name = ctx.CLASSNAME().getText()
		self.function_name += "Constructor"
		if self.function_name in self.functions_directory.getDirectory():
			self.constructores = self.constructores + 1
			self.function_name += str(self.constructores)

	def exitBloqueFunc(self, ctx):
		self.argumentos = SymbolTable()

	def exitBloqueConstructor(self, ctx):
		self.argumentos = SymbolTable()
		self.functions_directory.remove_info(self.function_name)

	def enterEmptyRule(self, ctx):
		self.newFunction()

	#def exitSuperExpresion(self, ctx):
	def getTypeFromFactor(self, ctx, value):
		if ctx.varCte().TYPE_INT() is not None:
			return 0
		elif ctx.varCte().TYPE_FLOAT() is not None:
			return 1
		elif ctx.varCte().TYPE_CHAR() is not None:
			return 2
		elif ctx.varCte().TYPE_STRING() is not None:
			return 3
		elif ctx.varCte().TYPE_BOOL() is not None:
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
			elif type == "bool":
				return 4
			elif type == "null":
				return 5
		return type

	# Se introducen los operandos en la pila
	def enterFactor(self, ctx):
		if ctx.varCte() is not None and ctx.varCte().TYPE_STRING() is None and ctx.varCte().TYPE_CHAR() is None:
			value = ctx.varCte().getText()
			self.operandos.push(value)
			type = self.getTypeFromFactor(ctx, value)
			type = self.convertTypeToInt(type)
			self.types.push(type)
		elif ctx.factorParentesis() is not None:
			# Fondo falso
			self.operadores.push('(')
		elif not self.isListDeclared:
			value = ctx.varCte().getText()
			self.operandos.push(value)
			type = self.getTypeFromFactor(ctx, value)
			type = self.convertTypeToInt(type)
			self.types.push(type)

	# Revisa que el id exista
	def enterObjeto(self, ctx):
		if ctx.objetoAux() is not None:
			id = ctx.objetoAux().getText()
			self.isVarDeclared(id)

	def exitAsignacion(self, ctx):
		string = True
		char = True
		id = ctx.objeto().getText()
		valor = self.operandos.pop()
		possibleType = self.types.pop()
		variableType = self.getTypeFromVariable(id)
		variableType = self.convertTypeToInt(variableType)
		#print("Var: " + str(id))
		new_type = np.int64(self.oraculo.getDataType(variableType, 10, possibleType))
		if new_type == -1:
			print("Data type mismatch")
			sys.exit(0)
			print("Error")
		cuadruplo = Quadruple(self.id, "=", valor, "", id)
		#cuadruplo.print()
		self.cuadruplos.append(cuadruplo)
		self.id += 1

	# Se saca el fondo falso
	def exitFactorParentesis(self, ctx):
		self.operadores.pop()

	# Se resuelven y meten multiplicaciones y divisiones
	def exitFactor(self, ctx):
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
			if new_type == -1:
				print("Data type mismatch")
				sys.exit(0)
			else:
				registro = "r" + str(self.registros)
				self.operandos.push(registro)
				self.types.push(new_type)
				cuadruplo = Quadruple(self.id, operador, operando1, operando2, registro)
				self.cuadruplos.append(cuadruplo)
				#cuadruplo.print()
				self.id += 1
				self.registros += 1


	# Sumas y restas
	def exitTermino(self, ctx):
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
				registro = "r" + str(self.registros)
				self.operandos.push(registro)
				self.types.push(new_type)
				cuadruplo = Quadruple(self.id, operador, operando1, operando2, registro)
				self.cuadruplos.append(cuadruplo)
				#cuadruplo.print()
				self.registros += 1
				self.id += 1

	def exitMegaExpresionAux(self, ctx):
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
				registro = "r" + str(self.registros)
				self.operandos.push(registro)
				self.types.push(new_type)
				cuadruplo = Quadruple(self.id, operador, operando1, operando2, registro)
				self.cuadruplos.append(cuadruplo)
				#cuadruplo.print()
				self.registros += 1
				self.id += 1

	def exitSuperExpresionOperadores(self, ctx):
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
			else:
				registro = "r" + str(self.registros)
				self.operandos.push(registro)
				self.types.push(new_type)
				cuadruplo = Quadruple(self.id, operador, operando1, operando2, registro)
				self.cuadruplos.append(cuadruplo)
				#cuadruplo.print()
				self.registros += 1
				self.id += 1

	def enterMegaExpresionAux(self, ctx):
		if ctx.LOGICAL_AND_OPERATOR() is not None:
			self.operadores.push('&&')
		elif ctx.LOGICAL_OR_OPERATOR() is not None:
			self.operadores.push('||')

	def enterSuperExpresionOperadores(self, ctx):
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
			self.operadores.push('=')

	def enterTerminoOperadores(self, ctx):
		if ctx.MULTIPLICATION_OPERATOR() is not None:
			self.operadores.push('*')
		elif ctx.DIVISION_OPERATOR() is not None:
			self.operadores.push('/')

	def enterExpresionOperadores(self, ctx):
		if ctx.SUM_OPERATOR() is not None:
			self.operadores.push('+')
		elif ctx.SUBSTRACTION_OPERATOR() is not None:
			self.operadores.push('-')

	def enterTipo_dato_list(self, ctx):
		self.isListDeclared = True

	def exitTipo_dato_list(self, ctx):
		self.isListDeclared = False

	def enterExitIfExpresion(self, ctx):
		condition_type = self.types.pop()
		if condition_type != 4:
			print("The result of the expression must be boolean")
			sys.exit(0)

		if not self.pending_jumps.empty():
			end = self.pending_jumps.pop()
			#print("END: " + str(end))
			self.fill(end, len(self.cuadruplos) + 1)

		condition = self.operandos.pop()
		quadruple = Quadruple(self.id, GO.TOFALSE, condition , None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos) - 1)

	def enterCondicionChoice(self, ctx):

		if ctx.ELSE() is not None: # If it is an elsif, it will do the enterExitIfExpresion action
			quadruple = Quadruple(self.id, GO.TO, None, None, None)
			self.cuadruplos.append(quadruple)
			self.id += 1
			false = self.pending_jumps.pop()
			self.pending_jumps.push(len(self.cuadruplos)-1)
			self.fill(false, len(self.cuadruplos) + 1)

	def exitEndIf(self, ctx):
		end = self.pending_jumps.pop()
		self.fill(end, len(self.cuadruplos) + 1)

	def exitAfterWhile(self, ctx):
		self.pending_jumps.push(len(self.cuadruplos))

	def enterAfterWhilExpression(self, ctx):
		# exp_type = self.types.pop()
		# if exp_type != 4: #Boolean
		# 	print("The result of the expression must be boolean")
		# 	sys.exit(0)
		# result = self.operandos.pop()
		# TODO(jorge) : Replace first None with the actual result of the expression
		quadruple = Quadruple(self.id, GO.TOFALSE, None, None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos)-1)

	def exitExitWhile(self, ctx):
		end = self.pending_jumps.pop()
		ret = self.pending_jumps.pop()
		quadruple = Quadruple(self.id, GO.TO, None, None, ret)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.fill(end, len(self.cuadruplos))

	def exitAfterDo(self, ctx):
		self.pending_jumps.push(len(self.cuadruplos))

	def exitAfterCondition(self, ctx):
		# exp_type = self.types.pop()
		# if exp_type != 4: #Boolean
		# 	print("The result of the expression must be boolean")
		# 	sys.exit(0)
		# result = self.operandos.pop()
		# TODO(jorge) : Replace first None with the actual result of the expression
		quadruple = Quadruple(self.id, GO.TOFALSE, None, None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos)-1)

	def exitAfterDoLoop(self, ctx):
		end = self.pending_jumps.pop()
		ret = self.pending_jumps.pop()
		quadruple = Quadruple(self.id, GO.TO, None, None, ret)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.fill(end, len(self.cuadruplos))