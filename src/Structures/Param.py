"""
Clase Param que almacena toda la informacion del parametro
La información que se guarda es:
tipo : int
isList: bool
listSize : int
dim : int
dimensions : Dimensions
"""
class Param(object):

	"""
	Inicializa la informacion del parametro
	"""
	def __init__(self, id, type, isList, listSize, dim, dimensions, address):
		self.id = id
		self.type = type
		self.isList = isList
		self.listSize = listSize
		self.dim = dim
		self.dimensions = dimensions
		self.address = address

	"""
	Regresa el Id del paramero
	"""
	def getId(self):
		return self.id

	"""
	Regresa el tipo del parametro
	"""
	def getType(self):
		return self.type

	"""
	Asigna el tipo al parametro
	"""
	def setType(self, type):
		self.type = type

	"""
	Regresa un booleano indicando si es lista
	"""
	def isList(self):
		return self.isList

	"""
	Regresa el tamano de la lista
	"""
	def getListSize(self):
		return self.listSize

	"""
	Regresa la cantidad de dimensiones del parametro
	"""
	def getRows(self):
		if not self.isList:
			return 0
		return self.dim

	"""
	Regresa el objeto dimensiones
	"""
	def getDimensions(self):
		return self.dimensions

	"""
	Regresa la direccion del parametro
	"""
	def getAddress(self):
		return self.address