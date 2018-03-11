import sys
from antlr4 import *
from Info import Info
from Objective_JSLexer import Objective_JSLexer
from Objective_JSParser import Objective_JSParser
from Objective_JSListener import Objective_JSListener
from SymbolTable import SymbolTable
from InfoDirectory import InfoDirectory
from FunctionsDirectory import FunctionsDirectory

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

	def getFunctionDirectory(self):
		return self.functions_directory

	def getSymbolsTables(self):
		return self.functions_directory.getDirectory()

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
		self.newVars(id, self.type, self.visibility)

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
			self.argumentos.push_frame(id, type, visibility)

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