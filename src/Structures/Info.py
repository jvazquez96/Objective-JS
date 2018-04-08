from Structures.Dimensions import Dimensions

class Info(object):
	def __init__(self, type=None, visibility=None, isList=None, listSize=0, dim = 0, dimensions = None):
		if type is None and visibility is None:
			self._info = []
		else:
			self._info = [type, visibility, isList, listSize, dim, dimensions]
	def getInfo(self):
		return self._info
	def getType(self):
		if not self._info:
			return []
		else:
			return self._info[0]
	def getVisibility(self):
		if not self._info:
			return []
		else:
			return self._info[1]
	def isList(self):
		return self._info[2]
	def getListSize(self):
		return self._info[3]
	def getDim(self):
		return self._info[4]
	def getDimensions(self):
		return self._info[5]
	def getLowerBound(self, dim):
		return self._info[5][dim].getLowerBound()
	def getUpperBound(self, dim):
		return self._info[5][dim].getUpperBound()
	def getM(self, dim):
		return self._info[5][dim].getM()