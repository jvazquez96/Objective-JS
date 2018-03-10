grammar Objective_JS;

// Conditionals and loops
IF : 'if';
ELSE : 'else';
ELSE_IF : 'elsif';
DO : 'do';
TIMES : 'times';
WHILE : 'while';
// Operators
INCREMENT_OPERATOR : '++';
DECREMENT_OPERATOR : '--';
MULTIPLICATION_OPERATOR : '*';
DIVISION_OPERATOR : '/';
MODULUS_OPERATOR : '%';
POWER_OPERATOR : '^';
EQUAL_OPERATOR : '==';
ASSIGNMENT : '=';
SUM_OPERATOR : '+';
SUBSTRACTION_OPERATOR : '-';
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
INPUT_STREAM : '>>';
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
SINGLE_QUOTES : '"';
// Data types
TYPE_INT : ('0' .. '9')+;
TYPE_FLOAT : ('0' .. '9')+'.'('0' .. '9')+;
TYPE_CHAR : '"'[a-zA-Z]'"';
TYPE_STRING : '"'~('"')*'"';
TYPE_BOOL : ('true'|'false');
// Types literal
INT : 'int';
FLOAT : 'float';
CHAR : 'char';
STRING : 'string';
// Classifiers
CLASSNAME : [A-Z][a-zA-Z]*;
ID : [a-zA-Z0-9]+;
// Ignore
WHITESPACE : [ \n\t\r]+ -> skip;

// Test rule just so that ANTLR doesn't complain
// Delete this when actually doing the real rules.

inicio:
	clase
	| main
	;

main :
	imports class_declaration
	;

clase :
	CLASS CLASSNAME claseAux bloqueClase
	;

imports :
	IMPORT ID imports
	|
	;

class_declaration :
	CLASS CLASSNAME LEFT_CURLY_BRACKET preVars impFunc MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS bloque RIGHT_CURLY_BRACKET
	;

bloque :
	LEFT_CURLY_BRACKET preEstatuto RIGHT_CURLY_BRACKET
	;

preEstatuto :
	estatuto preEstatuto
	|
	;

claseAux :
	INHERITS CLASSNAME
	|
	;

bloqueClase :
	LEFT_CURLY_BRACKET constructor atributos metodos RIGHT_CURLY_BRACKET impConstructores impFunc
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

impConstructores :
	impConstructor impConstructoresMultiples
	;

impConstructoresMultiples :
	impConstructor
	|
	;

impConstructor :
	CLASSNAME LEFT_PARENTHESIS argumentos RIGHT_PARENTHESIS LEFT_CURLY_BRACKET bloqueConstructor RIGHT_CURLY_BRACKET
	;

impFunc :
	FUNCTION ID LEFT_PARENTHESIS argumentos RIGHT_PARENTHESIS impFuncAux2 bloqueFunc impFunc
	|
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

bloqueConstructor :
	asignacion bloqueConstructorAux
	;

bloqueConstructorAux:
	asignacion bloqueConstructor
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
	RETURN megaExpresion SEMICOLON
	|
	;

preVars :
	vars_
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
	VAR ID varsAux COLON tipo_dato SEMICOLON varsRepeated
	|
	;

tipo_dato:
	tipo_dato_list tipo_dato_no_list
	| tipo_dato_no_list
	;

tipo_dato_list:
	LIST dim 
	;

dim :
	LEFT_SQUARE_BRACKET TYPE_INT RIGHT_SQUARE_BRACKET dimMatrix
	;

dimMatrix :
	LEFT_SQUARE_BRACKET TYPE_INT RIGHT_SQUARE_BRACKET
	|
	;

tipo_dato_no_list:
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

estatuto :
	asignacion
	| condicion
	| escritura
	| ciclos
	| vars_
	| llamadaFunc
	| lectura
	| decInc
	;

asignacion :
	objeto ASSIGNMENT megaExpresion SEMICOLON
	;

condicion :
	IF condicionAux
	;

condicionAux :
	LEFT_PARENTHESIS megaExpresion RIGHT_PARENTHESIS bloque condicionChoice
	;

condicionChoice :
	ELSE_IF condicionAux
	| ELSE bloque
	|
	;

escritura :
	PRINT LEFT_PARENTHESIS megaExpresion escrituraAux RIGHT_PARENTHESIS SEMICOLON
	;

escrituraAux :
	SUM_OPERATOR megaExpresion escrituraAux
	|
	;

ciclos :
	DO doAux TIMES bloque
	| WHILE LEFT_PARENTHESIS megaExpresion RIGHT_PARENTHESIS bloque
	;

doAux :
	objeto
	| TYPE_INT
	;

llamadaFunc :
	objeto LEFT_PARENTHESIS argumentosLlamada RIGHT_PARENTHESIS SEMICOLON
	;

argumentosLlamada :
	objeto argumentosLlamadaAux
	| megaExpresion argumentosLlamadaAux
	;

argumentosLlamadaAux :
	COMMA argumentosLlamada
	|
	;

lectura :
	READ INPUT_STREAM ID lecturaAux SEMICOLON
	;

lecturaAux :
	INPUT_STREAM ID lecturaAux
	|
	;

decInc :
	objeto decIncAux SEMICOLON
	;

decIncAux :
	INCREMENT_OPERATOR
	| DECREMENT_OPERATOR
	;

objeto :
	objetoAux
	;
	
objetoAux:
	THIS DOT ID
	| ID DOT ID
	| ID
	;

megaExpresion : 
	superExpresion megaExpresionAux
	;

megaExpresionAux :
	LOGICAL_AND_OPERATOR megaExpresion
	| LOGICAL_OR_OPERATOR megaExpresion
	|
	;

superExpresion :
	expresion superExpresionOperadores
	;

superExpresionOperadores :
	GREATER_THAN_OPERATOR expresion
	| GREATER_OR_EQUAL_THAN_OPERATOR expresion
	| LESS_THAN_OPERATOR expresion
	| LESS_THAN_OR_EQUAL_OPERATOR expresion
	| NOT_EQUAL_OPERATOR expresion
	| EQUAL_OPERATOR expresion
	|
	;

expresion :
	termino expresionOperadores
	;

expresionOperadores :
	SUM_OPERATOR termino
	| SUBSTRACTION_OPERATOR termino
	|
	;

termino :
	factor terminoOperadores
	;

terminoOperadores :
	MULTIPLICATION_OPERATOR termino
	| DIVISION_OPERATOR termino
	|
	;

factor :
	varCte
	| factorParentesis
	;

factorParentesis :
	LEFT_PARENTHESIS megaExpresion RIGHT_PARENTHESIS
	;

varCte :
	objeto
	| TYPE_INT
	| TYPE_FLOAT
	| TYPE_STRING
	| TYPE_CHAR
	| TYPE_BOOL
	| ID LEFT_SQUARE_BRACKET TYPE_INT RIGHT_SQUARE_BRACKET matrix
	;

matrix :
	LEFT_SQUARE_BRACKET TYPE_INT RIGHT_SQUARE_BRACKET
	|
	;