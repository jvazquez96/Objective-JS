class Quadruple(object):

	def __init__(self, operator=None, operand1=None, operand2=None, result=None):
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

	def print(self):
		print(str(self.operator) + " " + str(self.operand1) + " " + str(self.operand2) + " " + str(self.result))