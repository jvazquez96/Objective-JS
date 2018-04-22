class Param(object):

	def __init__(self, id, type, isList, listSize, dim, dimensions, address):
		self.id = id
		self.type = type
		self.isList = isList
		self.listSize = listSize
		self.dim = dim
		self.dimensions = dimensions
		self.address = address

	def getId(self):
		return self.id

	def getType(self):
		return self.type

	def isList(self):
		return self.isList

	def getListSize(self):
		return self.listSize

	def getRows(self):
		if not self.isList:
			return 0
		return self.dim

	def getDimensions(self):
		return self.dimensions

	def getAddress(self):
		return self.address