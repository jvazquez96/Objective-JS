from Structures.SymbolTable import SymbolTable
class InfoDirectory(object):
	def __init__ (self, symbol_table=None, return_type=None):
		if symbol_table is None and return_type is None:
			self._info = [SymbolTable(), None]
		else:
			self._info = [symbol_table, return_type]
	def getInfo(self):
		return self._info
	def createInfo(self, symbol_table, return_type):
		self._info = InfoDirectory(symbol_table, return_type)
	def getSymbolTable(self):
		return self._info[0]
	def getReturnType(self):
		return self._info[1]
	def deleteTable(self):
		self._info[0] = SymbolTable()