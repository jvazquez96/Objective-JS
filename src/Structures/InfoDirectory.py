from Structures.SymbolTable import SymbolTable
class InfoDirectory(object):
	def __init__ (self, symbol_table=None, return_type=None):
		if symbol_table is None and return_type is None:
			self._info = [SymbolTable(), None]
		else:
			self._info = [symbol_table, return_type]
		# Types of parameters [int, float, char, string, bool]
		self.parameters = [0, 0, 0, 0, 0]
		# Types of local variables [int, float, char, string, bool]
		self.local_variables = [0, 0, 0, 0, 0]

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

	def addInteger(self, isParameter=True):
		if isParameter:
			self.parameters[0] += 1
		else:
			self.local_variables[0] += 1

	def addFloat(self, isParameter = True):
		if isParameter:
			self.parameters[1] += 1
		else:
			self.local_variables[1] += 1

	def addChar(self, isParameter = True):
		if isParameter:
			self.parameters[2] += 1
		else:
			self.local_variables[2] += 1

	def addString(self, isParameter = True):
		if isParameter:
			self.parameters[2] += 1
		else:
			self.local_variables[2] += 1

	def addBool(self, isParameter = True):
		if isParameter:
			self.parameters[3] += 1
		else:
			self.local_variables[3] += 1

	def numberOfParameters(self):
		return sum(1 for item in self.parameters if item > 0)

	def numberOfLocalVariables(self):
		return sum(1 for item in self.local_variables if item > 0)

	def getParameters(self):
		return self.parameters

	def getVariables(self):
		return self.local_variables