from Structures.SymbolTable import SymbolTable
from Structures.Stack import Stack
from Structures.ParamTable import ParamTable

class InfoDirectory(object):
	def __init__ (self, return_type, symbol_table=SymbolTable()):
		self.symbol_table = symbol_table
		self.return_type = return_type
		# Types of parameters [int, float, char, string, bool, null]
		self.parameters = [0, 0, 0, 0, 0, 0]
		# Types of local variables [int, float, char, string, bool, null]
		self.local_variables = [0, 0, 0, 0, 0, 0]
		# Types of tempral variables [int, float, char, string, bool, null]
		self.temporal_variables = [0, 0, 0, 0, 0, 0]
		#
		self.parameters2 = []
		# Param table
		self.param_table = ParamTable()
		# Address where the function starts
		self.start_address = None
		self.accessible = None

	def createInfo(self, symbol_table, return_type):
		self.symbol_table = symbol_table
		self.return_type = return_type

	def setReturnType(self, type):
		self.return_type = type

	def getParamTable(self):
		return self.param_table

	def getSymbolTable(self):
		return self.symbol_table

	def getReturnType(self):
		return self.return_type

	def getParams(self):
		return self.parameters2

	def getStartAddress(self):
		return self.start_address

	def getText(self):
		return self.text

	def setParamTable(self, paramTable):
		self.param_table = paramTable

	def setStartAddress(self, address):
		self.start_address = address
		self.text = "I'm being set"

	def deleteTable(self):
		self.symbol_table = SymbolTable()

	def addParameter(self, id, type, size):
		parameter = [id, type, size]
		self.parameters2.append(parameter)

	def getParameters(self):
		return self.parameters

	def getVariables(self):
		return self.local_variables

	def setAccessibility(self, accessibility):
		self.accessible = accessibility  

	def getAccessibility(self):
		return self.accessible