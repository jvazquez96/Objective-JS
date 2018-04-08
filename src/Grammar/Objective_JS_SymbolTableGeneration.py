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
from Structures.Dimensions import Dimensions
from Structures.ParamTable import ParamTable

class Objective_JS_SymbolTableGeneration(Objective_JSListener):

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
		self.registros = 1
		self.oraculo = Cube()
		self.isListDeclared = False;
		self.pending_jumps = Stack()
		self.id = 1;
		self.do_object = False
		self.current_param_counter = 0

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
		quadruple = self.cuadruplos[end]
		quadruple.setResult(next)

	def getTypeFromVariable(self, var):
		# First check in the local scope
		if self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var):
			return self.functions_directory.getTable(self.function_name).getSymbolTable().getContent(var).getType()
		elif self.functions_directory.getTable(self.function_name).getParamTable().getParam(var):
				return self.functions_directory.getTable(self.function_name).getParamTable().getType(var)
		# Then check in the global scope
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
		if id in self.functions_directory.getTable(self.function_name).getSymbolTable().getSymbols().items():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		isList = False
		total = 1
		dimensions = []
		counter = 0
		if type == "int" or type == 0:
			counter += 1
			self.functions_directory.addInt(self.function_name, False, 1)
		elif type == "float" or type == 1:
			counter += 1
			self.functions_directory.addFloat(self.function_name, False, 1)
		elif type == "char" or type == 2:
			counter += 1
			self.functions_directory.addChar(self.function_name, False, 1)
		elif type == "string" or type == 3:
			counter += 1
			self.functions_directory.addString(self.function_name, False, 1)
		elif type == "bool" or type == 4:
			counter += 1
			self.functions_directory.addBool(self.function_name, False, 1)
		elif re.search("list(\[[0-9]+\])+int", type) is not None:
			total = 1
			start = 0
			isFirst = True
			counter = 0
			for i in range(0, len(type)):
				if type[i] == '[':
					size = 1
					while (type[i+1] != ']'):
						if isFirst:
							start = i + 1;
							isFirst = not isFirst
						size += 1
						i += 1
					counter += 1
					dim = int(type[start : start+size-1])
					dimension = Dimensions(0, dim)
					dimensions.append(dimension)
					total *= dim
					isFirst = True
					start = 0
			if counter == 2: # Matrix
				dimensions[0].setM(dimensions[1].getUpperBound())
				dimensions[1].setM(0)
			else: # List
				dimensions[0].setM(0)
			isList = True
			self.functions_directory.addInt(self.function_name, False, total)
		elif re.search("list(\[[0-9]+\])+float", type) is not None:
			total = 1
			start = 0
			isFirst = True
			counter = 0
			for i in range(0, len(type)):
				if type[i] == '[':
					size = 1
					while (type[i+1] != ']'):
						if isFirst:
							start = i + 1;
							isFirst = not isFirst
						size += 1
						i += 1
					counter += 1
					dim = int(int(type[start : start+size-1]))
					total *= dim
					dimension = Dimensions(0, dim)
					dimensions.append(dimension)
					isFirst = True
					start = 0
			if counter == 2: # Matrix
				dimensions[0].setM(dimensions[1].getUpperBound())
				dimensions[1].setM(0)
			else: # List
				dimensions[0].setM(0)
			isList = True
			self.functions_directory.addFloat(self.function_name, False, total)
		elif re.search("list(\[[0-9]+\])+char", type) is not None:
			total = 1
			start = 0
			isFirst = True
			counter = 0
			for i in range(0, len(type)):
				if type[i] == '[':
					size = 1
					while (type[i+1] != ']'):
						if isFirst:
							start = i + 1;
							isFirst = not isFirst
						size += 1
						i += 1
					counter += 1
					dim = int(int(type[start : start+size-1]))
					total *= dim
					dimension = Dimensions(0, dim)
					dimensions.append(dimension)
					isFirst = True
					start = 0
			if counter == 2: # Matrix
				dimensions[0].setM(dimensions[1].getUpperBound())
				dimensions[1].setM(0)
			else: # List
				dimensions[0].setM(0)
			isList = True
			self.functions_directory.addChar(self.function_name, False, total)
		elif re.search("list(\[[0-9]+\])+string", type) is not None:
			total = 1
			start = 0
			isFirst = True
			counter = 0
			for i in range(0, len(type)):
				if type[i] == '[':
					size = 1
					while (type[i+1] != ']'):
						if isFirst:
							start = i + 1;
							isFirst = not isFirst
						size += 1
						i += 1
					counter += 1
					dim = int(int(type[start : start+size-1]))
					total *= dim
					dimension = Dimensions(0, dim)
					dimensions.append(dimension)
					isFirst = True
					start = 0
			if counter == 2: # Matrix
				dimensions[0].setM(dimensions[1].getUpperBound())
				dimensions[1].setM(0)
			else: # List
				dimensions[0].setM(0)
			isList = True
			self.functions_directory.addString(self.function_name, False, total)
		elif re.search("list(\[[0-9]+\])+bool", type) is not None:
			total = 1
			start = 0
			isFirst = True
			counter = 0
			for i in range(0, len(type)):
				if type[i] == '[':
					size = 1
					while (type[i+1] != ']'):
						if isFirst:
							start = i + 1;
							isFirst = not isFirst
						size += 1
						i += 1
					counter += 1
					dim = int(type[start : start+size-1])
					total *= dim
					dimension = Dimensions(0, dim)
					dimensions.append(dimension)
					isFirst = True
					start = 0
			if counter == 2: # Matrix
				dimensions[0].setM(dimensions[1].getUpperBound())
				dimensions[1].setM(0)
			else: # List
				dimensions[0].setM(0)
			isList = False
			self.functions_directory.addBool(self.function_name, False, total)
		self.functions_directory.getInfoDirectory(self.function_name).push_frame(id, type, isList, total, counter, dimensions)

	# Se añade una función al directorio de funciones junto con sus parametros
	def newFunction(self):
		if self.function_name not in self.functions_directory.getDirectory():
			self.functions_directory.create_table(self.function_name, InfoDirectory())
			self.functions_directory.getTable(self.function_name).setParamTable(self.argumentos)
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
		if id in self.argumentos.getParameters():
			print("Syntax error!! Variable: " + id + " is already defined")
			sys.exit(0)
		else:
			isList = False
			total = 1
			dimensions = []
			counter = 0
			if type == "int":
				type_number = 0
				counter += 1
				# self.functions_directory.getSymbolTable(self.function_name).addInteger(True)
			elif type == "float":
				type_number = 1
				counter += 1
				# self.functions_directory.getSymbolTable(self.function_name).addFloat(True)
			elif type == "char":
				type_number = 2
				counter += 1
				# self.functions_directory.getSymbolTable(self.function_name).addChar(True)
			elif type == "string":
				type_number = 3
				counter += 1
				# self.functions_directory.getSymbolTable(self.function_name).addString(True)
			elif type == "bool":
				type_number = 4
				counter += 1
				# self.functions_directory.getSymbolTable(self.function_name).addBool(True)
			elif type == "null":
				type_number = 5
				counter += 1
			elif re.search("list(\[[0-9]+\])+int", type) is not None:
				type_number = 0
				isList = True
				total = 1
				start = 0
				isFirst = True
				counter = 0
				for i in range(0, len(type)):
					if type[i] == '[':
						size = 1
						while (type[i+1] != ']'):
							if isFirst:
								start = i + 1;
								isFirst = not isFirst
							size += 1
							i += 1
						counter += 1
						dim = int(type[start: start+size-1])
						dimension = Dimensions(0, dim)
						dimensions.append(dimension)
						total *= dim
						isFirst = True
						start = 0
				if counter == 2: # Matrix
					dimensions[0].setM(dimensions[1].getUpperBound())
					dimensions[1].setM(0)
				else: # List
					dimensions[0].setM(0)
			elif re.search("list(\[[0-9]+\])+float", type) is not None:
				type_number = 1
				isList = True
				total = 1
				start = 0
				isFirst = True
				counter = 0
				for i in range(0, len(type)):
					if type[i] == '[':
						size = 1
						while (type[i+1] != ']'):
							if isFirst:
								start = i + 1;
								isFirst = not isFirst
							size += 1
							i += 1
						counter += 1
						dim = int(type[start : start+size-1])
						dimension = Dimensions(0, dim)
						dimensions.append(dimension)
						total *= dim
						isFirst = True
						start = 0
				if counter == 2: # Matrix
					dimensions[0].setM(dimensions[1].getUpperBound())
					dimensions[1].setM(0)
				else: # List
					dimensions[0].setM(0)
			elif re.search("list(\[[0-9]+\])+char", type) is not None:
				type_number = 2
				isList = True
				total = 1
				start = 0
				isFirst = True
				counter = 0
				for i in range(0, len(type)):
					if type[i] == '[':
						size = 1
						while (type[i+1] != ']'):
							if isFirst:
								start = i + 1;
								isFirst = not isFirst
							size += 1
							i += 1
						counter += 1
						dim = int(type[start : start+size-1])
						dimension = Dimensions(0, dim)
						dimensions.append(dimension)
						total *= dim
						isFirst = True
						start = 0
				if counter == 2: # Matrix
					dimensions[0].setM(dimensions[1].getUpperBound())
					dimensions[1].setM(0)
				else: # List
					dimensions[0].setM(0)
			elif re.search("list(\[[0-9]+\])+string", type) is not None:
				type_number = 3
				isList = True
				total = 1
				start = 0
				isFirst = True
				counter = 0
				for i in range(0, len(type)):
					if type[i] == '[':
						size = 1
						while (type[i+1] != ']'):
							if isFirst:
								start = i + 1;
								isFirst = not isFirst
							size += 1
							i += 1
						counter += 1
						dim = int(type[start : start+size-1])
						total *= dim
						dimension = Dimensions(0, dim)
						dimensions.append(dimension)
						isFirst = True
						start = 0
				if counter == 2: # Matrix
					dimensions[0].setM(dimensions[1].getUpperBound())
					dimensions[1].setM(0)
				else: # List
					dimensions[0].setM(0)
			elif re.search("list(\[[0-9]+\])+bool", type) is not None:
				type_number = 4
				isList = True
				total = 1
				start = 0
				isFirst = True
				counter = 0
				for i in range(0, len(type)):
					if type[i] == '[':
						size = 1
						while (type[i+1] != ']'):
							if isFirst:
								start = i + 1;
								isFirst = not isFirst
							size += 1
							i += 1
						counter += 1
						dim = int(type[start : start+size-1])
						total *= dim
						dimension = Dimensions(0, dim)
						dimensions.append(dimension)
						isFirst = True
						start = 0
				if counter == 2: # Matrix
					dimensions[0].setM(dimensions[1].getUpperBound())
					dimensions[1].setM(0)
				else: # List
					dimensions[0].setM(0)
			self.argumentos.push_param(id, type_number, isList, total, counter, dimensions)

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
		self.argumentos = ParamTable()

	def exitBloqueConstructor(self, ctx):
		self.argumentos = ParamTable()
		self.functions_directory.remove_info(self.function_name)

	# Constructores
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
		cuadruplo = Quadruple(self.id, "=", valor, None, id)
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
			if new_type == 0:
				self.functions_directory.addTempInt(self.function_name, 1)
			elif new_type == 1:
				self.functions_directory.addTempFloat(self.function_name, 1)
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
			if new_type == 0:
				self.functions_directory.addTempInt(self.function_name, 1)
			elif new_type == 1:
				self.functions_directory.addTempFloat(self.function_name, 1)

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
			self.functions_directory.addTempBool(self.function_name, 1)

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
			self.functions_directory.addTempBool(self.function_name, 1)
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

		condition = self.operandos.pop()
		quadruple = Quadruple(self.id, GO.TOFALSE, condition , None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos) - 1)

	def exitAfterWhile(self, ctx):
		self.pending_jumps.push(len(self.cuadruplos))

	def enterAfterWhileExpression(self, ctx):
		condition = self.operandos.pop()
		exp_type = self.types.pop()
		if exp_type != 4:
			print("The result of the expression must be boolean")
			sys.exit(0)

		quadruple = Quadruple(self.id, GO.TOFALSE, condition, None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos)-1)

	def exitExitWhile(self, ctx):
		end = self.pending_jumps.pop()
		ret = self.pending_jumps.pop()
		quadruple = Quadruple(self.id, GO.TO, None, None, ret + 1)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.fill(end, len(self.cuadruplos) + 1)

	def exitAfterDo(self, ctx):
		cuadruplo = Quadruple(self.id, '=', 1, None, 'temp-while')
		self.cuadruplos.append(cuadruplo)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos) + 1)

	def exitAfterCondition(self, ctx):
		condition = self.operandos.pop()
		quadruple = Quadruple(self.id, GO.TOFALSE, condition, None, None)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.pending_jumps.push(len(self.cuadruplos)-1)

	def enterDoAux(self, ctx):
		if ctx.objeto() is not None:
			self.do_object = True
		elif ctx.TYPE_INT() is not None:
			cte = ctx.TYPE_INT().getText()
			registro = "r" + str(self.registros)
			cuadruplo = Quadruple(self.id, '<=', 'temp-while', cte, registro)
			self.operandos.push(registro)
			self.registros += 1
			self.cuadruplos.append(cuadruplo)
			self.id += 1
		else:
			print("Do while parameter wrong")
			sys.exit(0)

	def exitDoAux(self, ctx):
		self.do_object = False

	def exitAfterDoLoop(self, ctx):
		registro = "r" + str(self.registros)
		quadruple = Quadruple(self.id, '+', 'temp-while', 1, registro)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.registros += 1
		self.operandos.push(registro)

		registro = "r" + str(self.registros)
		quadruple = Quadruple(self.id, '=', self.operandos.pop(), None, 'temp-while')
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.registros += 1

		end = self.pending_jumps.pop()
		ret = self.pending_jumps.pop()
		quadruple = Quadruple(self.id, GO.TO, None, None, ret)
		self.cuadruplos.append(quadruple)
		self.id += 1
		self.fill(end, len(self.cuadruplos) + 1)

	def enterDecInc(self, ctx):
		var = ctx.objeto().getText()
		if ctx.decIncAux().INCREMENT_OPERATOR() is not None:
			type = self.getTypeFromVariable(var)
			type = self.convertTypeToInt(type)
			new_type = np.int64(self.oraculo.getDataType(type, 0, 0))
			if new_type == -1:
				print("Data type mismatch")
				sys.exit(0)

			registro = "r" + str(self.registros)
			quadruple = Quadruple(self.id, '+', var, 1, registro)
			self.cuadruplos.append(quadruple)
			self.registros += 1
			self.id += 1
			self.operandos.push(registro)


			registro = "r" + str(self.registros)
			quadruple = Quadruple(self.id, '=', self.operandos.pop(), None, var)
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
			quadruple = Quadruple(self.id, '-', var, 1, registro)
			self.cuadruplos.append(quadruple)
			self.registros += 1
			self.id += 1
			self.operandos.push(registro)


			registro = "r" + str(self.registros)
			quadruple = Quadruple(self.id, '=', self.operandos.pop(), None, var)
			self.cuadruplos.append(quadruple)
			self.registros += 1
			self.id += 1

	def exitEnterElse(self, ctx):
		quadruple = Quadruple(self.id, GO.TO, None, None, None)
		self.id += 1
		self.cuadruplos.append(quadruple)
		false = self.pending_jumps.pop()
		self.pending_jumps.push(len(self.cuadruplos) - 1)
		self.fill(false, len(self.cuadruplos)+1)

	def enterCondicion(self, ctx):
		self.pending_jumps.push(-1)


	def exitEndIf(self, ctx):
		end = self.pending_jumps.pop()
		while (end != -1):
			self.fill(end, len(self.cuadruplos)+1)
			end = self.pending_jumps.pop()
		if end == -1:
			self.pending_jumps.pop

	def enterEscritura(self, ctx):
		quadruple = Quadruple(self.id, "print", ctx.megaExpresion().getText(), None, None)
		self.id += 1
		self.cuadruplos.append(quadruple)

	def enterEscrituraAux(self, ctx):
		if ctx.COMMA() is not None:
			quadruple = Quadruple(self.id, "print",  ctx.megaExpresion().getText(), None, None)
			self.id += 1
			self.cuadruplos.append(quadruple)

	def enterLectura(self, ctx):
		quadruple = Quadruple(self.id, "read", ctx.ID().getText(), None, None)
		self.id += 1
		self.cuadruplos.append(quadruple)

	def enterLecturaAux(self, ctx):
		if ctx.INPUT_STREAM() is not None:
			quadruple = Quadruple(self.id, "read",  ctx.ID().getText(), None, None)
			self.id += 1
			self.cuadruplos.append(quadruple)

	def enterLlamadaFunc(self, ctx):
		if ctx.THIS() is not None or len(ctx.ID()) == 1: #Local method
			self.current_method_name = ctx.ID()[0].getText()
			if self.current_method_name not in  self.functions_directory.getDirectory():
				print("The function: " + str(self.current_method_name)+ " doesn't exist")
				sys.exit(0)
			quadruple = Quadruple("ERA", self.current_method_name, None, None)
			self.cuadruplos.append(quadruple)
			self.current_param_counter = 0

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

	def exitVerifyArgument(self, ctx):

		argument = self.operandos.pop()
		argument_type = self.types.pop()

		argument_type = self.normalizeTypes(argument_type)
		parameter_type = self.functions_directory.getTable(self.current_method_name).getParams()[self.current_param_counter][1]
		parameter_type = self.normalizeTypes(parameter_type)
		parameter = self.functions_directory.getTable(self.current_method_name).getParams()[self.current_param_counter][0]	
		dimensions_param = self.functions_directory.getTable(self.current_method_name).getParamTable().getParam(parameter).getRows()
		dimensions_argument = 1
		all_dimensions_argument = []
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
					print("The function " + str(self.current_method_name) + " was expecting a matrix of: " + str(dimensions_param) + " x " + str(dimP.getUpperBound()) + " but received a matrix of: " + str(dimensions_argument) + " x " + str(dimA.getUpperBound()))
					sys.exit(0)
				else:
					print("The function " + str(self.current_method_name) + " was expecting a list of " + str(dimP.getUpperBound()) + " but received a list of " + str(dimA.getUpperBound()))
				sys.exit(0)



	def exitAddArgument(self, ctx):
		self.current_param_counter += 1

	def exitLlamadaFunc(self, ctx):
		if self.current_param_counter != len(self.functions_directory.getTable(self.current_method_name).getParams()):
			print("The function call: " + self.current_method_name + " doesn't have the same number of arguments")
			print(str(self.current_param_counter) + " were given, but " + str(len(self.functions_directory.getTable(self.current_method_name).getParams())) + " were expected")
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