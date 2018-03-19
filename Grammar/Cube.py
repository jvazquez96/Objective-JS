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
		self.cube = {}
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

	def getDataType(self, operand1, operation, operand2):
		return self.cube{operand1, operation, operand2}

if __name__ == "__main__":
	cube = Cube()
	print(cube.getDataType(1, 0, 1))