from InfoDirectory import InfoDirectory
from SymbolTable import SymbolTable

class FunctionsDirectory(object):
	def __init__(self):
		self.directory = dict()
	def create_table(self, id, info):
		if id in self.directory:
			print("Syntax error!! Function already defined")
			sys.exit(0)
		else:
			self.directory[id] = info
	def remove_info(self, id):
		if id not in self.directory:
			print("Error")
			sys.exit(0)
		else:
			return_type = self.directory.getReturnType()
			self.directory[id] = InfoDirectory(SymbolTable(), return_type)
	def getSymbolTable(self, id):
		return self.directory[id].getSymboltable()
	def getAllSymbolsTables(self):
		return self.directory