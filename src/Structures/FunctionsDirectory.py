import sys

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
			sys.exit(0)
		else:
			self.directory[id].deleteTable()

	def addParam(self, id, name, value, size):
		self.directory[id].addParameter(name, value, size)

	def getInfoDirectory(self, id):
		return self.directory[id].getSymbolTable()

	def getTable(self, id):
		return self.directory[id]

	def getDirectory(self):
		return self.directory