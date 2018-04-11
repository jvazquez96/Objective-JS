from Structures.Param import Param

class ParamTable(object):
	def __init__(self):
		self.parameters = dict()
	def push_param(self, id, type, isList, listSize, dim, dimensions, address):
		self.parameters[id] = Param(id, type, isList, listSize, dim, dimensions, address)
	def getParam(self, id):
		if id in self.parameters:
			return self.parameters[id]
		else:
			return []
	def getParameters(self):
		return self.parameters
	def getType(self, id):
		return self.parameters[id].getType()
	def getAddress(self, id):
		return self.parameters[id].getAddress()