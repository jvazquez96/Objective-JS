// Generated from Objective_JS.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Objective_JSLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"IF", "ELSE", "ELSE_IF", "DO", "TIMES", "WHILE", "INCREMENT_OPERATOR", 
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


	public Objective_JSLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Objective_JS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B\u01ac\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3"+
		"\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3"+
		"\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3"+
		"!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&"+
		"\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3("+
		"\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+"+
		"\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3."+
		"\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3"+
		"\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3"+
		"\63\3\64\3\64\3\64\3\64\3\65\6\65\u015b\n\65\r\65\16\65\u015c\3\66\6\66"+
		"\u0160\n\66\r\66\16\66\u0161\3\66\3\66\6\66\u0166\n\66\r\66\16\66\u0167"+
		"\3\67\3\67\3\67\3\67\38\38\78\u0170\n8\f8\168\u0173\138\38\38\39\39\3"+
		"9\39\39\39\39\39\39\59\u0180\n9\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3"+
		"<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3?\3?\7?\u019c\n?\f?\16?\u019f\13?"+
		"\3@\6@\u01a2\n@\r@\16@\u01a3\3A\6A\u01a7\nA\rA\16A\u01a8\3A\3A\2\2B\3"+
		"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37"+
		"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37="+
		" ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9"+
		"q:s;u<w=y>{?}@\177A\u0081B\3\2\7\4\2C\\c|\3\2$$\3\2C\\\5\2\62;C\\c|\5"+
		"\2\13\f\17\17\"\"\2\u01b3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2"+
		"\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67"+
		"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2"+
		"\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]"+
		"\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2"+
		"\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2"+
		"\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2"+
		"\2\2\3\u0083\3\2\2\2\5\u0086\3\2\2\2\7\u008b\3\2\2\2\t\u0091\3\2\2\2\13"+
		"\u0094\3\2\2\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21\u00a3\3\2\2\2\23\u00a6"+
		"\3\2\2\2\25\u00a8\3\2\2\2\27\u00aa\3\2\2\2\31\u00ac\3\2\2\2\33\u00ae\3"+
		"\2\2\2\35\u00b0\3\2\2\2\37\u00b2\3\2\2\2!\u00b5\3\2\2\2#\u00b7\3\2\2\2"+
		"%\u00ba\3\2\2\2\'\u00bc\3\2\2\2)\u00bf\3\2\2\2+\u00c1\3\2\2\2-\u00c4\3"+
		"\2\2\2/\u00c7\3\2\2\2\61\u00ca\3\2\2\2\63\u00cc\3\2\2\2\65\u00ce\3\2\2"+
		"\2\67\u00d0\3\2\2\29\u00d2\3\2\2\2;\u00d4\3\2\2\2=\u00d6\3\2\2\2?\u00d8"+
		"\3\2\2\2A\u00da\3\2\2\2C\u00dc\3\2\2\2E\u00de\3\2\2\2G\u00e1\3\2\2\2I"+
		"\u00e7\3\2\2\2K\u00ec\3\2\2\2M\u00f2\3\2\2\2O\u00fb\3\2\2\2Q\u0106\3\2"+
		"\2\2S\u010d\3\2\2\2U\u0115\3\2\2\2W\u011f\3\2\2\2Y\u0127\3\2\2\2[\u0130"+
		"\3\2\2\2]\u0138\3\2\2\2_\u013f\3\2\2\2a\u0146\3\2\2\2c\u014b\3\2\2\2e"+
		"\u0150\3\2\2\2g\u0155\3\2\2\2i\u015a\3\2\2\2k\u015f\3\2\2\2m\u0169\3\2"+
		"\2\2o\u016d\3\2\2\2q\u017f\3\2\2\2s\u0181\3\2\2\2u\u0185\3\2\2\2w\u018b"+
		"\3\2\2\2y\u0190\3\2\2\2{\u0197\3\2\2\2}\u0199\3\2\2\2\177\u01a1\3\2\2"+
		"\2\u0081\u01a6\3\2\2\2\u0083\u0084\7k\2\2\u0084\u0085\7h\2\2\u0085\4\3"+
		"\2\2\2\u0086\u0087\7g\2\2\u0087\u0088\7n\2\2\u0088\u0089\7u\2\2\u0089"+
		"\u008a\7g\2\2\u008a\6\3\2\2\2\u008b\u008c\7g\2\2\u008c\u008d\7n\2\2\u008d"+
		"\u008e\7u\2\2\u008e\u008f\7k\2\2\u008f\u0090\7h\2\2\u0090\b\3\2\2\2\u0091"+
		"\u0092\7f\2\2\u0092\u0093\7q\2\2\u0093\n\3\2\2\2\u0094\u0095\7v\2\2\u0095"+
		"\u0096\7k\2\2\u0096\u0097\7o\2\2\u0097\u0098\7g\2\2\u0098\u0099\7u\2\2"+
		"\u0099\f\3\2\2\2\u009a\u009b\7y\2\2\u009b\u009c\7j\2\2\u009c\u009d\7k"+
		"\2\2\u009d\u009e\7n\2\2\u009e\u009f\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1"+
		"\7-\2\2\u00a1\u00a2\7-\2\2\u00a2\20\3\2\2\2\u00a3\u00a4\7/\2\2\u00a4\u00a5"+
		"\7/\2\2\u00a5\22\3\2\2\2\u00a6\u00a7\7-\2\2\u00a7\24\3\2\2\2\u00a8\u00a9"+
		"\7/\2\2\u00a9\26\3\2\2\2\u00aa\u00ab\7,\2\2\u00ab\30\3\2\2\2\u00ac\u00ad"+
		"\7\61\2\2\u00ad\32\3\2\2\2\u00ae\u00af\7\'\2\2\u00af\34\3\2\2\2\u00b0"+
		"\u00b1\7`\2\2\u00b1\36\3\2\2\2\u00b2\u00b3\7?\2\2\u00b3\u00b4\7?\2\2\u00b4"+
		" \3\2\2\2\u00b5\u00b6\7?\2\2\u00b6\"\3\2\2\2\u00b7\u00b8\7#\2\2\u00b8"+
		"\u00b9\7?\2\2\u00b9$\3\2\2\2\u00ba\u00bb\7@\2\2\u00bb&\3\2\2\2\u00bc\u00bd"+
		"\7@\2\2\u00bd\u00be\7?\2\2\u00be(\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0*\3"+
		"\2\2\2\u00c1\u00c2\7>\2\2\u00c2\u00c3\7?\2\2\u00c3,\3\2\2\2\u00c4\u00c5"+
		"\7(\2\2\u00c5\u00c6\7(\2\2\u00c6.\3\2\2\2\u00c7\u00c8\7~\2\2\u00c8\u00c9"+
		"\7~\2\2\u00c9\60\3\2\2\2\u00ca\u00cb\7*\2\2\u00cb\62\3\2\2\2\u00cc\u00cd"+
		"\7+\2\2\u00cd\64\3\2\2\2\u00ce\u00cf\7]\2\2\u00cf\66\3\2\2\2\u00d0\u00d1"+
		"\7_\2\2\u00d18\3\2\2\2\u00d2\u00d3\7}\2\2\u00d3:\3\2\2\2\u00d4\u00d5\7"+
		"\177\2\2\u00d5<\3\2\2\2\u00d6\u00d7\7\60\2\2\u00d7>\3\2\2\2\u00d8\u00d9"+
		"\7<\2\2\u00d9@\3\2\2\2\u00da\u00db\7=\2\2\u00dbB\3\2\2\2\u00dc\u00dd\7"+
		".\2\2\u00ddD\3\2\2\2\u00de\u00df\7@\2\2\u00df\u00e0\7@\2\2\u00e0F\3\2"+
		"\2\2\u00e1\u00e2\7r\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5"+
		"\7p\2\2\u00e5\u00e6\7v\2\2\u00e6H\3\2\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9"+
		"\7j\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7u\2\2\u00ebJ\3\2\2\2\u00ec\u00ed"+
		"\7E\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7u\2\2\u00f0"+
		"\u00f1\7u\2\2\u00f1L\3\2\2\2\u00f2\u00f3\7K\2\2\u00f3\u00f4\7p\2\2\u00f4"+
		"\u00f5\7j\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7k\2\2"+
		"\u00f8\u00f9\7v\2\2\u00f9\u00fa\7u\2\2\u00faN\3\2\2\2\u00fb\u00fc\7C\2"+
		"\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100"+
		"\7k\2\2\u0100\u0101\7d\2\2\u0101\u0102\7w\2\2\u0102\u0103\7v\2\2\u0103"+
		"\u0104\7g\2\2\u0104\u0105\7u\2\2\u0105P\3\2\2\2\u0106\u0107\7r\2\2\u0107"+
		"\u0108\7w\2\2\u0108\u0109\7d\2\2\u0109\u010a\7n\2\2\u010a\u010b\7k\2\2"+
		"\u010b\u010c\7e\2\2\u010cR\3\2\2\2\u010d\u010e\7r\2\2\u010e\u010f\7t\2"+
		"\2\u010f\u0110\7k\2\2\u0110\u0111\7x\2\2\u0111\u0112\7c\2\2\u0112\u0113"+
		"\7v\2\2\u0113\u0114\7g\2\2\u0114T\3\2\2\2\u0115\u0116\7r\2\2\u0116\u0117"+
		"\7t\2\2\u0117\u0118\7q\2\2\u0118\u0119\7v\2\2\u0119\u011a\7g\2\2\u011a"+
		"\u011b\7e\2\2\u011b\u011c\7v\2\2\u011c\u011d\7g\2\2\u011d\u011e\7f\2\2"+
		"\u011eV\3\2\2\2\u011f\u0120\7O\2\2\u0120\u0121\7g\2\2\u0121\u0122\7v\2"+
		"\2\u0122\u0123\7j\2\2\u0123\u0124\7q\2\2\u0124\u0125\7f\2\2\u0125\u0126"+
		"\7u\2\2\u0126X\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129\7w\2\2\u0129\u012a"+
		"\7p\2\2\u012a\u012b\7e\2\2\u012b\u012c\7v\2\2\u012c\u012d\7k\2\2\u012d"+
		"\u012e\7q\2\2\u012e\u012f\7p\2\2\u012fZ\3\2\2\2\u0130\u0131\7t\2\2\u0131"+
		"\u0132\7g\2\2\u0132\u0133\7v\2\2\u0133\u0134\7w\2\2\u0134\u0135\7t\2\2"+
		"\u0135\u0136\7p\2\2\u0136\u0137\7u\2\2\u0137\\\3\2\2\2\u0138\u0139\7t"+
		"\2\2\u0139\u013a\7g\2\2\u013a\u013b\7v\2\2\u013b\u013c\7w\2\2\u013c\u013d"+
		"\7t\2\2\u013d\u013e\7p\2\2\u013e^\3\2\2\2\u013f\u0140\7k\2\2\u0140\u0141"+
		"\7o\2\2\u0141\u0142\7r\2\2\u0142\u0143\7q\2\2\u0143\u0144\7t\2\2\u0144"+
		"\u0145\7v\2\2\u0145`\3\2\2\2\u0146\u0147\7o\2\2\u0147\u0148\7c\2\2\u0148"+
		"\u0149\7k\2\2\u0149\u014a\7p\2\2\u014ab\3\2\2\2\u014b\u014c\7n\2\2\u014c"+
		"\u014d\7k\2\2\u014d\u014e\7u\2\2\u014e\u014f\7v\2\2\u014fd\3\2\2\2\u0150"+
		"\u0151\7t\2\2\u0151\u0152\7g\2\2\u0152\u0153\7c\2\2\u0153\u0154\7f\2\2"+
		"\u0154f\3\2\2\2\u0155\u0156\7x\2\2\u0156\u0157\7c\2\2\u0157\u0158\7t\2"+
		"\2\u0158h\3\2\2\2\u0159\u015b\4\62;\2\u015a\u0159\3\2\2\2\u015b\u015c"+
		"\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dj\3\2\2\2\u015e"+
		"\u0160\4\62;\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2"+
		"\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\7\60\2\2\u0164"+
		"\u0166\4\62;\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2"+
		"\2\2\u0167\u0168\3\2\2\2\u0168l\3\2\2\2\u0169\u016a\7$\2\2\u016a\u016b"+
		"\t\2\2\2\u016b\u016c\7$\2\2\u016cn\3\2\2\2\u016d\u0171\7$\2\2\u016e\u0170"+
		"\n\3\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171"+
		"\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175\7$"+
		"\2\2\u0175p\3\2\2\2\u0176\u0177\7v\2\2\u0177\u0178\7t\2\2\u0178\u0179"+
		"\7w\2\2\u0179\u0180\7g\2\2\u017a\u017b\7h\2\2\u017b\u017c\7c\2\2\u017c"+
		"\u017d\7n\2\2\u017d\u017e\7u\2\2\u017e\u0180\7g\2\2\u017f\u0176\3\2\2"+
		"\2\u017f\u017a\3\2\2\2\u0180r\3\2\2\2\u0181\u0182\7k\2\2\u0182\u0183\7"+
		"p\2\2\u0183\u0184\7v\2\2\u0184t\3\2\2\2\u0185\u0186\7h\2\2\u0186\u0187"+
		"\7n\2\2\u0187\u0188\7q\2\2\u0188\u0189\7c\2\2\u0189\u018a\7v\2\2\u018a"+
		"v\3\2\2\2\u018b\u018c\7e\2\2\u018c\u018d\7j\2\2\u018d\u018e\7c\2\2\u018e"+
		"\u018f\7t\2\2\u018fx\3\2\2\2\u0190\u0191\7u\2\2\u0191\u0192\7v\2\2\u0192"+
		"\u0193\7t\2\2\u0193\u0194\7k\2\2\u0194\u0195\7p\2\2\u0195\u0196\7i\2\2"+
		"\u0196z\3\2\2\2\u0197\u0198\7$\2\2\u0198|\3\2\2\2\u0199\u019d\t\4\2\2"+
		"\u019a\u019c\t\2\2\2\u019b\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b"+
		"\3\2\2\2\u019d\u019e\3\2\2\2\u019e~\3\2\2\2\u019f\u019d\3\2\2\2\u01a0"+
		"\u01a2\t\5\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2"+
		"\2\2\u01a3\u01a4\3\2\2\2\u01a4\u0080\3\2\2\2\u01a5\u01a7\t\6\2\2\u01a6"+
		"\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2"+
		"\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\bA\2\2\u01ab\u0082\3\2\2\2\13\2\u015c"+
		"\u0161\u0167\u0171\u017f\u019d\u01a3\u01a8\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}