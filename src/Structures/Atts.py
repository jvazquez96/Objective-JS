from Structures.Dimensions import Dimensions
"""
Clase Atts que almacena la información de una variable.
La información que se guarda es:
tipo : int
isList: bool
listSize : int
dim : int
dimensions : Dimensions
"""
class Atts(object):
	"""
	Inicializa la informacion de un atributo
	"""
	def __init__(self, id=None, type=None, accessible=False, isList=None, listSize=0, dim = 0, dimensions = None, address = None):
		if type is None:
			self._info = []
		else:
			self._info = [id, type, accessible, isList, listSize, dim, dimensions, address]
	"""
	Regresa el Id de un atributo
	"""
	def getId(self):
		return self._info[0]
	"""
	Regresa el tipo de una variable
	"""
	def getType(self):
		return self._info[1]

	"""
	Asigna el tipo a una variable
	"""
	def setType(self, type):
		self._info[1] = type

	"""
	Regresa la accessibilidad de una variable
	"""
	def isAccessible(self):
		return self._info[2]

	"""
	Regresa un booleano indicando si es lista o no.
	"""
	def isList(self):
		return self._info[3]

	"""
	Regresa el tamano de la lista
	"""
	def getListSize(self):
		return self._info[4]

	"""
	Regresa la cantidad de dimensiones
	"""
	def getDim(self):
		return self._info[5]

	"""
	Regresa la lista de dimensiones
	"""
	def getDimensions(self):
		return self._info[6]

	"""
	Regresa el limite inferior de una dimension
	"""
	def getLowerBound(self, dim):
		return self._info[6][dim].getLowerBound()
	"""
	Regresa el limite superior de una dimension
	"""
	def getUpperBound(self, dim):
		return self._info[6][dim].getUpperBound()
	"""
	Regresa la M de una dimension
	"""
	def getM(self, dim):
		return self._info[6][dim].getM()
	"""
	Regresa la direccion del atributo
	"""
	def getAddress(self):
		return self._info[7]