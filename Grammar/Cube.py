import numpy as np

class Cube(object):
	# Data types
	ERROR = -1
	INT = 0
	FLOAT = 1
	CHAR = 2
	STRING = 3
	BOOLEAN = 4
	NULL = 5
	# Operations
	SUM = 0
	SUBSTRACTION = 1
	MULTIPLICATION = 2
	DIVISION = 3
	POWER = 4
	MOD = 5
	GREATER = 6
	LESS = 7
	GREATER_OR_EQUAL = 8
	LESS_OR_EQUAL = 9
	EQUAL = 10
	NOT_EQUAL = 11
	AND = 12
	OR = 13
	def __init__(self):
		self.cube = np.empty((6, 14, 6))
		# INT + Data types
		self.cube[self.INT, self.SUM, self.INT] = self.INT
		self.cube[self.INT, self.SUM, self.FLOAT] = self.FLOAT
		self.cube[self.INT, self.SUM, self.CHAR] = self.ERROR
		self.cube[self.INT, self.SUM, self.STRING] = self.ERROR
		self.cube[self.INT, self.SUM, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.SUM, self.NULL] = self.ERROR;
		# INT - Data types
		self.cube[self.INT, self.SUBSTRACTION, self.INT] = self.INT
		self.cube[self.INT, self.SUBSTRACTION, self.FLOAT] = self.FLOAT
		self.cube[self.INT, self.SUBSTRACTION, self.CHAR] = self.ERROR
		self.cube[self.INT, self.SUBSTRACTION, self.STRING] = self.ERROR
		self.cube[self.INT, self.SUBSTRACTION, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.SUBSTRACTION, self.NULL] = self.ERROR
		# INT * Data types
		self.cube[self.INT, self.MULTIPLICATION, self.INT] = self.INT
		self.cube[self.INT, self.MULTIPLICATION, self.FLOAT] = self.FLOAT
		self.cube[self.INT, self.MULTIPLICATION, self.CHAR] = self.ERROR
		self.cube[self.INT, self.MULTIPLICATION, self.STRING] = self.ERROR
		self.cube[self.INT, self.MULTIPLICATION, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.MULTIPLICATION, self.NULL] = self.ERROR
		# INT / Data types
		self.cube[self.INT, self.DIVISION, self.INT] = self.INT
		self.cube[self.INT, self.DIVISION, self.FLOAT] = self.INT
		self.cube[self.INT, self.DIVISION, self.CHAR] = self.ERROR
		self.cube[self.INT, self.DIVISION, self.STRING] = self.ERROR
		self.cube[self.INT, self.DIVISION, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.DIVISION, self.NULL] = self.ERROR
		# INT MOD Data types
		self.cube[self.INT, self.MOD, self.INT] = self.INT
		self.cube[self.INT, self.MOD, self.FLOAT] = self.FLOAT
		self.cube[self.INT, self.MOD, self.CHAR] = self.ERROR
		self.cube[self.INT, self.MOD, self.STRING] = self.ERROR
		self.cube[self.INT, self.MOD, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.MOD, self.NULL] = self.ERROR
		# INT > Data type
		self.cube[self.INT, self.GREATER, self.INT] = self.BOOLEAN
		self.cube[self.INT, self.GREATER, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.GREATER, self.CHAR] = self.ERROR
		self.cube[self.INT, self.GREATER, self.STRING] = self.ERROR
		self.cube[self.INT, self.GREATER, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.GREATER, self.NULL] = self.ERROR
		# INT < Data types
		self.cube[self.INT, self.LESS, self.INT] = self.BOOLEAN
		self.cube[self.INT, self.LESS, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.LESS, self.CHAR] = self.ERROR
		self.cube[self.INT, self.LESS, self.STRING] = self.ERROR
		self.cube[self.INT, self.LESS, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.LESS, self.NULL] = self.ERROR
		# INT >= Data types
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.INT] = self.BOOLEAN
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.STRING] = self.ERROR
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.GREATER_OR_EQUAL, self.NULL] = self.ERROR
		# INT <= Data types
		self.cube[self.INT, self.LESS_OR_EQUAL, self.INT] = self.BOOLEAN
		self.cube[self.INT, self.LESS_OR_EQUAL, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.LESS_OR_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.INT, self.LESS_OR_EQUAL, self.STRING] = self.ERROR
		self.cube[self.INT, self.LESS_OR_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.LESS_OR_EQUAL, self.NULL] = self.ERROR
		# INT = Data types
		self.cube[self.INT, self.EQUAL, self.INT] = self.INT
		self.cube[self.INT, self.EQUAL, self.FLOAT] = self.FLOAT
		self.cube[self.INT, self.EQUAL, self.CHAR] = self.ERROR
		self.cube[self.INT, self.EQUAL, self.STRING] = self.ERROR
		self.cube[self.INT, self.EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.EQUAL, self.NULL] = self.ERROR
		# INT != Data type
		self.cube[self.INT, self.NOT_EQUAL, self.INT] = self.ERROR
		self.cube[self.INT, self.NOT_EQUAL, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.NOT_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.INT, self.NOT_EQUAL, self.STRING] = self.ERROR
		self.cube[self.INT, self.NOT_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.NOT_EQUAL, self.NULL] = self.ERROR
		# INT && Data types
		self.cube[self.INT, self.AND, self.INT] = self.ERROR
		self.cube[self.INT, self.AND, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.AND, self.CHAR] = self.ERROR
		self.cube[self.INT, self.AND, self.STRING] = self.ERROR
		self.cube[self.INT, self.AND, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.AND, self.NULL] = self.ERROR
		# INT || Data types
		self.cube[self.INT, self.OR, self.INT] = self.ERROR
		self.cube[self.INT, self.OR, self.FLOAT] = self.ERROR
		self.cube[self.INT, self.OR, self.CHAR] = self.ERROR
		self.cube[self.INT, self.OR, self.STRING] = self.ERROR
		self.cube[self.INT, self.OR, self.BOOLEAN] = self.ERROR
		self.cube[self.INT, self.OR, self.NULL] = self.ERROR
		# FLOAT + Data types
		self.cube[self.FLOAT, self.SUM, self.INT] = self.FLOAT
		self.cube[self.FLOAT, self.SUM, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.SUM, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.SUM, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.SUM, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.SUM, self.NULL] = self.ERROR
		# FLOAT - Data types
		self.cube[self.FLOAT, self.SUBSTRACTION, self.INT] = self.FLOAT
		self.cube[self.FLOAT, self.SUBSTRACTION, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.SUBSTRACTION, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.SUBSTRACTION, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.SUBSTRACTION, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.SUBSTRACTION, self.NULL] = self.ERRORs
		# FLOAT * Data types
		self.cube[self.FLOAT, self.MULTIPLICATION, self.INT] = self.FLOAT
		self.cube[self.FLOAT, self.MULTIPLICATION, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.MULTIPLICATION, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.MULTIPLICATION, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.MULTIPLICATION, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.MULTIPLICATION, self.NULL] = self.ERROR
		# FLOAT / Data types
		self.cube[self.FLOAT, self.DIVISION, self.INT] = self.INT
		self.cube[self.FLOAT, self.DIVISION, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.DIVISION, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.DIVISION, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.DIVISION, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.DIVISION, self.NULL] = self.ERROR
		# FLOAT MOD Data types
		self.cube[self.FLOAT, self.MOD, self.INT] = self.FLOAT
		self.cube[self.FLOAT, self.MOD, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.MOD, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.MOD, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.MOD, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.MOD, self.NULL] = self.ERROR
		# FLOAT > Data type
		self.cube[self.FLOAT, self.GREATER, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.GREATER, self.FLOAT] = self.BOOLEAN
		self.cube[self.FLOAT, self.GREATER, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.GREATER, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.GREATER, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.GREATER, self.NULL] = self.ERROR
		# FLOAT < Data types
		self.cube[self.FLOAT, self.LESS, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.LESS, self.FLOAT] = self.BOOLEAN
		self.cube[self.FLOAT, self.LESS, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.LESS, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.LESS, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.LESS, self.NULL] = self.ERROR
		# FLOAT >= Data types
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.FLOAT] = self.BOOLEAN
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.GREATER_OR_EQUAL, self.NULL] = self.ERROR
		# FLOAT <= Data types
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.FLOAT] = self.BOOLEAN
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.LESS_OR_EQUAL, self.NULL] = self.ERROR
		# FLOAT = Data types
		self.cube[self.FLOAT, self.EQUAL, self.INT] = self.INT
		self.cube[self.FLOAT, self.EQUAL, self.FLOAT] = self.FLOAT
		self.cube[self.FLOAT, self.EQUAL, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.EQUAL, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.EQUAL, self.NULL] = self.ERROR
		# FLOAT != Data type
		self.cube[self.FLOAT, self.NOT_EQUAL, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.NOT_EQUAL, self.FLOAT] = self.ERROR
		self.cube[self.FLOAT, self.NOT_EQUAL, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.NOT_EQUAL, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.NOT_EQUAL, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.NOT_EQUAL, self.NULL] = self.ERROR
		# FLOAT && Data types
		self.cube[self.FLOAT, self.AND, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.AND, self.FLOAT] = self.ERROR
		self.cube[self.FLOAT, self.AND, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.AND, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.AND, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.AND, self.NULL] = self.ERROR
		# FLOAT|| Data types
		self.cube[self.FLOAT, self.OR, self.INT] = self.ERROR
		self.cube[self.FLOAT, self.OR, self.FLOAT] = self.ERROR
		self.cube[self.FLOAT, self.OR, self.CHAR] = self.ERROR
		self.cube[self.FLOAT, self.OR, self.STRING] = self.ERROR
		self.cube[self.FLOAT, self.OR, self.BOOLEAN] = self.ERROR
		self.cube[self.FLOAT, self.OR, self.NULL] = self.ERROR	

	def getDataType(self, operand1, operation, operand2):
		return self.cube[operand1, operation, operand2]

if __name__ == "__main__":
	cube = Cube()
	print(cube.getDataType(0, 0, 3))