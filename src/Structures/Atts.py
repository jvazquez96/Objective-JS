from Structures.Dimensions import Dimensions

class Atts(object):
	def __init__(self, id=None, type=None, accessible=False, isList=None, listSize=0, dim = 0, dimensions = None, address = None):
		if type is None:
			self._info = []
		else:
			self._info = [id, type, accessible, isList, listSize, dim, dimensions, address]
	
	def getId(self):
		return self._info[0]

	def getType(self):
		return self._info[1]

	def setType(self, type):
		self._info[1] = type

	def isAccessible(self):
		return self._info[2]

	def isList(self):
		return self._info[3]

	def getListSize(self):
		return self._info[4]

	def getDim(self):
		return self._info[5]

	def getDimensions(self):
		return self._info[6]

	def getLowerBound(self, dim):
		return self._info[6][dim].getLowerBound()

	def getUpperBound(self, dim):
		return self._info[6][dim].getUpperBound()

	def getM(self, dim):
		return self._info[6][dim].getM()

	def getAddress(self):
		return self._info[7]