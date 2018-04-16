from Structures.Dimensions import Dimensions

class Info(object):
	def __init__(self, type=None, isList=None, listSize=0, dim = 0, dimensions = None, address = 0):
		if type is None:
			self._info = []
		else:
			self._info = [type, isList, listSize, dim, dimensions, address]
	def getInfo(self):
		return self._info
	def getType(self):
		if not self._info:
			return []
		else:
			return self._info[0]
	def isList(self):
		return self._info[1]
	def getListSize(self):
		return self._info[2]
	def getDim(self):
		return self._info[3]
	def getDimensions(self):
		return self._info[4]
	def getLowerBound(self, dim):
		return self._info[4][dim].getLowerBound()
	def getUpperBound(self, dim):
		return self._info[4][dim].getUpperBound()
	def getM(self, dim):
		return self._info[4][dim].getM()
	def getAddress(self):
		return self._info[5]