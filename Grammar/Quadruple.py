class Quadruple(object):

	def __init__(self, int operator, string operand1=None, string operand2=None, string result=None):
		self.operator = operator
		self.operand1 = operand1
		self.operand2 = operand2
		self.result = result

	def getOperator(self):
		return self.operator

	def getOperand1(self):
		return self.operand1

	def getOperand2(self):
		return self.operand2

	def getResult(self):
		return self.result