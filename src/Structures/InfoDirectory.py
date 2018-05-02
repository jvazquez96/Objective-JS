from Structures.SymbolTable import SymbolTable
from Structures.Stack import Stack
from Structures.ParamTable import ParamTable


"""
Clase InfoDirectory que almacena la información de una función.
"""
class InfoDirectory(object):
	"""
	Los atributos de la clase son:
	symbol_table : Informacion de todas las variables
	return_tyoe : Int que indica el valor de retorno
	parametrs : Lista que contiene la informacion de cuantos parametros por tipo se necesitan
	parameters2 : Lista que contiene el tipo literal de cada parametro.
	start_address : Direccion de inicio de cada funcion (Int)
	accessible : Booleano que indica si la función es publica o privada
	"""
	def __init__ (self, return_type, symbol_table=SymbolTable()):
		self.symbol_table = symbol_table
		self.return_type = return_type
		# Types of parameters [int, float, char, string, bool, null]
		self.parameters = [0, 0, 0, 0, 0, 0]
		self.parameters2 = []
		# Param table
		self.param_table = ParamTable()
		# Address where the function starts
		self.start_address = None
		self.accessible = None

	"""
	Almacena la tabla de simbolos y el tipo de retorno en la variable correspondiente
	"""
	def createInfo(self, symbol_table, return_type):
		self.symbol_table = symbol_table
		self.return_type = return_type

	"""
	Asigna el valor de retorno
	"""
	def setReturnType(self, type):
		self.return_type = type

	"""
	Regresa la tabla de parametros
	"""
	def getParamTable(self):
		return self.param_table

	"""
	Regresa la tabla de simbolos (SymbolTablee)
	"""
	def getSymbolTable(self):
		return self.symbol_table

	"""
	Regresa el tipo de retorno de la función
	"""
	def getReturnType(self):
		return self.return_type

	"""
	Regresa la lista de parametros literal
	"""
	def getParams(self):
		return self.parameters2

	"""
	Regresa la direccion de inicio
	"""
	def getStartAddress(self):
		return self.start_address

	"""
	Asigna la tabla de parametros que se recibe como parametro.
	El objeto es de tipo ParamTable.
	"""
	def setParamTable(self, paramTable):
		self.param_table = paramTable

	"""
	Asigna la direccion de inicio de la funcion.
	"""
	def setStartAddress(self, address):
		self.start_address = address

	"""
	Borra la tabla de simbolos de la funcion.
	"""
	def deleteTable(self):
		self.symbol_table = SymbolTable()

	"""
	agrega un parametro a la lista de parametros
	"""
	def addParameter(self, id, type, size):
		parameter = [id, type, size]
		self.parameters2.append(parameter)

	"""
	Regresa la lista que contiene la cantidad de parametros por tipo
	"""
	def getParameters(self):
		return self.parameters

	"""
	Asigna la accesibilidad a la función
	"""
	def setAccessibility(self, accessibility):
		self.accessible = accessibility  

	"""
	Regresa la accesibildad de la función
	"""
	def getAccessibility(self):
		return self.accessible