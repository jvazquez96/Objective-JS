import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSListener import Objective_JSListener
from SymbolTable import SymbolTable
from InfoDirectory import InfoDirectory
from FunctionsDirectory import FunctionsDirectory
from Stack import Stack
from Quadruple import Quadruple
from Cube import Cube



PLUS = 101
MINUS = 102
MULTIPLICATION = 103
DIVISION = 104


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
		self.asignacion = False
		self.registros = 1
		self.oraculo = Cube()
		self.is_locale = False

	def getFunctionDirectory(self):
		return self.functions_directory

	def isVarDeclared(self, var):
		exist = False
		tabla = self.functions_directory.getSymbolTable(self.function_name)

		if var in tabla.getTable():
			exist = True
			#self.is_locale = True
		else:
			for key, value in self.functions_directory.getDirectory().items():
				if var in value.getSymbolTable().getTable():
					exist = True
					#self.is_locale = False
					break

		if not exist:
			print(var + " is used but not defined!")
			sys.exit(0)

	def getTypeFromVariable(self, var):
		# if self.is_locale:
		# 	print("Var: " + str(var))
		# 	tabla = self.functions_directory.getSymbolTable(self.function_name)
		# 	print(tabla.getContent(var))
		# 	return tabla.getContent(var).getType()
		# else:
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

	# Se introducen los operandos en la pila
	def enterFactor(self, ctx):
		if ctx.varCte() is not None and ctx.varCte().TYPE_STRING() is None and ctx.varCte().TYPE_CHAR() is None:
			value = ctx.varCte().getText()
			if self.asignacion:
				self.operandos.push(value)
				type = self.getTypeFromFactor(ctx, value)
				print("value: " + value)
				print("type: " + str(type))
				self.types.push(type)
				
		elif ctx.factorParentesis() is not None:
			# Fondo falso
			if self.asignacion:
				self.operadores.push('(')

	# Revisa que el id exista
	def enterObjeto(self, ctx):
		self.is_locale = False
		if ctx.objetoAux() is not None and self.asignacion:
			id = ctx.objetoAux().getText()
			self.isVarDeclared(id)

	# Sirve para activar o desactivar la bandera de asignacion
	def enterAsignacion(self, ctx):
		self.asignacion = True

	def exitAsignacion(self, ctx):
		string = True
		char = True
		if ctx.megaExpresion().superExpresion().expresion().termino().factor().varCte() is not None:
			string = ctx.megaExpresion().superExpresion().expresion().termino().factor().varCte().TYPE_STRING()
			char = ctx.megaExpresion().superExpresion().expresion().termino().factor().varCte().TYPE_CHAR()
		if string is None and char is None:
			id = ctx.objeto().getText()
			valor = self.operandos.pop()
			self.types.pop()
			cuadruplo = Quadruple("=", valor, "", id)
			cuadruplo.print()
			self.cuadruplos.append(cuadruplo)
			self.asignacion = False

	# Se saca el fondo falso
	def exitFactorParentesis(self, ctx):
		self.operadores.pop()

	# Se resuelven y meten multiplicaciones y divisiones
	def exitFactor(self, ctx):
		if self.asignacion:
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

				print("type1: " + str(tipo1))
				print("type2" + str(tipo2))
				new_type = self.oraculo.getDataType(tipo1, number_op, tipo2).any()
				if new_type == -1.0:
					print("Data type mismatch")
					sys.exit(0)
				else:
					registro = "r" + str(self.registros)
					self.operandos.push(registro)
					self.types.push(new_type)
					cuadruplo = Quadruple(operador, operando1, operando2, registro)
					self.cuadruplos.append(cuadruplo)
					cuadruplo.print()
					self.registros += 1


	# Sumas y restas
	def exitTermino(self, ctx):
		if self.asignacion:
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

				print("type1: " + str(tipo1))
				print("type2" + str(tipo2))
				new_type = self.oraculo.getDataType(tipo1, number_op, tipo2).any()
				if new_type == -1.0:
					print("Data type mismatch")
					sys.exit(0)
				else:
					registro = "r" + str(self.registros)
					self.operandos.push(registro)
					self.types.push(new_type)
					cuadruplo = Quadruple(operador, operando1, operando2, registro)
					self.cuadruplos.append(cuadruplo)
					cuadruplo.print()
					self.registros += 1

	def enterTerminoOperadores(self, ctx):
		if self.asignacion:
			if ctx.MULTIPLICATION_OPERATOR() is not None:
				self.operadores.push('*')
			elif ctx.DIVISION_OPERATOR() is not None:
				self.operadores.push('/')

	def enterExpresionOperadores(self, ctx):
		if self.asignacion:
			if ctx.SUM_OPERATOR() is not None:
				self.operadores.push('+')
			elif ctx.SUBSTRACTION_OPERATOR() is not None:
				self.operadores.push('-')