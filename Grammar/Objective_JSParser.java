// Generated from Objective_JS.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Objective_JSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, ELSE_IF=3, DO=4, TIMES=5, WHILE=6, INCREMENT_OPERATOR=7, 
		DECREMENT_OPERATOR=8, SUM_OPERATOR=9, SUBSTRACTION_OPERATOR=10, MULTIPLICATION_OPERATOR=11, 
		DIVISION_OPERATOR=12, MODULUS_OPERATOR=13, POWER_OPERATOR=14, EQUAL_OPERATOR=15, 
		ASSIGNMENT=16, NOT_EQUAL_OPERATOR=17, GREATER_THAN_OPERATOR=18, GREATER_OR_EQUAL_THAN_OPERATOR=19, 
		LESS_THAN_OPERATOR=20, LESS_THAN_OR_EQUAL_OPERATOR=21, LOGICAL_AND_OPERATOR=22, 
		LOGICAL_OR_OPERATOR=23, LEFT_PARENTHESIS=24, RIGHT_PARENTHESIS=25, LEFT_SQUARE_BRACKET=26, 
		RIGHT_SQUARE_BRACKET=27, LEFT_CURLY_BRACKET=28, RIGHT_CURLY_BRACKET=29, 
		DOT=30, COLON=31, SEMICOLON=32, COMMA=33, INPUT_STREAM=34, PRINT=35, THIS=36, 
		CLASS=37, INHERITS=38, ATTRIBUTES=39, PUBLIC=40, PRIVATE=41, PROTECTED=42, 
		METHODS=43, FUNCTION=44, RETURNS=45, RETURN=46, IMPORT=47, MAIN=48, LIST=49, 
		READ=50, VAR=51, TYPE_INT=52, TYPE_FLOAT=53, TYPE_CHAR=54, TYPE_STRING=55, 
		TYPE_BOOL=56, INT=57, FLOAT=58, CHAR=59, STRING=60, SINGLE_QUOTES=61, 
		CLASSNAME=62, ID=63, WHITESPACE=64;
	public static final int
		RULE_inicio = 0, RULE_main = 1, RULE_clase = 2, RULE_imports = 3, RULE_class_declaration = 4, 
		RULE_bloque = 5, RULE_preEstatuto = 6, RULE_claseAux = 7, RULE_bloqueClase = 8, 
		RULE_constructor = 9, RULE_constructorAux = 10, RULE_constructorAux2 = 11, 
		RULE_atributos = 12, RULE_atributosPublic = 13, RULE_atributosPublicAux = 14, 
		RULE_atributosPrivate = 15, RULE_atributosPrivateAux = 16, RULE_atributosProtected = 17, 
		RULE_metodos = 18, RULE_metodosPublicos = 19, RULE_metodosPublicosAux = 20, 
		RULE_metodosPrivados = 21, RULE_metodosPrivadosAux = 22, RULE_func = 23, 
		RULE_funcAux = 24, RULE_impConstructores = 25, RULE_impConstructoresMultiples = 26, 
		RULE_impConstructor = 27, RULE_impFunc = 28, RULE_impFuncAux2 = 29, RULE_argumentos = 30, 
		RULE_argumentosAux = 31, RULE_bloqueConstructor = 32, RULE_bloqueFunc = 33, 
		RULE_bloqueFuncAux = 34, RULE_bloqueFuncAux2 = 35, RULE_preVars = 36, 
		RULE_vars_ = 37, RULE_varsAux = 38, RULE_varsRepeated = 39, RULE_tipo_dato = 40, 
		RULE_tipo_dato_list = 41, RULE_dim = 42, RULE_dimMatrix = 43, RULE_tipo_dato_no_list = 44, 
		RULE_tipo = 45, RULE_estatuto = 46, RULE_asignacion = 47, RULE_condicion = 48, 
		RULE_condicionAux = 49, RULE_condicionChoice = 50, RULE_escritura = 51, 
		RULE_escrituraAux = 52, RULE_ciclos = 53, RULE_doAux = 54, RULE_llamadaFunc = 55, 
		RULE_argumentosLlamada = 56, RULE_argumentosLlamadaAux = 57, RULE_lectura = 58, 
		RULE_lecturaAux = 59, RULE_objeto = 60, RULE_objetoAux = 61, RULE_megaExpresion = 62, 
		RULE_megaExpresionAux = 63, RULE_superExpresion = 64, RULE_superExpresionOperadores = 65, 
		RULE_expresion = 66, RULE_expresionOperadores = 67, RULE_termino = 68, 
		RULE_terminoOperadores = 69, RULE_factor = 70, RULE_factorParentesis = 71, 
		RULE_varCte = 72, RULE_matrix = 73;
	public static final String[] ruleNames = {
		"inicio", "main", "clase", "imports", "class_declaration", "bloque", "preEstatuto", 
		"claseAux", "bloqueClase", "constructor", "constructorAux", "constructorAux2", 
		"atributos", "atributosPublic", "atributosPublicAux", "atributosPrivate", 
		"atributosPrivateAux", "atributosProtected", "metodos", "metodosPublicos", 
		"metodosPublicosAux", "metodosPrivados", "metodosPrivadosAux", "func", 
		"funcAux", "impConstructores", "impConstructoresMultiples", "impConstructor", 
		"impFunc", "impFuncAux2", "argumentos", "argumentosAux", "bloqueConstructor", 
		"bloqueFunc", "bloqueFuncAux", "bloqueFuncAux2", "preVars", "vars_", "varsAux", 
		"varsRepeated", "tipo_dato", "tipo_dato_list", "dim", "dimMatrix", "tipo_dato_no_list", 
		"tipo", "estatuto", "asignacion", "condicion", "condicionAux", "condicionChoice", 
		"escritura", "escrituraAux", "ciclos", "doAux", "llamadaFunc", "argumentosLlamada", 
		"argumentosLlamadaAux", "lectura", "lecturaAux", "objeto", "objetoAux", 
		"megaExpresion", "megaExpresionAux", "superExpresion", "superExpresionOperadores", 
		"expresion", "expresionOperadores", "termino", "terminoOperadores", "factor", 
		"factorParentesis", "varCte", "matrix"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'if'", "'else'", "'elsif'", "'do'", "'times'", "'while'", "'++'", 
		"'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'=='", "'='", "'!='", 
		"'>'", "'>='", "'<'", "'<='", "'&&'", "'||'", "'('", "')'", "'['", "']'", 
		"'{'", "'}'", "'.'", "':'", "';'", "','", "'>>'", "'print'", "'this'", 
		"'Class'", "'Inherits'", "'Attributes'", "'public'", "'private'", "'protected'", 
		"'Methods'", "'function'", "'returns'", "'return'", "'import'", "'main'", 
		"'list'", "'read'", "'var'", null, null, null, null, null, "'int'", "'float'", 
		"'char'", "'string'", "'\"'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "IF", "ELSE", "ELSE_IF", "DO", "TIMES", "WHILE", "INCREMENT_OPERATOR", 
		"DECREMENT_OPERATOR", "SUM_OPERATOR", "SUBSTRACTION_OPERATOR", "MULTIPLICATION_OPERATOR", 
		"DIVISION_OPERATOR", "MODULUS_OPERATOR", "POWER_OPERATOR", "EQUAL_OPERATOR", 
		"ASSIGNMENT", "NOT_EQUAL_OPERATOR", "GREATER_THAN_OPERATOR", "GREATER_OR_EQUAL_THAN_OPERATOR", 
		"LESS_THAN_OPERATOR", "LESS_THAN_OR_EQUAL_OPERATOR", "LOGICAL_AND_OPERATOR", 
		"LOGICAL_OR_OPERATOR", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
		"RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "DOT", 
		"COLON", "SEMICOLON", "COMMA", "INPUT_STREAM", "PRINT", "THIS", "CLASS", 
		"INHERITS", "ATTRIBUTES", "PUBLIC", "PRIVATE", "PROTECTED", "METHODS", 
		"FUNCTION", "RETURNS", "RETURN", "IMPORT", "MAIN", "LIST", "READ", "VAR", 
		"TYPE_INT", "TYPE_FLOAT", "TYPE_CHAR", "TYPE_STRING", "TYPE_BOOL", "INT", 
		"FLOAT", "CHAR", "STRING", "SINGLE_QUOTES", "CLASSNAME", "ID", "WHITESPACE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Objective_JS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Objective_JSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class InicioContext extends ParserRuleContext {
		public ClaseContext clase() {
			return getRuleContext(ClaseContext.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public InicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicio; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterInicio(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitInicio(this);
		}
	}

	public final InicioContext inicio() throws RecognitionException {
		InicioContext _localctx = new InicioContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_inicio);
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				clase();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				main();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public ImportsContext imports() {
			return getRuleContext(ImportsContext.class,0);
		}
		public Class_declarationContext class_declaration() {
			return getRuleContext(Class_declarationContext.class,0);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMain(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMain(this);
		}
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			imports();
			setState(153);
			class_declaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClaseContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(Objective_JSParser.CLASS, 0); }
		public TerminalNode CLASSNAME() { return getToken(Objective_JSParser.CLASSNAME, 0); }
		public ClaseAuxContext claseAux() {
			return getRuleContext(ClaseAuxContext.class,0);
		}
		public BloqueClaseContext bloqueClase() {
			return getRuleContext(BloqueClaseContext.class,0);
		}
		public ClaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterClase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitClase(this);
		}
	}

	public final ClaseContext clase() throws RecognitionException {
		ClaseContext _localctx = new ClaseContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_clase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(CLASS);
			setState(156);
			match(CLASSNAME);
			setState(157);
			claseAux();
			setState(158);
			bloqueClase();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImportsContext extends ParserRuleContext {
		public TerminalNode IMPORT() { return getToken(Objective_JSParser.IMPORT, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public ImportsContext imports() {
			return getRuleContext(ImportsContext.class,0);
		}
		public ImportsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imports; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImports(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImports(this);
		}
	}

	public final ImportsContext imports() throws RecognitionException {
		ImportsContext _localctx = new ImportsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_imports);
		try {
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IMPORT:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				match(IMPORT);
				setState(161);
				match(ID);
				setState(162);
				imports();
				}
				break;
			case CLASS:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declarationContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(Objective_JSParser.CLASS, 0); }
		public TerminalNode CLASSNAME() { return getToken(Objective_JSParser.CLASSNAME, 0); }
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public PreVarsContext preVars() {
			return getRuleContext(PreVarsContext.class,0);
		}
		public ImpFuncContext impFunc() {
			return getRuleContext(ImpFuncContext.class,0);
		}
		public TerminalNode MAIN() { return getToken(Objective_JSParser.MAIN, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public Class_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterClass_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitClass_declaration(this);
		}
	}

	public final Class_declarationContext class_declaration() throws RecognitionException {
		Class_declarationContext _localctx = new Class_declarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_class_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(CLASS);
			setState(167);
			match(CLASSNAME);
			setState(168);
			match(LEFT_CURLY_BRACKET);
			setState(169);
			preVars();
			setState(170);
			impFunc();
			setState(171);
			match(MAIN);
			setState(172);
			match(LEFT_PARENTHESIS);
			setState(173);
			match(RIGHT_PARENTHESIS);
			setState(174);
			bloque();
			setState(175);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public PreEstatutoContext preEstatuto() {
			return getRuleContext(PreEstatutoContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(LEFT_CURLY_BRACKET);
			setState(178);
			preEstatuto();
			setState(179);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreEstatutoContext extends ParserRuleContext {
		public EstatutoContext estatuto() {
			return getRuleContext(EstatutoContext.class,0);
		}
		public PreEstatutoContext preEstatuto() {
			return getRuleContext(PreEstatutoContext.class,0);
		}
		public PreEstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preEstatuto; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterPreEstatuto(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitPreEstatuto(this);
		}
	}

	public final PreEstatutoContext preEstatuto() throws RecognitionException {
		PreEstatutoContext _localctx = new PreEstatutoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_preEstatuto);
		try {
			setState(185);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
			case DO:
			case PRINT:
			case THIS:
			case READ:
			case VAR:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(181);
				estatuto();
				setState(182);
				preEstatuto();
				}
				break;
			case RIGHT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClaseAuxContext extends ParserRuleContext {
		public TerminalNode INHERITS() { return getToken(Objective_JSParser.INHERITS, 0); }
		public TerminalNode CLASSNAME() { return getToken(Objective_JSParser.CLASSNAME, 0); }
		public ClaseAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_claseAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterClaseAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitClaseAux(this);
		}
	}

	public final ClaseAuxContext claseAux() throws RecognitionException {
		ClaseAuxContext _localctx = new ClaseAuxContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_claseAux);
		try {
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INHERITS:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				match(INHERITS);
				setState(188);
				match(CLASSNAME);
				}
				break;
			case LEFT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueClaseContext extends ParserRuleContext {
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public ConstructorContext constructor() {
			return getRuleContext(ConstructorContext.class,0);
		}
		public AtributosContext atributos() {
			return getRuleContext(AtributosContext.class,0);
		}
		public MetodosContext metodos() {
			return getRuleContext(MetodosContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public ImpConstructoresContext impConstructores() {
			return getRuleContext(ImpConstructoresContext.class,0);
		}
		public ImpFuncContext impFunc() {
			return getRuleContext(ImpFuncContext.class,0);
		}
		public BloqueClaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueClase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloqueClase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloqueClase(this);
		}
	}

	public final BloqueClaseContext bloqueClase() throws RecognitionException {
		BloqueClaseContext _localctx = new BloqueClaseContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_bloqueClase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(LEFT_CURLY_BRACKET);
			setState(193);
			constructor();
			setState(194);
			atributos();
			setState(195);
			metodos();
			setState(196);
			match(RIGHT_CURLY_BRACKET);
			setState(197);
			impConstructores();
			setState(198);
			impFunc();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstructorContext extends ParserRuleContext {
		public TerminalNode CLASSNAME() { return getToken(Objective_JSParser.CLASSNAME, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public ConstructorAuxContext constructorAux() {
			return getRuleContext(ConstructorAuxContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public ConstructorAux2Context constructorAux2() {
			return getRuleContext(ConstructorAux2Context.class,0);
		}
		public ConstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterConstructor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitConstructor(this);
		}
	}

	public final ConstructorContext constructor() throws RecognitionException {
		ConstructorContext _localctx = new ConstructorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constructor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(CLASSNAME);
			setState(201);
			match(LEFT_PARENTHESIS);
			setState(202);
			constructorAux();
			setState(203);
			match(RIGHT_PARENTHESIS);
			setState(204);
			match(SEMICOLON);
			setState(205);
			constructorAux2();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstructorAuxContext extends ParserRuleContext {
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public ConstructorAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructorAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterConstructorAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitConstructorAux(this);
		}
	}

	public final ConstructorAuxContext constructorAux() throws RecognitionException {
		ConstructorAuxContext _localctx = new ConstructorAuxContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_constructorAux);
		try {
			setState(209);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(207);
				argumentos();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstructorAux2Context extends ParserRuleContext {
		public ConstructorContext constructor() {
			return getRuleContext(ConstructorContext.class,0);
		}
		public ConstructorAux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructorAux2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterConstructorAux2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitConstructorAux2(this);
		}
	}

	public final ConstructorAux2Context constructorAux2() throws RecognitionException {
		ConstructorAux2Context _localctx = new ConstructorAux2Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_constructorAux2);
		try {
			setState(213);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASSNAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				constructor();
				}
				break;
			case ATTRIBUTES:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTES() { return getToken(Objective_JSParser.ATTRIBUTES, 0); }
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public AtributosPublicContext atributosPublic() {
			return getRuleContext(AtributosPublicContext.class,0);
		}
		public AtributosPrivateContext atributosPrivate() {
			return getRuleContext(AtributosPrivateContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public AtributosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributos(this);
		}
	}

	public final AtributosContext atributos() throws RecognitionException {
		AtributosContext _localctx = new AtributosContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_atributos);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(ATTRIBUTES);
			setState(216);
			match(LEFT_CURLY_BRACKET);
			setState(217);
			atributosPublic();
			setState(218);
			atributosPrivate();
			setState(219);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosPublicContext extends ParserRuleContext {
		public TerminalNode PUBLIC() { return getToken(Objective_JSParser.PUBLIC, 0); }
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public AtributosPublicAuxContext atributosPublicAux() {
			return getRuleContext(AtributosPublicAuxContext.class,0);
		}
		public AtributosPublicContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributosPublic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributosPublic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributosPublic(this);
		}
	}

	public final AtributosPublicContext atributosPublic() throws RecognitionException {
		AtributosPublicContext _localctx = new AtributosPublicContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_atributosPublic);
		try {
			setState(227);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PUBLIC:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				match(PUBLIC);
				setState(222);
				match(COLON);
				setState(223);
				vars_();
				setState(224);
				atributosPublicAux();
				}
				break;
			case RIGHT_CURLY_BRACKET:
			case PRIVATE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosPublicAuxContext extends ParserRuleContext {
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public AtributosPublicAuxContext atributosPublicAux() {
			return getRuleContext(AtributosPublicAuxContext.class,0);
		}
		public AtributosPublicAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributosPublicAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributosPublicAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributosPublicAux(this);
		}
	}

	public final AtributosPublicAuxContext atributosPublicAux() throws RecognitionException {
		AtributosPublicAuxContext _localctx = new AtributosPublicAuxContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_atributosPublicAux);
		try {
			setState(233);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(229);
				vars_();
				setState(230);
				atributosPublicAux();
				}
				break;
			case RIGHT_CURLY_BRACKET:
			case PRIVATE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosPrivateContext extends ParserRuleContext {
		public TerminalNode PRIVATE() { return getToken(Objective_JSParser.PRIVATE, 0); }
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public AtributosPrivateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributosPrivate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributosPrivate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributosPrivate(this);
		}
	}

	public final AtributosPrivateContext atributosPrivate() throws RecognitionException {
		AtributosPrivateContext _localctx = new AtributosPrivateContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_atributosPrivate);
		try {
			setState(239);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRIVATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(235);
				match(PRIVATE);
				setState(236);
				match(COLON);
				setState(237);
				vars_();
				}
				break;
			case RIGHT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosPrivateAuxContext extends ParserRuleContext {
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public AtributosPrivateAuxContext atributosPrivateAux() {
			return getRuleContext(AtributosPrivateAuxContext.class,0);
		}
		public AtributosPrivateAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributosPrivateAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributosPrivateAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributosPrivateAux(this);
		}
	}

	public final AtributosPrivateAuxContext atributosPrivateAux() throws RecognitionException {
		AtributosPrivateAuxContext _localctx = new AtributosPrivateAuxContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_atributosPrivateAux);
		try {
			setState(245);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(241);
				vars_();
				setState(242);
				atributosPrivateAux();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtributosProtectedContext extends ParserRuleContext {
		public TerminalNode PROTECTED() { return getToken(Objective_JSParser.PROTECTED, 0); }
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public AtributosProtectedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributosProtected; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAtributosProtected(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAtributosProtected(this);
		}
	}

	public final AtributosProtectedContext atributosProtected() throws RecognitionException {
		AtributosProtectedContext _localctx = new AtributosProtectedContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_atributosProtected);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PROTECTED:
				enterOuterAlt(_localctx, 1);
				{
				setState(247);
				match(PROTECTED);
				setState(248);
				match(COLON);
				setState(249);
				vars_();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MetodosContext extends ParserRuleContext {
		public TerminalNode METHODS() { return getToken(Objective_JSParser.METHODS, 0); }
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public MetodosPublicosContext metodosPublicos() {
			return getRuleContext(MetodosPublicosContext.class,0);
		}
		public MetodosPrivadosContext metodosPrivados() {
			return getRuleContext(MetodosPrivadosContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public MetodosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMetodos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMetodos(this);
		}
	}

	public final MetodosContext metodos() throws RecognitionException {
		MetodosContext _localctx = new MetodosContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_metodos);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(METHODS);
			setState(254);
			match(LEFT_CURLY_BRACKET);
			setState(255);
			metodosPublicos();
			setState(256);
			metodosPrivados();
			setState(257);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MetodosPublicosContext extends ParserRuleContext {
		public TerminalNode PUBLIC() { return getToken(Objective_JSParser.PUBLIC, 0); }
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public MetodosPublicosAuxContext metodosPublicosAux() {
			return getRuleContext(MetodosPublicosAuxContext.class,0);
		}
		public MetodosPublicosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodosPublicos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMetodosPublicos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMetodosPublicos(this);
		}
	}

	public final MetodosPublicosContext metodosPublicos() throws RecognitionException {
		MetodosPublicosContext _localctx = new MetodosPublicosContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_metodosPublicos);
		try {
			setState(267);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(259);
				match(PUBLIC);
				setState(260);
				match(COLON);
				setState(261);
				func();
				setState(262);
				match(SEMICOLON);
				setState(263);
				metodosPublicosAux();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(265);
				match(PUBLIC);
				setState(266);
				match(COLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MetodosPublicosAuxContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public MetodosPublicosAuxContext metodosPublicosAux() {
			return getRuleContext(MetodosPublicosAuxContext.class,0);
		}
		public MetodosPublicosAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodosPublicosAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMetodosPublicosAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMetodosPublicosAux(this);
		}
	}

	public final MetodosPublicosAuxContext metodosPublicosAux() throws RecognitionException {
		MetodosPublicosAuxContext _localctx = new MetodosPublicosAuxContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_metodosPublicosAux);
		try {
			setState(274);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNCTION:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				func();
				setState(270);
				match(SEMICOLON);
				setState(271);
				metodosPublicosAux();
				}
				break;
			case PRIVATE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MetodosPrivadosContext extends ParserRuleContext {
		public TerminalNode PRIVATE() { return getToken(Objective_JSParser.PRIVATE, 0); }
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public MetodosPrivadosAuxContext metodosPrivadosAux() {
			return getRuleContext(MetodosPrivadosAuxContext.class,0);
		}
		public MetodosPrivadosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodosPrivados; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMetodosPrivados(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMetodosPrivados(this);
		}
	}

	public final MetodosPrivadosContext metodosPrivados() throws RecognitionException {
		MetodosPrivadosContext _localctx = new MetodosPrivadosContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_metodosPrivados);
		try {
			setState(284);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(276);
				match(PRIVATE);
				setState(277);
				match(COLON);
				setState(278);
				func();
				setState(279);
				match(SEMICOLON);
				setState(280);
				metodosPrivadosAux();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(282);
				match(PRIVATE);
				setState(283);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MetodosPrivadosAuxContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public MetodosPrivadosAuxContext metodosPrivadosAux() {
			return getRuleContext(MetodosPrivadosAuxContext.class,0);
		}
		public MetodosPrivadosAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodosPrivadosAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMetodosPrivadosAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMetodosPrivadosAux(this);
		}
	}

	public final MetodosPrivadosAuxContext metodosPrivadosAux() throws RecognitionException {
		MetodosPrivadosAuxContext _localctx = new MetodosPrivadosAuxContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_metodosPrivadosAux);
		try {
			setState(291);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNCTION:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				func();
				setState(287);
				match(SEMICOLON);
				setState(288);
				metodosPrivadosAux();
				}
				break;
			case RIGHT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(Objective_JSParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public FuncAuxContext funcAux() {
			return getRuleContext(FuncAuxContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitFunc(this);
		}
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			match(FUNCTION);
			setState(294);
			match(ID);
			setState(295);
			match(LEFT_PARENTHESIS);
			setState(296);
			argumentos();
			setState(297);
			match(RIGHT_PARENTHESIS);
			setState(298);
			funcAux();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncAuxContext extends ParserRuleContext {
		public TerminalNode RETURNS() { return getToken(Objective_JSParser.RETURNS, 0); }
		public FuncAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterFuncAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitFuncAux(this);
		}
	}

	public final FuncAuxContext funcAux() throws RecognitionException {
		FuncAuxContext _localctx = new FuncAuxContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_funcAux);
		try {
			setState(302);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURNS:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				match(RETURNS);
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImpConstructoresContext extends ParserRuleContext {
		public ImpConstructorContext impConstructor() {
			return getRuleContext(ImpConstructorContext.class,0);
		}
		public ImpConstructoresMultiplesContext impConstructoresMultiples() {
			return getRuleContext(ImpConstructoresMultiplesContext.class,0);
		}
		public ImpConstructoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impConstructores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImpConstructores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImpConstructores(this);
		}
	}

	public final ImpConstructoresContext impConstructores() throws RecognitionException {
		ImpConstructoresContext _localctx = new ImpConstructoresContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_impConstructores);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			impConstructor();
			setState(305);
			impConstructoresMultiples();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImpConstructoresMultiplesContext extends ParserRuleContext {
		public ImpConstructorContext impConstructor() {
			return getRuleContext(ImpConstructorContext.class,0);
		}
		public ImpConstructoresMultiplesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impConstructoresMultiples; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImpConstructoresMultiples(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImpConstructoresMultiples(this);
		}
	}

	public final ImpConstructoresMultiplesContext impConstructoresMultiples() throws RecognitionException {
		ImpConstructoresMultiplesContext _localctx = new ImpConstructoresMultiplesContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_impConstructoresMultiples);
		try {
			setState(309);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASSNAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(307);
				impConstructor();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImpConstructorContext extends ParserRuleContext {
		public TerminalNode CLASSNAME() { return getToken(Objective_JSParser.CLASSNAME, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public BloqueConstructorContext bloqueConstructor() {
			return getRuleContext(BloqueConstructorContext.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public ImpConstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impConstructor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImpConstructor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImpConstructor(this);
		}
	}

	public final ImpConstructorContext impConstructor() throws RecognitionException {
		ImpConstructorContext _localctx = new ImpConstructorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_impConstructor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			match(CLASSNAME);
			setState(312);
			match(LEFT_PARENTHESIS);
			setState(313);
			argumentos();
			setState(314);
			match(RIGHT_PARENTHESIS);
			setState(315);
			match(LEFT_CURLY_BRACKET);
			setState(316);
			bloqueConstructor();
			setState(317);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImpFuncContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(Objective_JSParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public ImpFuncAux2Context impFuncAux2() {
			return getRuleContext(ImpFuncAux2Context.class,0);
		}
		public BloqueFuncContext bloqueFunc() {
			return getRuleContext(BloqueFuncContext.class,0);
		}
		public ImpFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImpFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImpFunc(this);
		}
	}

	public final ImpFuncContext impFunc() throws RecognitionException {
		ImpFuncContext _localctx = new ImpFuncContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_impFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(FUNCTION);
			setState(320);
			match(ID);
			setState(321);
			match(LEFT_PARENTHESIS);
			setState(322);
			argumentos();
			setState(323);
			match(RIGHT_PARENTHESIS);
			setState(324);
			impFuncAux2();
			setState(325);
			bloqueFunc();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImpFuncAux2Context extends ParserRuleContext {
		public TerminalNode RETURNS() { return getToken(Objective_JSParser.RETURNS, 0); }
		public ImpFuncAux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impFuncAux2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterImpFuncAux2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitImpFuncAux2(this);
		}
	}

	public final ImpFuncAux2Context impFuncAux2() throws RecognitionException {
		ImpFuncAux2Context _localctx = new ImpFuncAux2Context(_ctx, getState());
		enterRule(_localctx, 58, RULE_impFuncAux2);
		try {
			setState(329);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURNS:
				enterOuterAlt(_localctx, 1);
				{
				setState(327);
				match(RETURNS);
				}
				break;
			case LEFT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentosContext extends ParserRuleContext {
		public Tipo_datoContext tipo_dato() {
			return getRuleContext(Tipo_datoContext.class,0);
		}
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public ArgumentosAuxContext argumentosAux() {
			return getRuleContext(ArgumentosAuxContext.class,0);
		}
		public ArgumentosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterArgumentos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitArgumentos(this);
		}
	}

	public final ArgumentosContext argumentos() throws RecognitionException {
		ArgumentosContext _localctx = new ArgumentosContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_argumentos);
		try {
			setState(336);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LIST:
			case INT:
			case FLOAT:
			case CHAR:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(331);
				tipo_dato();
				setState(332);
				match(ID);
				setState(333);
				argumentosAux();
				}
				break;
			case RIGHT_PARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentosAuxContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(Objective_JSParser.COMMA, 0); }
		public Tipo_datoContext tipo_dato() {
			return getRuleContext(Tipo_datoContext.class,0);
		}
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public ArgumentosAuxContext argumentosAux() {
			return getRuleContext(ArgumentosAuxContext.class,0);
		}
		public ArgumentosAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentosAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterArgumentosAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitArgumentosAux(this);
		}
	}

	public final ArgumentosAuxContext argumentosAux() throws RecognitionException {
		ArgumentosAuxContext _localctx = new ArgumentosAuxContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_argumentosAux);
		try {
			setState(344);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				match(COMMA);
				setState(339);
				tipo_dato();
				setState(340);
				match(ID);
				setState(341);
				argumentosAux();
				}
				break;
			case RIGHT_PARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueConstructorContext extends ParserRuleContext {
		public BloqueConstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueConstructor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloqueConstructor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloqueConstructor(this);
		}
	}

	public final BloqueConstructorContext bloqueConstructor() throws RecognitionException {
		BloqueConstructorContext _localctx = new BloqueConstructorContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_bloqueConstructor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueFuncContext extends ParserRuleContext {
		public TerminalNode LEFT_CURLY_BRACKET() { return getToken(Objective_JSParser.LEFT_CURLY_BRACKET, 0); }
		public BloqueFuncAuxContext bloqueFuncAux() {
			return getRuleContext(BloqueFuncAuxContext.class,0);
		}
		public BloqueFuncAux2Context bloqueFuncAux2() {
			return getRuleContext(BloqueFuncAux2Context.class,0);
		}
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public BloqueFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloqueFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloqueFunc(this);
		}
	}

	public final BloqueFuncContext bloqueFunc() throws RecognitionException {
		BloqueFuncContext _localctx = new BloqueFuncContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_bloqueFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(LEFT_CURLY_BRACKET);
			setState(349);
			bloqueFuncAux();
			setState(350);
			bloqueFuncAux2();
			setState(351);
			match(RIGHT_CURLY_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueFuncAuxContext extends ParserRuleContext {
		public EstatutoContext estatuto() {
			return getRuleContext(EstatutoContext.class,0);
		}
		public BloqueFuncAuxContext bloqueFuncAux() {
			return getRuleContext(BloqueFuncAuxContext.class,0);
		}
		public BloqueFuncAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueFuncAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloqueFuncAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloqueFuncAux(this);
		}
	}

	public final BloqueFuncAuxContext bloqueFuncAux() throws RecognitionException {
		BloqueFuncAuxContext _localctx = new BloqueFuncAuxContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_bloqueFuncAux);
		try {
			setState(357);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
			case DO:
			case PRINT:
			case THIS:
			case READ:
			case VAR:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(353);
				estatuto();
				setState(354);
				bloqueFuncAux();
				}
				break;
			case RIGHT_CURLY_BRACKET:
			case RETURN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueFuncAux2Context extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(Objective_JSParser.RETURN, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public BloqueFuncAux2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloqueFuncAux2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterBloqueFuncAux2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitBloqueFuncAux2(this);
		}
	}

	public final BloqueFuncAux2Context bloqueFuncAux2() throws RecognitionException {
		BloqueFuncAux2Context _localctx = new BloqueFuncAux2Context(_ctx, getState());
		enterRule(_localctx, 70, RULE_bloqueFuncAux2);
		try {
			setState(364);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
				enterOuterAlt(_localctx, 1);
				{
				setState(359);
				match(RETURN);
				setState(360);
				megaExpresion();
				setState(361);
				match(SEMICOLON);
				}
				break;
			case RIGHT_CURLY_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreVarsContext extends ParserRuleContext {
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public PreVarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preVars; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterPreVars(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitPreVars(this);
		}
	}

	public final PreVarsContext preVars() throws RecognitionException {
		PreVarsContext _localctx = new PreVarsContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_preVars);
		try {
			setState(368);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(366);
				vars_();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vars_Context extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(Objective_JSParser.VAR, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public VarsAuxContext varsAux() {
			return getRuleContext(VarsAuxContext.class,0);
		}
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public Tipo_datoContext tipo_dato() {
			return getRuleContext(Tipo_datoContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public VarsRepeatedContext varsRepeated() {
			return getRuleContext(VarsRepeatedContext.class,0);
		}
		public Vars_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterVars_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitVars_(this);
		}
	}

	public final Vars_Context vars_() throws RecognitionException {
		Vars_Context _localctx = new Vars_Context(_ctx, getState());
		enterRule(_localctx, 74, RULE_vars_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(VAR);
			setState(371);
			match(ID);
			setState(372);
			varsAux();
			setState(373);
			match(COLON);
			setState(374);
			tipo_dato();
			setState(375);
			match(SEMICOLON);
			setState(376);
			varsRepeated();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarsAuxContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(Objective_JSParser.COMMA, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public VarsAuxContext varsAux() {
			return getRuleContext(VarsAuxContext.class,0);
		}
		public VarsAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varsAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterVarsAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitVarsAux(this);
		}
	}

	public final VarsAuxContext varsAux() throws RecognitionException {
		VarsAuxContext _localctx = new VarsAuxContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_varsAux);
		try {
			setState(382);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(378);
				match(COMMA);
				setState(379);
				match(ID);
				setState(380);
				varsAux();
				}
				break;
			case COLON:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarsRepeatedContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(Objective_JSParser.VAR, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public VarsAuxContext varsAux() {
			return getRuleContext(VarsAuxContext.class,0);
		}
		public TerminalNode COLON() { return getToken(Objective_JSParser.COLON, 0); }
		public Tipo_datoContext tipo_dato() {
			return getRuleContext(Tipo_datoContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public VarsRepeatedContext varsRepeated() {
			return getRuleContext(VarsRepeatedContext.class,0);
		}
		public VarsRepeatedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varsRepeated; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterVarsRepeated(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitVarsRepeated(this);
		}
	}

	public final VarsRepeatedContext varsRepeated() throws RecognitionException {
		VarsRepeatedContext _localctx = new VarsRepeatedContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_varsRepeated);
		try {
			setState(393);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(384);
				match(VAR);
				setState(385);
				match(ID);
				setState(386);
				varsAux();
				setState(387);
				match(COLON);
				setState(388);
				tipo_dato();
				setState(389);
				match(SEMICOLON);
				setState(390);
				varsRepeated();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tipo_datoContext extends ParserRuleContext {
		public Tipo_dato_listContext tipo_dato_list() {
			return getRuleContext(Tipo_dato_listContext.class,0);
		}
		public Tipo_dato_no_listContext tipo_dato_no_list() {
			return getRuleContext(Tipo_dato_no_listContext.class,0);
		}
		public Tipo_datoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo_dato; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTipo_dato(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTipo_dato(this);
		}
	}

	public final Tipo_datoContext tipo_dato() throws RecognitionException {
		Tipo_datoContext _localctx = new Tipo_datoContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_tipo_dato);
		try {
			setState(399);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LIST:
				enterOuterAlt(_localctx, 1);
				{
				setState(395);
				tipo_dato_list();
				setState(396);
				tipo_dato_no_list();
				}
				break;
			case INT:
			case FLOAT:
			case CHAR:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(398);
				tipo_dato_no_list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tipo_dato_listContext extends ParserRuleContext {
		public TerminalNode LIST() { return getToken(Objective_JSParser.LIST, 0); }
		public DimContext dim() {
			return getRuleContext(DimContext.class,0);
		}
		public Tipo_dato_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo_dato_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTipo_dato_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTipo_dato_list(this);
		}
	}

	public final Tipo_dato_listContext tipo_dato_list() throws RecognitionException {
		Tipo_dato_listContext _localctx = new Tipo_dato_listContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_tipo_dato_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(LIST);
			setState(402);
			dim();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DimContext extends ParserRuleContext {
		public TerminalNode LEFT_SQUARE_BRACKET() { return getToken(Objective_JSParser.LEFT_SQUARE_BRACKET, 0); }
		public TerminalNode TYPE_INT() { return getToken(Objective_JSParser.TYPE_INT, 0); }
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public DimMatrixContext dimMatrix() {
			return getRuleContext(DimMatrixContext.class,0);
		}
		public DimContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dim; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterDim(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitDim(this);
		}
	}

	public final DimContext dim() throws RecognitionException {
		DimContext _localctx = new DimContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_dim);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(404);
			match(LEFT_SQUARE_BRACKET);
			setState(405);
			match(TYPE_INT);
			setState(406);
			match(RIGHT_CURLY_BRACKET);
			setState(407);
			dimMatrix();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DimMatrixContext extends ParserRuleContext {
		public TerminalNode LEFT_SQUARE_BRACKET() { return getToken(Objective_JSParser.LEFT_SQUARE_BRACKET, 0); }
		public TerminalNode TYPE_INT() { return getToken(Objective_JSParser.TYPE_INT, 0); }
		public TerminalNode RIGHT_CURLY_BRACKET() { return getToken(Objective_JSParser.RIGHT_CURLY_BRACKET, 0); }
		public DimMatrixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimMatrix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterDimMatrix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitDimMatrix(this);
		}
	}

	public final DimMatrixContext dimMatrix() throws RecognitionException {
		DimMatrixContext _localctx = new DimMatrixContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_dimMatrix);
		try {
			setState(413);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_SQUARE_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(409);
				match(LEFT_SQUARE_BRACKET);
				setState(410);
				match(TYPE_INT);
				setState(411);
				match(RIGHT_CURLY_BRACKET);
				}
				break;
			case INT:
			case FLOAT:
			case CHAR:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tipo_dato_no_listContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(Objective_JSParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(Objective_JSParser.FLOAT, 0); }
		public TerminalNode CHAR() { return getToken(Objective_JSParser.CHAR, 0); }
		public TerminalNode STRING() { return getToken(Objective_JSParser.STRING, 0); }
		public Tipo_dato_no_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo_dato_no_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTipo_dato_no_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTipo_dato_no_list(this);
		}
	}

	public final Tipo_dato_no_listContext tipo_dato_no_list() throws RecognitionException {
		Tipo_dato_no_listContext _localctx = new Tipo_dato_no_listContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_tipo_dato_no_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << CHAR) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode TYPE_INT() { return getToken(Objective_JSParser.TYPE_INT, 0); }
		public TerminalNode TYPE_FLOAT() { return getToken(Objective_JSParser.TYPE_FLOAT, 0); }
		public TerminalNode TYPE_CHAR() { return getToken(Objective_JSParser.TYPE_CHAR, 0); }
		public TerminalNode TYPE_STRING() { return getToken(Objective_JSParser.TYPE_STRING, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(417);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TYPE_INT) | (1L << TYPE_FLOAT) | (1L << TYPE_CHAR) | (1L << TYPE_STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EstatutoContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public EscrituraContext escritura() {
			return getRuleContext(EscrituraContext.class,0);
		}
		public CiclosContext ciclos() {
			return getRuleContext(CiclosContext.class,0);
		}
		public Vars_Context vars_() {
			return getRuleContext(Vars_Context.class,0);
		}
		public LlamadaFuncContext llamadaFunc() {
			return getRuleContext(LlamadaFuncContext.class,0);
		}
		public LecturaContext lectura() {
			return getRuleContext(LecturaContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterEstatuto(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitEstatuto(this);
		}
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_estatuto);
		try {
			setState(426);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(419);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(420);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(421);
				escritura();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(422);
				ciclos();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(423);
				vars_();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(424);
				llamadaFunc();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(425);
				lectura();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AsignacionContext extends ParserRuleContext {
		public ObjetoContext objeto() {
			return getRuleContext(ObjetoContext.class,0);
		}
		public TerminalNode ASSIGNMENT() { return getToken(Objective_JSParser.ASSIGNMENT, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			objeto();
			setState(429);
			match(ASSIGNMENT);
			setState(430);
			megaExpresion();
			setState(431);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(Objective_JSParser.IF, 0); }
		public CondicionAuxContext condicionAux() {
			return getRuleContext(CondicionAuxContext.class,0);
		}
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterCondicion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitCondicion(this);
		}
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(433);
			match(IF);
			setState(434);
			condicionAux();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicionAuxContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public CondicionChoiceContext condicionChoice() {
			return getRuleContext(CondicionChoiceContext.class,0);
		}
		public CondicionAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicionAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterCondicionAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitCondicionAux(this);
		}
	}

	public final CondicionAuxContext condicionAux() throws RecognitionException {
		CondicionAuxContext _localctx = new CondicionAuxContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_condicionAux);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(436);
			match(LEFT_PARENTHESIS);
			setState(437);
			megaExpresion();
			setState(438);
			match(RIGHT_PARENTHESIS);
			setState(439);
			bloque();
			setState(440);
			condicionChoice();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicionChoiceContext extends ParserRuleContext {
		public TerminalNode ELSE_IF() { return getToken(Objective_JSParser.ELSE_IF, 0); }
		public CondicionAuxContext condicionAux() {
			return getRuleContext(CondicionAuxContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(Objective_JSParser.ELSE, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public CondicionChoiceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicionChoice; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterCondicionChoice(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitCondicionChoice(this);
		}
	}

	public final CondicionChoiceContext condicionChoice() throws RecognitionException {
		CondicionChoiceContext _localctx = new CondicionChoiceContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_condicionChoice);
		try {
			setState(447);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ELSE_IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(442);
				match(ELSE_IF);
				setState(443);
				condicionAux();
				}
				break;
			case ELSE:
				enterOuterAlt(_localctx, 2);
				{
				setState(444);
				match(ELSE);
				setState(445);
				bloque();
				}
				break;
			case IF:
			case DO:
			case RIGHT_CURLY_BRACKET:
			case PRINT:
			case THIS:
			case RETURN:
			case READ:
			case VAR:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EscrituraContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(Objective_JSParser.PRINT, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public EscrituraAuxContext escrituraAux() {
			return getRuleContext(EscrituraAuxContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public EscrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escritura; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterEscritura(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitEscritura(this);
		}
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_escritura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(449);
			match(PRINT);
			setState(450);
			match(LEFT_PARENTHESIS);
			setState(451);
			megaExpresion();
			setState(452);
			escrituraAux();
			setState(453);
			match(RIGHT_PARENTHESIS);
			setState(454);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EscrituraAuxContext extends ParserRuleContext {
		public TerminalNode SUM_OPERATOR() { return getToken(Objective_JSParser.SUM_OPERATOR, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public EscrituraAuxContext escrituraAux() {
			return getRuleContext(EscrituraAuxContext.class,0);
		}
		public EscrituraAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escrituraAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterEscrituraAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitEscrituraAux(this);
		}
	}

	public final EscrituraAuxContext escrituraAux() throws RecognitionException {
		EscrituraAuxContext _localctx = new EscrituraAuxContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_escrituraAux);
		try {
			setState(461);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUM_OPERATOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(456);
				match(SUM_OPERATOR);
				setState(457);
				megaExpresion();
				setState(458);
				escrituraAux();
				}
				break;
			case RIGHT_PARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CiclosContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(Objective_JSParser.DO, 0); }
		public DoAuxContext doAux() {
			return getRuleContext(DoAuxContext.class,0);
		}
		public TerminalNode TIMES() { return getToken(Objective_JSParser.TIMES, 0); }
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode WHILE() { return getToken(Objective_JSParser.WHILE, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public CiclosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterCiclos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitCiclos(this);
		}
	}

	public final CiclosContext ciclos() throws RecognitionException {
		CiclosContext _localctx = new CiclosContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_ciclos);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(463);
			match(DO);
			setState(464);
			doAux();
			setState(465);
			match(TIMES);
			setState(466);
			bloque();
			setState(467);
			match(WHILE);
			setState(468);
			match(LEFT_PARENTHESIS);
			setState(469);
			megaExpresion();
			setState(470);
			match(RIGHT_PARENTHESIS);
			setState(471);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DoAuxContext extends ParserRuleContext {
		public ObjetoContext objeto() {
			return getRuleContext(ObjetoContext.class,0);
		}
		public TerminalNode TYPE_INT() { return getToken(Objective_JSParser.TYPE_INT, 0); }
		public DoAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterDoAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitDoAux(this);
		}
	}

	public final DoAuxContext doAux() throws RecognitionException {
		DoAuxContext _localctx = new DoAuxContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_doAux);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			objeto();
			setState(474);
			match(TYPE_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LlamadaFuncContext extends ParserRuleContext {
		public ObjetoContext objeto() {
			return getRuleContext(ObjetoContext.class,0);
		}
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public ArgumentosLlamadaContext argumentosLlamada() {
			return getRuleContext(ArgumentosLlamadaContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public LlamadaFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamadaFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterLlamadaFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitLlamadaFunc(this);
		}
	}

	public final LlamadaFuncContext llamadaFunc() throws RecognitionException {
		LlamadaFuncContext _localctx = new LlamadaFuncContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_llamadaFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(476);
			objeto();
			setState(477);
			match(LEFT_PARENTHESIS);
			setState(478);
			argumentosLlamada();
			setState(479);
			match(RIGHT_PARENTHESIS);
			setState(480);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentosLlamadaContext extends ParserRuleContext {
		public ObjetoContext objeto() {
			return getRuleContext(ObjetoContext.class,0);
		}
		public List<ArgumentosLlamadaAuxContext> argumentosLlamadaAux() {
			return getRuleContexts(ArgumentosLlamadaAuxContext.class);
		}
		public ArgumentosLlamadaAuxContext argumentosLlamadaAux(int i) {
			return getRuleContext(ArgumentosLlamadaAuxContext.class,i);
		}
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public ArgumentosLlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentosLlamada; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterArgumentosLlamada(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitArgumentosLlamada(this);
		}
	}

	public final ArgumentosLlamadaContext argumentosLlamada() throws RecognitionException {
		ArgumentosLlamadaContext _localctx = new ArgumentosLlamadaContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_argumentosLlamada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(482);
			objeto();
			setState(483);
			argumentosLlamadaAux();
			setState(484);
			megaExpresion();
			setState(485);
			argumentosLlamadaAux();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentosLlamadaAuxContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(Objective_JSParser.COMMA, 0); }
		public ArgumentosLlamadaContext argumentosLlamada() {
			return getRuleContext(ArgumentosLlamadaContext.class,0);
		}
		public ArgumentosLlamadaAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentosLlamadaAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterArgumentosLlamadaAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitArgumentosLlamadaAux(this);
		}
	}

	public final ArgumentosLlamadaAuxContext argumentosLlamadaAux() throws RecognitionException {
		ArgumentosLlamadaAuxContext _localctx = new ArgumentosLlamadaAuxContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_argumentosLlamadaAux);
		try {
			setState(490);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(487);
				match(COMMA);
				setState(488);
				argumentosLlamada();
				}
				break;
			case LEFT_PARENTHESIS:
			case RIGHT_PARENTHESIS:
			case THIS:
			case TYPE_INT:
			case TYPE_FLOAT:
			case TYPE_CHAR:
			case TYPE_STRING:
			case TYPE_BOOL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LecturaContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(Objective_JSParser.READ, 0); }
		public TerminalNode INPUT_STREAM() { return getToken(Objective_JSParser.INPUT_STREAM, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public LecturaAuxContext lecturaAux() {
			return getRuleContext(LecturaAuxContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(Objective_JSParser.SEMICOLON, 0); }
		public LecturaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lectura; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterLectura(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitLectura(this);
		}
	}

	public final LecturaContext lectura() throws RecognitionException {
		LecturaContext _localctx = new LecturaContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_lectura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(492);
			match(READ);
			setState(493);
			match(INPUT_STREAM);
			setState(494);
			match(ID);
			setState(495);
			lecturaAux();
			setState(496);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LecturaAuxContext extends ParserRuleContext {
		public TerminalNode INPUT_STREAM() { return getToken(Objective_JSParser.INPUT_STREAM, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public LecturaAuxContext lecturaAux() {
			return getRuleContext(LecturaAuxContext.class,0);
		}
		public LecturaAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lecturaAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterLecturaAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitLecturaAux(this);
		}
	}

	public final LecturaAuxContext lecturaAux() throws RecognitionException {
		LecturaAuxContext _localctx = new LecturaAuxContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_lecturaAux);
		try {
			setState(502);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INPUT_STREAM:
				enterOuterAlt(_localctx, 1);
				{
				setState(498);
				match(INPUT_STREAM);
				setState(499);
				match(ID);
				setState(500);
				lecturaAux();
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjetoContext extends ParserRuleContext {
		public ObjetoAuxContext objetoAux() {
			return getRuleContext(ObjetoAuxContext.class,0);
		}
		public ObjetoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objeto; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterObjeto(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitObjeto(this);
		}
	}

	public final ObjetoContext objeto() throws RecognitionException {
		ObjetoContext _localctx = new ObjetoContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_objeto);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(504);
			objetoAux();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjetoAuxContext extends ParserRuleContext {
		public TerminalNode THIS() { return getToken(Objective_JSParser.THIS, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public ObjetoAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objetoAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterObjetoAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitObjetoAux(this);
		}
	}

	public final ObjetoAuxContext objetoAux() throws RecognitionException {
		ObjetoAuxContext _localctx = new ObjetoAuxContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_objetoAux);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(506);
			_la = _input.LA(1);
			if ( !(_la==THIS || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MegaExpresionContext extends ParserRuleContext {
		public SuperExpresionContext superExpresion() {
			return getRuleContext(SuperExpresionContext.class,0);
		}
		public MegaExpresionAuxContext megaExpresionAux() {
			return getRuleContext(MegaExpresionAuxContext.class,0);
		}
		public MegaExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_megaExpresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMegaExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMegaExpresion(this);
		}
	}

	public final MegaExpresionContext megaExpresion() throws RecognitionException {
		MegaExpresionContext _localctx = new MegaExpresionContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_megaExpresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(508);
			superExpresion();
			setState(509);
			megaExpresionAux();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MegaExpresionAuxContext extends ParserRuleContext {
		public TerminalNode LOGICAL_AND_OPERATOR() { return getToken(Objective_JSParser.LOGICAL_AND_OPERATOR, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode LOGICAL_OR_OPERATOR() { return getToken(Objective_JSParser.LOGICAL_OR_OPERATOR, 0); }
		public MegaExpresionAuxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_megaExpresionAux; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMegaExpresionAux(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMegaExpresionAux(this);
		}
	}

	public final MegaExpresionAuxContext megaExpresionAux() throws RecognitionException {
		MegaExpresionAuxContext _localctx = new MegaExpresionAuxContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_megaExpresionAux);
		try {
			setState(515);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LOGICAL_AND_OPERATOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(511);
				match(LOGICAL_AND_OPERATOR);
				setState(512);
				megaExpresion();
				}
				break;
			case LOGICAL_OR_OPERATOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(513);
				match(LOGICAL_OR_OPERATOR);
				setState(514);
				megaExpresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuperExpresionContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public SuperExpresionOperadoresContext superExpresionOperadores() {
			return getRuleContext(SuperExpresionOperadoresContext.class,0);
		}
		public SuperExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_superExpresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterSuperExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitSuperExpresion(this);
		}
	}

	public final SuperExpresionContext superExpresion() throws RecognitionException {
		SuperExpresionContext _localctx = new SuperExpresionContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_superExpresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			expresion();
			setState(518);
			superExpresionOperadores();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuperExpresionOperadoresContext extends ParserRuleContext {
		public TerminalNode GREATER_THAN_OPERATOR() { return getToken(Objective_JSParser.GREATER_THAN_OPERATOR, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode GREATER_OR_EQUAL_THAN_OPERATOR() { return getToken(Objective_JSParser.GREATER_OR_EQUAL_THAN_OPERATOR, 0); }
		public TerminalNode LESS_THAN_OPERATOR() { return getToken(Objective_JSParser.LESS_THAN_OPERATOR, 0); }
		public TerminalNode LESS_THAN_OR_EQUAL_OPERATOR() { return getToken(Objective_JSParser.LESS_THAN_OR_EQUAL_OPERATOR, 0); }
		public TerminalNode NOT_EQUAL_OPERATOR() { return getToken(Objective_JSParser.NOT_EQUAL_OPERATOR, 0); }
		public TerminalNode EQUAL_OPERATOR() { return getToken(Objective_JSParser.EQUAL_OPERATOR, 0); }
		public SuperExpresionOperadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_superExpresionOperadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterSuperExpresionOperadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitSuperExpresionOperadores(this);
		}
	}

	public final SuperExpresionOperadoresContext superExpresionOperadores() throws RecognitionException {
		SuperExpresionOperadoresContext _localctx = new SuperExpresionOperadoresContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_superExpresionOperadores);
		try {
			setState(533);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GREATER_THAN_OPERATOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(520);
				match(GREATER_THAN_OPERATOR);
				setState(521);
				expresion();
				}
				break;
			case GREATER_OR_EQUAL_THAN_OPERATOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(522);
				match(GREATER_OR_EQUAL_THAN_OPERATOR);
				setState(523);
				expresion();
				}
				break;
			case LESS_THAN_OPERATOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(524);
				match(LESS_THAN_OPERATOR);
				setState(525);
				expresion();
				}
				break;
			case LESS_THAN_OR_EQUAL_OPERATOR:
				enterOuterAlt(_localctx, 4);
				{
				setState(526);
				match(LESS_THAN_OR_EQUAL_OPERATOR);
				setState(527);
				expresion();
				}
				break;
			case NOT_EQUAL_OPERATOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(528);
				match(NOT_EQUAL_OPERATOR);
				setState(529);
				expresion();
				}
				break;
			case EQUAL_OPERATOR:
				enterOuterAlt(_localctx, 6);
				{
				setState(530);
				match(EQUAL_OPERATOR);
				setState(531);
				expresion();
				}
				break;
			case LOGICAL_AND_OPERATOR:
			case LOGICAL_OR_OPERATOR:
				enterOuterAlt(_localctx, 7);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpresionContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public ExpresionOperadoresContext expresionOperadores() {
			return getRuleContext(ExpresionOperadoresContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitExpresion(this);
		}
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(535);
			termino();
			setState(536);
			expresionOperadores();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpresionOperadoresContext extends ParserRuleContext {
		public TerminalNode SUM_OPERATOR() { return getToken(Objective_JSParser.SUM_OPERATOR, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode SUBSTRACTION_OPERATOR() { return getToken(Objective_JSParser.SUBSTRACTION_OPERATOR, 0); }
		public ExpresionOperadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionOperadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterExpresionOperadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitExpresionOperadores(this);
		}
	}

	public final ExpresionOperadoresContext expresionOperadores() throws RecognitionException {
		ExpresionOperadoresContext _localctx = new ExpresionOperadoresContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_expresionOperadores);
		try {
			setState(543);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUM_OPERATOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(538);
				match(SUM_OPERATOR);
				setState(539);
				termino();
				}
				break;
			case SUBSTRACTION_OPERATOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(540);
				match(SUBSTRACTION_OPERATOR);
				setState(541);
				termino();
				}
				break;
			case EQUAL_OPERATOR:
			case NOT_EQUAL_OPERATOR:
			case GREATER_THAN_OPERATOR:
			case GREATER_OR_EQUAL_THAN_OPERATOR:
			case LESS_THAN_OPERATOR:
			case LESS_THAN_OR_EQUAL_OPERATOR:
			case LOGICAL_AND_OPERATOR:
			case LOGICAL_OR_OPERATOR:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminoOperadoresContext terminoOperadores() {
			return getRuleContext(TerminoOperadoresContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTermino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTermino(this);
		}
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(545);
			factor();
			setState(546);
			terminoOperadores();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminoOperadoresContext extends ParserRuleContext {
		public TerminalNode MULTIPLICATION_OPERATOR() { return getToken(Objective_JSParser.MULTIPLICATION_OPERATOR, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode DIVISION_OPERATOR() { return getToken(Objective_JSParser.DIVISION_OPERATOR, 0); }
		public TerminoOperadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminoOperadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterTerminoOperadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitTerminoOperadores(this);
		}
	}

	public final TerminoOperadoresContext terminoOperadores() throws RecognitionException {
		TerminoOperadoresContext _localctx = new TerminoOperadoresContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_terminoOperadores);
		try {
			setState(553);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULTIPLICATION_OPERATOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(548);
				match(MULTIPLICATION_OPERATOR);
				setState(549);
				termino();
				}
				break;
			case DIVISION_OPERATOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(550);
				match(DIVISION_OPERATOR);
				setState(551);
				termino();
				}
				break;
			case SUM_OPERATOR:
			case SUBSTRACTION_OPERATOR:
			case EQUAL_OPERATOR:
			case NOT_EQUAL_OPERATOR:
			case GREATER_THAN_OPERATOR:
			case GREATER_OR_EQUAL_THAN_OPERATOR:
			case LESS_THAN_OPERATOR:
			case LESS_THAN_OR_EQUAL_OPERATOR:
			case LOGICAL_AND_OPERATOR:
			case LOGICAL_OR_OPERATOR:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public VarCteContext varCte() {
			return getRuleContext(VarCteContext.class,0);
		}
		public FactorParentesisContext factorParentesis() {
			return getRuleContext(FactorParentesisContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_factor);
		try {
			setState(557);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case THIS:
			case TYPE_INT:
			case TYPE_FLOAT:
			case TYPE_CHAR:
			case TYPE_STRING:
			case TYPE_BOOL:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(555);
				varCte();
				}
				break;
			case LEFT_PARENTHESIS:
				enterOuterAlt(_localctx, 2);
				{
				setState(556);
				factorParentesis();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorParentesisContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(Objective_JSParser.LEFT_PARENTHESIS, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(Objective_JSParser.RIGHT_PARENTHESIS, 0); }
		public FactorParentesisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factorParentesis; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterFactorParentesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitFactorParentesis(this);
		}
	}

	public final FactorParentesisContext factorParentesis() throws RecognitionException {
		FactorParentesisContext _localctx = new FactorParentesisContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_factorParentesis);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(559);
			match(LEFT_PARENTHESIS);
			setState(560);
			megaExpresion();
			setState(561);
			match(RIGHT_PARENTHESIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarCteContext extends ParserRuleContext {
		public ObjetoContext objeto() {
			return getRuleContext(ObjetoContext.class,0);
		}
		public TerminalNode TYPE_INT() { return getToken(Objective_JSParser.TYPE_INT, 0); }
		public TerminalNode TYPE_FLOAT() { return getToken(Objective_JSParser.TYPE_FLOAT, 0); }
		public TerminalNode TYPE_STRING() { return getToken(Objective_JSParser.TYPE_STRING, 0); }
		public TerminalNode TYPE_CHAR() { return getToken(Objective_JSParser.TYPE_CHAR, 0); }
		public TerminalNode TYPE_BOOL() { return getToken(Objective_JSParser.TYPE_BOOL, 0); }
		public TerminalNode ID() { return getToken(Objective_JSParser.ID, 0); }
		public TerminalNode LEFT_SQUARE_BRACKET() { return getToken(Objective_JSParser.LEFT_SQUARE_BRACKET, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode RIGHT_SQUARE_BRACKET() { return getToken(Objective_JSParser.RIGHT_SQUARE_BRACKET, 0); }
		public MatrixContext matrix() {
			return getRuleContext(MatrixContext.class,0);
		}
		public VarCteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varCte; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterVarCte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitVarCte(this);
		}
	}

	public final VarCteContext varCte() throws RecognitionException {
		VarCteContext _localctx = new VarCteContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_varCte);
		try {
			setState(575);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(563);
				objeto();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(564);
				match(TYPE_INT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(565);
				match(TYPE_FLOAT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(566);
				match(TYPE_STRING);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(567);
				match(TYPE_CHAR);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(568);
				match(TYPE_BOOL);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(569);
				match(ID);
				setState(570);
				match(LEFT_SQUARE_BRACKET);
				setState(571);
				megaExpresion();
				setState(572);
				match(RIGHT_SQUARE_BRACKET);
				setState(573);
				matrix();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MatrixContext extends ParserRuleContext {
		public TerminalNode LEFT_SQUARE_BRACKET() { return getToken(Objective_JSParser.LEFT_SQUARE_BRACKET, 0); }
		public MegaExpresionContext megaExpresion() {
			return getRuleContext(MegaExpresionContext.class,0);
		}
		public TerminalNode RIGHT_SQUARE_BRACKET() { return getToken(Objective_JSParser.RIGHT_SQUARE_BRACKET, 0); }
		public MatrixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matrix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).enterMatrix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Objective_JSListener ) ((Objective_JSListener)listener).exitMatrix(this);
		}
	}

	public final MatrixContext matrix() throws RecognitionException {
		MatrixContext _localctx = new MatrixContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_matrix);
		try {
			setState(582);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_SQUARE_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(577);
				match(LEFT_SQUARE_BRACKET);
				setState(578);
				megaExpresion();
				setState(579);
				match(RIGHT_SQUARE_BRACKET);
				}
				break;
			case SUM_OPERATOR:
			case SUBSTRACTION_OPERATOR:
			case MULTIPLICATION_OPERATOR:
			case DIVISION_OPERATOR:
			case EQUAL_OPERATOR:
			case NOT_EQUAL_OPERATOR:
			case GREATER_THAN_OPERATOR:
			case GREATER_OR_EQUAL_THAN_OPERATOR:
			case LESS_THAN_OPERATOR:
			case LESS_THAN_OR_EQUAL_OPERATOR:
			case LOGICAL_AND_OPERATOR:
			case LOGICAL_OR_OPERATOR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B\u024b\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\3\2\3\2\5\2\u0099\n\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\3\5\5\5\u00a7\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00bc\n\b\3\t\3\t\3\t\5\t\u00c1"+
		"\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\f\3\f\5\f\u00d4\n\f\3\r\3\r\5\r\u00d8\n\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e6\n\17\3\20\3\20\3\20\3\20"+
		"\5\20\u00ec\n\20\3\21\3\21\3\21\3\21\5\21\u00f2\n\21\3\22\3\22\3\22\3"+
		"\22\5\22\u00f8\n\22\3\23\3\23\3\23\3\23\5\23\u00fe\n\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u010e\n\25"+
		"\3\26\3\26\3\26\3\26\3\26\5\26\u0115\n\26\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\5\27\u011f\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u0126\n\30\3"+
		"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u0131\n\32\3\33\3\33"+
		"\3\33\3\34\3\34\5\34\u0138\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u014c\n\37\3 "+
		"\3 \3 \3 \3 \5 \u0153\n \3!\3!\3!\3!\3!\3!\5!\u015b\n!\3\"\3\"\3#\3#\3"+
		"#\3#\3#\3$\3$\3$\3$\5$\u0168\n$\3%\3%\3%\3%\3%\5%\u016f\n%\3&\3&\5&\u0173"+
		"\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u0181\n(\3)\3)\3)\3"+
		")\3)\3)\3)\3)\3)\5)\u018c\n)\3*\3*\3*\3*\5*\u0192\n*\3+\3+\3+\3,\3,\3"+
		",\3,\3,\3-\3-\3-\3-\5-\u01a0\n-\3.\3.\3/\3/\3\60\3\60\3\60\3\60\3\60\3"+
		"\60\3\60\5\60\u01ad\n\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63"+
		"\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\5\64\u01c2\n\64\3\65"+
		"\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u01d0\n\66"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39\3"+
		"9\39\39\3:\3:\3:\3:\3:\3;\3;\3;\5;\u01ed\n;\3<\3<\3<\3<\3<\3<\3=\3=\3"+
		"=\3=\5=\u01f9\n=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3A\5A\u0206\nA\3B\3B\3"+
		"B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u0218\nC\3D\3D\3D\3E\3E\3"+
		"E\3E\3E\5E\u0222\nE\3F\3F\3F\3G\3G\3G\3G\3G\5G\u022c\nG\3H\3H\5H\u0230"+
		"\nH\3I\3I\3I\3I\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u0242\nJ\3K\3K"+
		"\3K\3K\3K\5K\u0249\nK\3K\2\2L\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 "+
		"\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082"+
		"\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\2\5\3\2;>\3\2\66"+
		"9\4\2&&AA\2\u0239\2\u0098\3\2\2\2\4\u009a\3\2\2\2\6\u009d\3\2\2\2\b\u00a6"+
		"\3\2\2\2\n\u00a8\3\2\2\2\f\u00b3\3\2\2\2\16\u00bb\3\2\2\2\20\u00c0\3\2"+
		"\2\2\22\u00c2\3\2\2\2\24\u00ca\3\2\2\2\26\u00d3\3\2\2\2\30\u00d7\3\2\2"+
		"\2\32\u00d9\3\2\2\2\34\u00e5\3\2\2\2\36\u00eb\3\2\2\2 \u00f1\3\2\2\2\""+
		"\u00f7\3\2\2\2$\u00fd\3\2\2\2&\u00ff\3\2\2\2(\u010d\3\2\2\2*\u0114\3\2"+
		"\2\2,\u011e\3\2\2\2.\u0125\3\2\2\2\60\u0127\3\2\2\2\62\u0130\3\2\2\2\64"+
		"\u0132\3\2\2\2\66\u0137\3\2\2\28\u0139\3\2\2\2:\u0141\3\2\2\2<\u014b\3"+
		"\2\2\2>\u0152\3\2\2\2@\u015a\3\2\2\2B\u015c\3\2\2\2D\u015e\3\2\2\2F\u0167"+
		"\3\2\2\2H\u016e\3\2\2\2J\u0172\3\2\2\2L\u0174\3\2\2\2N\u0180\3\2\2\2P"+
		"\u018b\3\2\2\2R\u0191\3\2\2\2T\u0193\3\2\2\2V\u0196\3\2\2\2X\u019f\3\2"+
		"\2\2Z\u01a1\3\2\2\2\\\u01a3\3\2\2\2^\u01ac\3\2\2\2`\u01ae\3\2\2\2b\u01b3"+
		"\3\2\2\2d\u01b6\3\2\2\2f\u01c1\3\2\2\2h\u01c3\3\2\2\2j\u01cf\3\2\2\2l"+
		"\u01d1\3\2\2\2n\u01db\3\2\2\2p\u01de\3\2\2\2r\u01e4\3\2\2\2t\u01ec\3\2"+
		"\2\2v\u01ee\3\2\2\2x\u01f8\3\2\2\2z\u01fa\3\2\2\2|\u01fc\3\2\2\2~\u01fe"+
		"\3\2\2\2\u0080\u0205\3\2\2\2\u0082\u0207\3\2\2\2\u0084\u0217\3\2\2\2\u0086"+
		"\u0219\3\2\2\2\u0088\u0221\3\2\2\2\u008a\u0223\3\2\2\2\u008c\u022b\3\2"+
		"\2\2\u008e\u022f\3\2\2\2\u0090\u0231\3\2\2\2\u0092\u0241\3\2\2\2\u0094"+
		"\u0248\3\2\2\2\u0096\u0099\5\6\4\2\u0097\u0099\5\4\3\2\u0098\u0096\3\2"+
		"\2\2\u0098\u0097\3\2\2\2\u0099\3\3\2\2\2\u009a\u009b\5\b\5\2\u009b\u009c"+
		"\5\n\6\2\u009c\5\3\2\2\2\u009d\u009e\7\'\2\2\u009e\u009f\7@\2\2\u009f"+
		"\u00a0\5\20\t\2\u00a0\u00a1\5\22\n\2\u00a1\7\3\2\2\2\u00a2\u00a3\7\61"+
		"\2\2\u00a3\u00a4\7A\2\2\u00a4\u00a7\5\b\5\2\u00a5\u00a7\3\2\2\2\u00a6"+
		"\u00a2\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\t\3\2\2\2\u00a8\u00a9\7\'\2\2"+
		"\u00a9\u00aa\7@\2\2\u00aa\u00ab\7\36\2\2\u00ab\u00ac\5J&\2\u00ac\u00ad"+
		"\5:\36\2\u00ad\u00ae\7\62\2\2\u00ae\u00af\7\32\2\2\u00af\u00b0\7\33\2"+
		"\2\u00b0\u00b1\5\f\7\2\u00b1\u00b2\7\37\2\2\u00b2\13\3\2\2\2\u00b3\u00b4"+
		"\7\36\2\2\u00b4\u00b5\5\16\b\2\u00b5\u00b6\7\37\2\2\u00b6\r\3\2\2\2\u00b7"+
		"\u00b8\5^\60\2\u00b8\u00b9\5\16\b\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\3"+
		"\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\17\3\2\2\2\u00bd"+
		"\u00be\7(\2\2\u00be\u00c1\7@\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00bd\3\2\2"+
		"\2\u00c0\u00bf\3\2\2\2\u00c1\21\3\2\2\2\u00c2\u00c3\7\36\2\2\u00c3\u00c4"+
		"\5\24\13\2\u00c4\u00c5\5\32\16\2\u00c5\u00c6\5&\24\2\u00c6\u00c7\7\37"+
		"\2\2\u00c7\u00c8\5\64\33\2\u00c8\u00c9\5:\36\2\u00c9\23\3\2\2\2\u00ca"+
		"\u00cb\7@\2\2\u00cb\u00cc\7\32\2\2\u00cc\u00cd\5\26\f\2\u00cd\u00ce\7"+
		"\33\2\2\u00ce\u00cf\7\"\2\2\u00cf\u00d0\5\30\r\2\u00d0\25\3\2\2\2\u00d1"+
		"\u00d4\5> \2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2"+
		"\2\u00d4\27\3\2\2\2\u00d5\u00d8\5\24\13\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5"+
		"\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\31\3\2\2\2\u00d9\u00da\7)\2\2\u00da"+
		"\u00db\7\36\2\2\u00db\u00dc\5\34\17\2\u00dc\u00dd\5 \21\2\u00dd\u00de"+
		"\7\37\2\2\u00de\33\3\2\2\2\u00df\u00e0\7*\2\2\u00e0\u00e1\7!\2\2\u00e1"+
		"\u00e2\5L\'\2\u00e2\u00e3\5\36\20\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\3"+
		"\2\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\35\3\2\2\2\u00e7"+
		"\u00e8\5L\'\2\u00e8\u00e9\5\36\20\2\u00e9\u00ec\3\2\2\2\u00ea\u00ec\3"+
		"\2\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\37\3\2\2\2\u00ed"+
		"\u00ee\7+\2\2\u00ee\u00ef\7!\2\2\u00ef\u00f2\5L\'\2\u00f0\u00f2\3\2\2"+
		"\2\u00f1\u00ed\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2!\3\2\2\2\u00f3\u00f4"+
		"\5L\'\2\u00f4\u00f5\5\"\22\2\u00f5\u00f8\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7"+
		"\u00f3\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8#\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa"+
		"\u00fb\7!\2\2\u00fb\u00fe\5L\'\2\u00fc\u00fe\3\2\2\2\u00fd\u00f9\3\2\2"+
		"\2\u00fd\u00fc\3\2\2\2\u00fe%\3\2\2\2\u00ff\u0100\7-\2\2\u0100\u0101\7"+
		"\36\2\2\u0101\u0102\5(\25\2\u0102\u0103\5,\27\2\u0103\u0104\7\37\2\2\u0104"+
		"\'\3\2\2\2\u0105\u0106\7*\2\2\u0106\u0107\7!\2\2\u0107\u0108\5\60\31\2"+
		"\u0108\u0109\7\"\2\2\u0109\u010a\5*\26\2\u010a\u010e\3\2\2\2\u010b\u010c"+
		"\7*\2\2\u010c\u010e\7!\2\2\u010d\u0105\3\2\2\2\u010d\u010b\3\2\2\2\u010e"+
		")\3\2\2\2\u010f\u0110\5\60\31\2\u0110\u0111\7\"\2\2\u0111\u0112\5*\26"+
		"\2\u0112\u0115\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u010f\3\2\2\2\u0114\u0113"+
		"\3\2\2\2\u0115+\3\2\2\2\u0116\u0117\7+\2\2\u0117\u0118\7!\2\2\u0118\u0119"+
		"\5\60\31\2\u0119\u011a\7\"\2\2\u011a\u011b\5.\30\2\u011b\u011f\3\2\2\2"+
		"\u011c\u011d\7+\2\2\u011d\u011f\7\"\2\2\u011e\u0116\3\2\2\2\u011e\u011c"+
		"\3\2\2\2\u011f-\3\2\2\2\u0120\u0121\5\60\31\2\u0121\u0122\7\"\2\2\u0122"+
		"\u0123\5.\30\2\u0123\u0126\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0120\3\2"+
		"\2\2\u0125\u0124\3\2\2\2\u0126/\3\2\2\2\u0127\u0128\7.\2\2\u0128\u0129"+
		"\7A\2\2\u0129\u012a\7\32\2\2\u012a\u012b\5> \2\u012b\u012c\7\33\2\2\u012c"+
		"\u012d\5\62\32\2\u012d\61\3\2\2\2\u012e\u0131\7/\2\2\u012f\u0131\3\2\2"+
		"\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131\63\3\2\2\2\u0132\u0133"+
		"\58\35\2\u0133\u0134\5\66\34\2\u0134\65\3\2\2\2\u0135\u0138\58\35\2\u0136"+
		"\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138\67\3\2\2"+
		"\2\u0139\u013a\7@\2\2\u013a\u013b\7\32\2\2\u013b\u013c\5> \2\u013c\u013d"+
		"\7\33\2\2\u013d\u013e\7\36\2\2\u013e\u013f\5B\"\2\u013f\u0140\7\37\2\2"+
		"\u01409\3\2\2\2\u0141\u0142\7.\2\2\u0142\u0143\7A\2\2\u0143\u0144\7\32"+
		"\2\2\u0144\u0145\5> \2\u0145\u0146\7\33\2\2\u0146\u0147\5<\37\2\u0147"+
		"\u0148\5D#\2\u0148;\3\2\2\2\u0149\u014c\7/\2\2\u014a\u014c\3\2\2\2\u014b"+
		"\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c=\3\2\2\2\u014d\u014e\5R*\2\u014e"+
		"\u014f\7A\2\2\u014f\u0150\5@!\2\u0150\u0153\3\2\2\2\u0151\u0153\3\2\2"+
		"\2\u0152\u014d\3\2\2\2\u0152\u0151\3\2\2\2\u0153?\3\2\2\2\u0154\u0155"+
		"\7#\2\2\u0155\u0156\5R*\2\u0156\u0157\7A\2\2\u0157\u0158\5@!\2\u0158\u015b"+
		"\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0154\3\2\2\2\u015a\u0159\3\2\2\2\u015b"+
		"A\3\2\2\2\u015c\u015d\3\2\2\2\u015dC\3\2\2\2\u015e\u015f\7\36\2\2\u015f"+
		"\u0160\5F$\2\u0160\u0161\5H%\2\u0161\u0162\7\37\2\2\u0162E\3\2\2\2\u0163"+
		"\u0164\5^\60\2\u0164\u0165\5F$\2\u0165\u0168\3\2\2\2\u0166\u0168\3\2\2"+
		"\2\u0167\u0163\3\2\2\2\u0167\u0166\3\2\2\2\u0168G\3\2\2\2\u0169\u016a"+
		"\7\60\2\2\u016a\u016b\5~@\2\u016b\u016c\7\"\2\2\u016c\u016f\3\2\2\2\u016d"+
		"\u016f\3\2\2\2\u016e\u0169\3\2\2\2\u016e\u016d\3\2\2\2\u016fI\3\2\2\2"+
		"\u0170\u0173\5L\'\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171"+
		"\3\2\2\2\u0173K\3\2\2\2\u0174\u0175\7\65\2\2\u0175\u0176\7A\2\2\u0176"+
		"\u0177\5N(\2\u0177\u0178\7!\2\2\u0178\u0179\5R*\2\u0179\u017a\7\"\2\2"+
		"\u017a\u017b\5P)\2\u017bM\3\2\2\2\u017c\u017d\7#\2\2\u017d\u017e\7A\2"+
		"\2\u017e\u0181\5N(\2\u017f\u0181\3\2\2\2\u0180\u017c\3\2\2\2\u0180\u017f"+
		"\3\2\2\2\u0181O\3\2\2\2\u0182\u0183\7\65\2\2\u0183\u0184\7A\2\2\u0184"+
		"\u0185\5N(\2\u0185\u0186\7!\2\2\u0186\u0187\5R*\2\u0187\u0188\7\"\2\2"+
		"\u0188\u0189\5P)\2\u0189\u018c\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0182"+
		"\3\2\2\2\u018b\u018a\3\2\2\2\u018cQ\3\2\2\2\u018d\u018e\5T+\2\u018e\u018f"+
		"\5Z.\2\u018f\u0192\3\2\2\2\u0190\u0192\5Z.\2\u0191\u018d\3\2\2\2\u0191"+
		"\u0190\3\2\2\2\u0192S\3\2\2\2\u0193\u0194\7\63\2\2\u0194\u0195\5V,\2\u0195"+
		"U\3\2\2\2\u0196\u0197\7\34\2\2\u0197\u0198\7\66\2\2\u0198\u0199\7\37\2"+
		"\2\u0199\u019a\5X-\2\u019aW\3\2\2\2\u019b\u019c\7\34\2\2\u019c\u019d\7"+
		"\66\2\2\u019d\u01a0\7\37\2\2\u019e\u01a0\3\2\2\2\u019f\u019b\3\2\2\2\u019f"+
		"\u019e\3\2\2\2\u01a0Y\3\2\2\2\u01a1\u01a2\t\2\2\2\u01a2[\3\2\2\2\u01a3"+
		"\u01a4\t\3\2\2\u01a4]\3\2\2\2\u01a5\u01ad\5`\61\2\u01a6\u01ad\5b\62\2"+
		"\u01a7\u01ad\5h\65\2\u01a8\u01ad\5l\67\2\u01a9\u01ad\5L\'\2\u01aa\u01ad"+
		"\5p9\2\u01ab\u01ad\5v<\2\u01ac\u01a5\3\2\2\2\u01ac\u01a6\3\2\2\2\u01ac"+
		"\u01a7\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ac\u01aa\3\2"+
		"\2\2\u01ac\u01ab\3\2\2\2\u01ad_\3\2\2\2\u01ae\u01af\5z>\2\u01af\u01b0"+
		"\7\22\2\2\u01b0\u01b1\5~@\2\u01b1\u01b2\7\"\2\2\u01b2a\3\2\2\2\u01b3\u01b4"+
		"\7\3\2\2\u01b4\u01b5\5d\63\2\u01b5c\3\2\2\2\u01b6\u01b7\7\32\2\2\u01b7"+
		"\u01b8\5~@\2\u01b8\u01b9\7\33\2\2\u01b9\u01ba\5\f\7\2\u01ba\u01bb\5f\64"+
		"\2\u01bbe\3\2\2\2\u01bc\u01bd\7\5\2\2\u01bd\u01c2\5d\63\2\u01be\u01bf"+
		"\7\4\2\2\u01bf\u01c2\5\f\7\2\u01c0\u01c2\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c1"+
		"\u01be\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2g\3\2\2\2\u01c3\u01c4\7%\2\2\u01c4"+
		"\u01c5\7\32\2\2\u01c5\u01c6\5~@\2\u01c6\u01c7\5j\66\2\u01c7\u01c8\7\33"+
		"\2\2\u01c8\u01c9\7\"\2\2\u01c9i\3\2\2\2\u01ca\u01cb\7\13\2\2\u01cb\u01cc"+
		"\5~@\2\u01cc\u01cd\5j\66\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf"+
		"\u01ca\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0k\3\2\2\2\u01d1\u01d2\7\6\2\2"+
		"\u01d2\u01d3\5n8\2\u01d3\u01d4\7\7\2\2\u01d4\u01d5\5\f\7\2\u01d5\u01d6"+
		"\7\b\2\2\u01d6\u01d7\7\32\2\2\u01d7\u01d8\5~@\2\u01d8\u01d9\7\33\2\2\u01d9"+
		"\u01da\5\f\7\2\u01dam\3\2\2\2\u01db\u01dc\5z>\2\u01dc\u01dd\7\66\2\2\u01dd"+
		"o\3\2\2\2\u01de\u01df\5z>\2\u01df\u01e0\7\32\2\2\u01e0\u01e1\5r:\2\u01e1"+
		"\u01e2\7\33\2\2\u01e2\u01e3\7\"\2\2\u01e3q\3\2\2\2\u01e4\u01e5\5z>\2\u01e5"+
		"\u01e6\5t;\2\u01e6\u01e7\5~@\2\u01e7\u01e8\5t;\2\u01e8s\3\2\2\2\u01e9"+
		"\u01ea\7#\2\2\u01ea\u01ed\5r:\2\u01eb\u01ed\3\2\2\2\u01ec\u01e9\3\2\2"+
		"\2\u01ec\u01eb\3\2\2\2\u01edu\3\2\2\2\u01ee\u01ef\7\64\2\2\u01ef\u01f0"+
		"\7$\2\2\u01f0\u01f1\7A\2\2\u01f1\u01f2\5x=\2\u01f2\u01f3\7\"\2\2\u01f3"+
		"w\3\2\2\2\u01f4\u01f5\7$\2\2\u01f5\u01f6\7A\2\2\u01f6\u01f9\5x=\2\u01f7"+
		"\u01f9\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9y\3\2\2\2"+
		"\u01fa\u01fb\5|?\2\u01fb{\3\2\2\2\u01fc\u01fd\t\4\2\2\u01fd}\3\2\2\2\u01fe"+
		"\u01ff\5\u0082B\2\u01ff\u0200\5\u0080A\2\u0200\177\3\2\2\2\u0201\u0202"+
		"\7\30\2\2\u0202\u0206\5~@\2\u0203\u0204\7\31\2\2\u0204\u0206\5~@\2\u0205"+
		"\u0201\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0081\3\2\2\2\u0207\u0208\5\u0086"+
		"D\2\u0208\u0209\5\u0084C\2\u0209\u0083\3\2\2\2\u020a\u020b\7\24\2\2\u020b"+
		"\u0218\5\u0086D\2\u020c\u020d\7\25\2\2\u020d\u0218\5\u0086D\2\u020e\u020f"+
		"\7\26\2\2\u020f\u0218\5\u0086D\2\u0210\u0211\7\27\2\2\u0211\u0218\5\u0086"+
		"D\2\u0212\u0213\7\23\2\2\u0213\u0218\5\u0086D\2\u0214\u0215\7\21\2\2\u0215"+
		"\u0218\5\u0086D\2\u0216\u0218\3\2\2\2\u0217\u020a\3\2\2\2\u0217\u020c"+
		"\3\2\2\2\u0217\u020e\3\2\2\2\u0217\u0210\3\2\2\2\u0217\u0212\3\2\2\2\u0217"+
		"\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u0085\3\2\2\2\u0219\u021a\5\u008a"+
		"F\2\u021a\u021b\5\u0088E\2\u021b\u0087\3\2\2\2\u021c\u021d\7\13\2\2\u021d"+
		"\u0222\5\u008aF\2\u021e\u021f\7\f\2\2\u021f\u0222\5\u008aF\2\u0220\u0222"+
		"\3\2\2\2\u0221\u021c\3\2\2\2\u0221\u021e\3\2\2\2\u0221\u0220\3\2\2\2\u0222"+
		"\u0089\3\2\2\2\u0223\u0224\5\u008eH\2\u0224\u0225\5\u008cG\2\u0225\u008b"+
		"\3\2\2\2\u0226\u0227\7\r\2\2\u0227\u022c\5\u008aF\2\u0228\u0229\7\16\2"+
		"\2\u0229\u022c\5\u008aF\2\u022a\u022c\3\2\2\2\u022b\u0226\3\2\2\2\u022b"+
		"\u0228\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u008d\3\2\2\2\u022d\u0230\5\u0092"+
		"J\2\u022e\u0230\5\u0090I\2\u022f\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230"+
		"\u008f\3\2\2\2\u0231\u0232\7\32\2\2\u0232\u0233\5~@\2\u0233\u0234\7\33"+
		"\2\2\u0234\u0091\3\2\2\2\u0235\u0242\5z>\2\u0236\u0242\7\66\2\2\u0237"+
		"\u0242\7\67\2\2\u0238\u0242\79\2\2\u0239\u0242\78\2\2\u023a\u0242\7:\2"+
		"\2\u023b\u023c\7A\2\2\u023c\u023d\7\34\2\2\u023d\u023e\5~@\2\u023e\u023f"+
		"\7\35\2\2\u023f\u0240\5\u0094K\2\u0240\u0242\3\2\2\2\u0241\u0235\3\2\2"+
		"\2\u0241\u0236\3\2\2\2\u0241\u0237\3\2\2\2\u0241\u0238\3\2\2\2\u0241\u0239"+
		"\3\2\2\2\u0241\u023a\3\2\2\2\u0241\u023b\3\2\2\2\u0242\u0093\3\2\2\2\u0243"+
		"\u0244\7\34\2\2\u0244\u0245\5~@\2\u0245\u0246\7\35\2\2\u0246\u0249\3\2"+
		"\2\2\u0247\u0249\3\2\2\2\u0248\u0243\3\2\2\2\u0248\u0247\3\2\2\2\u0249"+
		"\u0095\3\2\2\2)\u0098\u00a6\u00bb\u00c0\u00d3\u00d7\u00e5\u00eb\u00f1"+
		"\u00f7\u00fd\u010d\u0114\u011e\u0125\u0130\u0137\u014b\u0152\u015a\u0167"+
		"\u016e\u0172\u0180\u018b\u0191\u019f\u01ac\u01c1\u01cf\u01ec\u01f8\u0205"+
		"\u0217\u0221\u022b\u022f\u0241\u0248";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}