import sys
"""
Clase FunctionDirectory que almacena la información de cada función.
Se almacena en el formato llave : valor, donde la llave es el nombre
de la función y el valor es un Objecto de tipo Infodirectory.
"""
class FunctionsDirectory(object):

	"""
	Inicia el directorio vacio
	"""
	def __init__(self):
		self.directory = dict()

	"""
	Crea un InfoDirectory para el id de la función que se recibe
	como parametro. Si el id ya se encuentra en el diccionario
	el programa termina.
	El tipo de los parametros son: id es un string, info es un InfoDirectory
	"""
	def create_table(self, id, info):
		if id in self.directory:
			print("Syntax error!! Function already defined")
			sys.exit(0)
		else:
			self.directory[id] = info

	"""
	Remueve la información de una función. Si se desea remover la información
	de una función que no existe el programa termina.
	El tipo de los parametros son: id es un string, info es un InfoDirectory
	"""
	def remove_info(self, id):
		if id not in self.directory:
			sys.exit(0)
		else:
			self.directory[id].deleteTable()

	"""
	Crea un InfoDirectory para el id de la función que se recibe
	como parametro. Si el id ya se encuentra en el diccionario
	el programa termina.
	El tipo de los parametros son: id es un string, info es un InfoDirectory
	"""
	def addParam(self, id, name, value, size):
		self.directory[id].addParameter(name, value, size)

	"""
	Regresa la tabla de simbolos de una función.
	El parametro id es un string.
	El valor de retorno es un Objeto SymbolTable
	"""
	def getInfoDirectory(self, id):
		return self.directory[id].getSymbolTable()

	"""
	Regresa el InfoDirectory del ID que recibe como parametro.
	El parametro id es un string.
	El valor de retorno es un Objeto InfoDirectory
	"""
	def getTable(self, id):
		return self.directory[id]

	"""
	Regresa el diccionario que contiene a todas las funciones con su
	objeto InfoDirectory.
	"""
	def getDirectory(self):
		return self.directory