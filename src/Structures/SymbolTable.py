from Structures.Info import Info
from Structures.Dimensions import Dimensions

class SymbolTable(object):
	def __init__(self):
		self._symbols = dict()
	def push_frame(self, address, id, type=None, attribute=None, isList = None, listSize = 0, dim = 0, dimensions = None):
		self._symbols[id] = Info(type, attribute, isList, listSize, dim, dimensions, address);
	def size(self):
		return len(self._symbols)
	def getContent(self, id):
		if id in self._symbols:
			return self._symbols[id]
		else:
			return []
	def getSymbols(self):
		return self._symbols
	def getDimensions(self, id):
		return self._symbols[id].getDim()