# Generated from Objective_JS.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\3\3\2/\62\2\5\2\4\3\2")
        buf.write("\2\2\4\5\t\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class Objective_JSParser ( Parser ):

    grammarFileName = "Objective_JS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elsif'", "'do'", "'times'", 
                     "'while'", "'++'", "'--'", "'+'", "'*'", "'/'", "'%'", 
                     "'^'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'&&'", "'||'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'.'", "':'", "';'", "'print'", "'this'", "'Class'", 
                     "'Inherits'", "'Attributes'", "'Public'", "'Private'", 
                     "'Protected'", "'METHODS'", "'function'", "'returns'", 
                     "'import'", "'main'", "'list'", "'read'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'float'", 
                     "'char'", "'string'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE_IF", "DO", "TIMES", "WHILE", 
                      "INCREMENT_OPERATOR", "DECREMENT_OPERATOR", "SUM_OPERATOR", 
                      "SUBSTRACTION_OPERATOR", "DIVISION_OPERATOR", "MODULUS_OPERATOR", 
                      "POWER_OPERATOR", "EQUAL_OPERATOR", "NOT_EQUAL_OPERATOR", 
                      "GREATER_THAN_OPERATOR", "GREATER_OR_EQUAL_THAN_OPERATOR", 
                      "LESS_THAN_OPERATOR", "LESS_THAN_OR_EQUAL_OPERATOR", 
                      "LOGICAL_AND_OPERATOR", "LOGICAL_OR_OPERATOR", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "DOT", 
                      "COLON", "SEMICOLON", "PRINT", "THIS", "CLASS", "INHERITS", 
                      "ATTRIBUTES", "PUBLIC", "PRIVATE", "PROTECTED", "METHODS", 
                      "FUNCTION", "RETURNS", "IMPORT", "MAIN", "LIST", "READ", 
                      "TYPE_INT", "TYPE_FLOAT", "TYPE_CHAR", "TYPE_STRING", 
                      "INT", "FLOAT", "CHAR", "STRING", "SINGLE_QUOTES", 
                      "CLASSNAME", "ID", "WHITESPACE" ]

    RULE_tipo = 0

    ruleNames =  [ "tipo" ]

    EOF = Token.EOF
    IF=1
    ELSE_IF=2
    DO=3
    TIMES=4
    WHILE=5
    INCREMENT_OPERATOR=6
    DECREMENT_OPERATOR=7
    SUM_OPERATOR=8
    SUBSTRACTION_OPERATOR=9
    DIVISION_OPERATOR=10
    MODULUS_OPERATOR=11
    POWER_OPERATOR=12
    EQUAL_OPERATOR=13
    NOT_EQUAL_OPERATOR=14
    GREATER_THAN_OPERATOR=15
    GREATER_OR_EQUAL_THAN_OPERATOR=16
    LESS_THAN_OPERATOR=17
    LESS_THAN_OR_EQUAL_OPERATOR=18
    LOGICAL_AND_OPERATOR=19
    LOGICAL_OR_OPERATOR=20
    LEFT_PARENTHESIS=21
    RIGHT_PARENTHESIS=22
    LEFT_SQUARE_BRACKET=23
    RIGHT_SQUARE_BRACKET=24
    LEFT_CURLY_BRACKET=25
    RIGHT_CURLY_BRACKET=26
    DOT=27
    COLON=28
    SEMICOLON=29
    PRINT=30
    THIS=31
    CLASS=32
    INHERITS=33
    ATTRIBUTES=34
    PUBLIC=35
    PRIVATE=36
    PROTECTED=37
    METHODS=38
    FUNCTION=39
    RETURNS=40
    IMPORT=41
    MAIN=42
    LIST=43
    READ=44
    TYPE_INT=45
    TYPE_FLOAT=46
    TYPE_CHAR=47
    TYPE_STRING=48
    INT=49
    FLOAT=50
    CHAR=51
    STRING=52
    SINGLE_QUOTES=53
    CLASSNAME=54
    ID=55
    WHITESPACE=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(Objective_JSParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(Objective_JSParser.TYPE_FLOAT, 0)

        def TYPE_CHAR(self):
            return self.getToken(Objective_JSParser.TYPE_CHAR, 0)

        def TYPE_STRING(self):
            return self.getToken(Objective_JSParser.TYPE_STRING, 0)

        def getRuleIndex(self):
            return Objective_JSParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = Objective_JSParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Objective_JSParser.TYPE_INT) | (1 << Objective_JSParser.TYPE_FLOAT) | (1 << Objective_JSParser.TYPE_CHAR) | (1 << Objective_JSParser.TYPE_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





