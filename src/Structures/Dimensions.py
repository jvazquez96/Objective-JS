class Dimensions(object):

	def __init__(self, lower=None, upper=None, m=None):
		self.lower = lower
		self.upper = upper
		self.m = m

	def getLowerBound(self):
		return self.lower

	def getUpperBound(self):
		return self.upper

	def getM(self):
		return m

	def setLowerBound(selfm, lowerBound):
		self.lower = lowerBound

	def setUpperBound(self, upperBound):
		self.upper = upperBound

	def setM(self, m):
		self.m = m
