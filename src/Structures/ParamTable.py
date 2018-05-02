from Structures.Param import Param

"""
Clase ParamTable que almacena en un diccionario la informacion de los parametros de una funcion. La llave es el id del parametro y el valor es un objeto Param que contiene toda la informacion del parametro.
"""
class ParamTable(object):
	"""
	Inicializa el diccionario vacio
	"""
	def __init__(self):
		self.parameters = dict()
	"""
	Almacena la informacion de un parametro
	La informacion que recibe el parametro es:
	id : int
	type : int
	isList : bool
	listSize : int
	dim : int
	dimensions : Dimension
	address : int
	"""
	def push_param(self, id, type, isList, listSize, dim, dimensions, address):
		self.parameters[id] = Param(id, type, isList, listSize, dim, dimensions, address)
	"""
	Regresa la informacion de un parametro. Si no existe regresa una lista vacia
	"""
	def getParam(self, id):
		if id in self.parameters:
			return self.parameters[id]
		else:
			return []
	"""
	Regresa el diccionario de parametros
	"""
	def getParameters(self):
		return self.parameters
	"""
	Regresa el tipo del parametro
	"""
	def getType(self, id):
		return self.parameters[id].getType()
	"""
	Asigna el tipo al parametro
	"""
	def setType(self, id, type):
		self.parameters[id].setType(type)
	"""
	Regresa la direccion del parametro
	"""
	def getAddress(self, id):
		return self.parameters[id].getAddress()
	"""
	Regresa las dimensiones del parametro
	"""
	def getDimensions(self, id):
		return self.parameters[id].getDimensions()
	"""
	Regresa el tamano de la variable
	"""
	def getSize(self, id):
		return self.parameters[id].getListSize()
	"""
	Regresa el ID de la variable
	"""
	def getId(self, id):
		return self.parameters[id].getId()