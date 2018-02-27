grammar Objective_JS;

// Conditionals and loops
IF : 'if';
ELSE_IF : 'elsif';
DO : 'do';
TIMES : 'times';
WHILE : 'while';
// Operators
INCREMENT_OPERATOR : '++';
DECREMENT_OPERATOR : '--';
SUM_OPERATOR : '+';
SUBSTRACTION_OPERATOR : '*';
DIVISION_OPERATOR : '/';
MODULUS_OPERATOR : '%';
POWER_OPERATOR : '^';
EQUAL_OPERATOR : '==';
NOT_EQUAL_OPERATOR : '!=';
GREATER_THAN_OPERATOR : '>';
GREATER_OR_EQUAL_THAN_OPERATOR : '>=';
LESS_THAN_OPERATOR : '<';
LESS_THAN_OR_EQUAL_OPERATOR : '<=';
LOGICAL_AND_OPERATOR : '&&';
LOGICAL_OR_OPERATOR : '||';
// Special characters 	
LEFT_PARENTHESIS : '(';
RIGHT_PARENTHESIS : ')';
LEFT_SQUARE_BRACKET : '[';
RIGHT_SQUARE_BRACKET : ']';
LEFT_CURLY_BRACKET : '{';
RIGHT_CURLY_BRACKET : '}';
DOT : '.';
COLON : ':';
SEMICOLON : ';';
// Reserved words
PRINT : 'print';
THIS : 'this';
CLASS : 'Class';
INHERITS : 'Inherits';
ATTRIBUTES : 'Attributes';
PUBLIC : 'Public';
PRIVATE : 'Private';
PROTECTED : 'Protected';
METHODS : 'METHODS';
FUNCTION : 'function';
RETURNS : 'returns';
IMPORT : 'import';
MAIN : 'main';
LIST : 'list';
READ : 'read';
// Data types
TYPE_INT : ('0' .. '9')+;
TYPE_FLOAT : ('0' .. '9')+'.'('0' .. '9')+;
TYPE_CHAR : '"'[a-zA-Z]'"';
TYPE_STRING : '"'~('"')*'"';
// Types literal
INT : 'int';
FLOAT : 'float';
CHAR : 'char';
STRING : 'string';
SINGLE_QUOTES : '"';
// Classifiers
CLASSNAME : [A-Z][a-zA-Z]*;
ID : [a-zA-Z0-9]+;
// Ignore
WHITESPACE : [ \n\t\r]+ -> skip;

// Test rule just so that ANTLR doesn't complain
// Delete this when actually doing the real rules.
tipo : 
	TYPE_INT
	| TYPE_FLOAT
	| TYPE_CHAR
	| TYPE_STRING;