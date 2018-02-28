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
COMMA : ',';
// Reserved words
PRINT : 'print';
THIS : 'this';
CLASS : 'Class';
INHERITS : 'Inherits';
ATTRIBUTES : 'Attributes';
PUBLIC : 'public';
PRIVATE : 'private';
PROTECTED : 'protected';
METHODS : 'Methods';
FUNCTION : 'function';
RETURNS : 'returns';
RETURN : 'return';
IMPORT : 'import';
MAIN : 'main';
LIST : 'list';
READ : 'read';
VAR : 'var';
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

inicio:
	clase
	;

clase :
	CLASS CLASSNAME claseAux bloqueClase
	;

claseAux :
	INHERITS CLASSNAME
	|
	;

bloqueClase :
	LEFT_CURLY_BRACKET constructor atributos metodos RIGHT_CURLY_BRACKET impFunc
	;

constructor :
	CLASSNAME LEFT_PARENTHESIS constructorAux RIGHT_PARENTHESIS SEMICOLON constructorAux2
	;

constructorAux :
	argumentos
	|
	;

constructorAux2 :
	constructor
	| 
	;

atributos :
	ATTRIBUTES LEFT_CURLY_BRACKET atributosPublic atributosPrivate RIGHT_CURLY_BRACKET
	;

atributosPublic :
	PUBLIC COLON vars_ atributosPublicAux
	|
	;
atributosPublicAux :
	vars_ atributosPublicAux
	|
	;

atributosPrivate :
	PRIVATE COLON vars_
	|
	;

atributosPrivateAux:
	vars_ atributosPrivateAux
	|
	;

atributosProtected :
	PROTECTED COLON vars_
	|
	;

metodos :
	METHODS LEFT_CURLY_BRACKET metodosPublicos metodosPrivados RIGHT_CURLY_BRACKET
	;

metodosPublicos :
	PUBLIC COLON func SEMICOLON metodosPublicosAux
	| PUBLIC COLON
	;

metodosPublicosAux :
	func SEMICOLON metodosPublicosAux
	|
	;

metodosPrivados :
	PRIVATE COLON func SEMICOLON metodosPrivadosAux
	| PRIVATE SEMICOLON
	;

metodosPrivadosAux :
	func SEMICOLON metodosPrivadosAux
	|
	;

func :
	FUNCTION ID LEFT_PARENTHESIS argumentos RIGHT_PARENTHESIS funcAux;

funcAux:
	RETURNS
	|
	;

impFunc :
	FUNCTION ID LEFT_PARENTHESIS argumentos RIGHT_PARENTHESIS impFuncAux2 bloqueFunc
	;

impFuncAux2 :
	RETURNS
	|
	;

argumentos:
	tipo_dato ID argumentosAux
	|
	;

argumentosAux:
	COMMA tipo_dato ID argumentosAux
	|
	;

bloqueFunc :
	LEFT_CURLY_BRACKET bloqueFuncAux bloqueFuncAux2 RIGHT_CURLY_BRACKET
	;

bloqueFuncAux :
	estatuto bloqueFuncAux
	|
	;

bloqueFuncAux2 :
	RETURN TYPE_INT SEMICOLON
	|
	;

vars_ :
	VAR ID varsAux COLON tipo_dato SEMICOLON varsRepeated
	;

varsAux:
	COMMA ID varsAux
	|
	;

varsRepeated:
	ID varsAux COLON tipo_dato SEMICOLON varsRepeated
	|
	;

tipo_dato:
	INT
	| FLOAT
	| CHAR
	| STRING
	;

tipo : 
	TYPE_INT
	| TYPE_FLOAT
	| TYPE_CHAR
	| TYPE_STRING
	;

estatuto:
	escritura
	;

escritura:
	PRINT LEFT_PARENTHESIS TYPE_STRING RIGHT_PARENTHESIS SEMICOLON
	;