from enum import Enum
"""
ENUM que encapsula todos los posibles saltos
"""
class GO(Enum):
	TOFALSE = 1
	TOTRUE = 2
	TO = 3
	SUB = 4