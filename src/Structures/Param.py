class Param(object):

	def __init__(self, id, type, isList, listSize, dim, dimensions):
		self.id = id
		self.type = type
		self.isList = isList
		self.listSize = listSize
		self.dim = dim
		self.dimensions = dimensions

	def getType(self):
		return self.type

	def isList(self):
		return self.isList

	def getListSize(self):
		return self.listSize

	def getRows(self):
		return self.dim

	def getDimensions(self):
		return self.dimensions