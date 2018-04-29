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
	def setType(self, id, type):
		self.parameters[id].setType(type)
	def getAddress(self, id):
		return self.parameters[id].getAddress()
	def getDimensions(self, id):
		return self.parameters[id].getDimensions()
	def getSize(self, id):
		return self.parameters[id].getListSize()
	def getId(self, id):
		return self.parameters[id].getId()