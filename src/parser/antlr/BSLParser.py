# Generated from ../parser/BSL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0118\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\7\29\n\2\f\2\16\2<\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\5\4E\n\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\5\6N\n\6\3\6\3\6\3\6\5\6S\n\6\3\6\7\6V")
        buf.write("\n\6\f\6\16\6Y\13\6\3\6\3\6\5\6]\n\6\3\7\5\7`\n\7\3\7")
        buf.write("\3\7\3\7\5\7e\n\7\3\7\7\7h\n\7\f\7\16\7k\13\7\3\7\3\7")
        buf.write("\5\7o\n\7\3\b\3\b\3\b\3\b\7\bu\n\b\f\b\16\bx\13\b\5\b")
        buf.write("z\n\b\3\b\3\b\3\t\5\t\177\n\t\3\t\3\t\3\t\5\t\u0084\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u008d\n\n\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u0093\n\13\3\f\3\f\3\f\3\f\7\f\u0099\n")
        buf.write("\f\f\f\16\f\u009c\13\f\3\f\3\f\7\f\u00a0\n\f\f\f\16\f")
        buf.write("\u00a3\13\f\5\f\u00a5\n\f\3\f\3\f\5\f\u00a9\n\f\3\r\3")
        buf.write("\r\5\r\u00ad\n\r\3\r\5\r\u00b0\n\r\3\16\3\16\3\16\7\16")
        buf.write("\u00b5\n\16\f\16\16\16\u00b8\13\16\3\17\3\17\3\17\5\17")
        buf.write("\u00bd\n\17\3\17\3\17\5\17\u00c1\n\17\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00cd\n\21\f\21")
        buf.write("\16\21\u00d0\13\21\3\21\3\21\5\21\u00d4\n\21\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00da\n\22\f\22\16\22\u00dd\13\22\3\22")
        buf.write("\3\22\5\22\u00e1\n\22\3\23\3\23\3\23\7\23\u00e6\n\23\f")
        buf.write("\23\16\23\u00e9\13\23\3\24\3\24\3\24\7\24\u00ee\n\24\f")
        buf.write("\24\16\24\u00f1\13\24\3\25\3\25\3\25\5\25\u00f6\n\25\3")
        buf.write("\26\3\26\3\26\7\26\u00fb\n\26\f\26\16\26\u00fe\13\26\3")
        buf.write("\27\3\27\3\27\7\27\u0103\n\27\f\27\16\27\u0106\13\27\3")
        buf.write("\30\5\30\u0109\n\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0114\n\31\3\32\3\32\3\32\2\2\33\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\b\3")
        buf.write("\2 \"\3\2\',\3\2#$\3\2%&\4\2\37\37#$\4\2\31\34./\2\u012c")
        buf.write("\2:\3\2\2\2\4?\3\2\2\2\6A\3\2\2\2\bH\3\2\2\2\nM\3\2\2")
        buf.write("\2\f_\3\2\2\2\16p\3\2\2\2\20~\3\2\2\2\22\u008c\3\2\2\2")
        buf.write("\24\u008e\3\2\2\2\26\u0094\3\2\2\2\30\u00aa\3\2\2\2\32")
        buf.write("\u00b1\3\2\2\2\34\u00b9\3\2\2\2\36\u00c2\3\2\2\2 \u00c4")
        buf.write("\3\2\2\2\"\u00d5\3\2\2\2$\u00e2\3\2\2\2&\u00ea\3\2\2\2")
        buf.write("(\u00f2\3\2\2\2*\u00f7\3\2\2\2,\u00ff\3\2\2\2.\u0108\3")
        buf.write("\2\2\2\60\u0113\3\2\2\2\62\u0115\3\2\2\2\649\5\6\4\2\65")
        buf.write("9\5\b\5\2\669\5\n\6\2\679\5\f\7\28\64\3\2\2\28\65\3\2")
        buf.write("\2\28\66\3\2\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2")
        buf.write("\2\2;=\3\2\2\2<:\3\2\2\2=>\7\2\2\3>\3\3\2\2\2?@\t\2\2")
        buf.write("\2@\5\3\2\2\2AB\7\b\2\2BD\7-\2\2CE\7\t\2\2DC\3\2\2\2D")
        buf.write("E\3\2\2\2EF\3\2\2\2FG\7\3\2\2G\7\3\2\2\2HI\7\b\2\2IJ\7")
        buf.write("-\2\2JK\7\3\2\2K\t\3\2\2\2LN\5\4\3\2ML\3\2\2\2MN\3\2\2")
        buf.write("\2NO\3\2\2\2OP\7\n\2\2PR\7-\2\2QS\5\16\b\2RQ\3\2\2\2R")
        buf.write("S\3\2\2\2SW\3\2\2\2TV\5\22\n\2UT\3\2\2\2VY\3\2\2\2WU\3")
        buf.write("\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z\\\7\13\2\2[]\7\3")
        buf.write("\2\2\\[\3\2\2\2\\]\3\2\2\2]\13\3\2\2\2^`\5\4\3\2_^\3\2")
        buf.write("\2\2_`\3\2\2\2`a\3\2\2\2ab\7\f\2\2bd\7-\2\2ce\5\16\b\2")
        buf.write("dc\3\2\2\2de\3\2\2\2ei\3\2\2\2fh\5\22\n\2gf\3\2\2\2hk")
        buf.write("\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2ln\7\r")
        buf.write("\2\2mo\7\3\2\2nm\3\2\2\2no\3\2\2\2o\r\3\2\2\2py\7\4\2")
        buf.write("\2qv\5\20\t\2rs\7\5\2\2su\5\20\t\2tr\3\2\2\2ux\3\2\2\2")
        buf.write("vt\3\2\2\2vw\3\2\2\2wz\3\2\2\2xv\3\2\2\2yq\3\2\2\2yz\3")
        buf.write("\2\2\2z{\3\2\2\2{|\7\6\2\2|\17\3\2\2\2}\177\7\7\2\2~}")
        buf.write("\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0083\7")
        buf.write("-\2\2\u0081\u0082\7+\2\2\u0082\u0084\5\36\20\2\u0083\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\21\3\2\2\2\u0085\u008d")
        buf.write("\5\24\13\2\u0086\u008d\5\26\f\2\u0087\u008d\5 \21\2\u0088")
        buf.write("\u008d\5\"\22\2\u0089\u008d\5\30\r\2\u008a\u008d\5\34")
        buf.write("\17\2\u008b\u008d\5\b\5\2\u008c\u0085\3\2\2\2\u008c\u0086")
        buf.write("\3\2\2\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2\u008c")
        buf.write("\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2")
        buf.write("\u008d\23\3\2\2\2\u008e\u008f\7-\2\2\u008f\u0090\7+\2")
        buf.write("\2\u0090\u0092\5\36\20\2\u0091\u0093\7\3\2\2\u0092\u0091")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\25\3\2\2\2\u0094\u0095")
        buf.write("\7\16\2\2\u0095\u0096\5\36\20\2\u0096\u009a\7\17\2\2\u0097")
        buf.write("\u0099\5\22\n\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a4")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u00a1\7\21\2\2\u009e")
        buf.write("\u00a0\5\22\n\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u009d\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\7\22\2")
        buf.write("\2\u00a7\u00a9\7\3\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\27\3\2\2\2\u00aa\u00ac\7\30\2\2\u00ab\u00ad")
        buf.write("\5\36\20\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00b0\7\3\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\31\3\2\2\2\u00b1\u00b6\5\36")
        buf.write("\20\2\u00b2\u00b3\7\5\2\2\u00b3\u00b5\5\36\20\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\33\3\2\2\2\u00b8\u00b6\3\2")
        buf.write("\2\2\u00b9\u00ba\7-\2\2\u00ba\u00bc\7\4\2\2\u00bb\u00bd")
        buf.write("\5\32\16\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\7\6\2\2\u00bf\u00c1\7\3\2\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\35\3\2")
        buf.write("\2\2\u00c2\u00c3\5$\23\2\u00c3\37\3\2\2\2\u00c4\u00c5")
        buf.write("\7\23\2\2\u00c5\u00c6\7-\2\2\u00c6\u00c7\7+\2\2\u00c7")
        buf.write("\u00c8\5\36\20\2\u00c8\u00c9\7\24\2\2\u00c9\u00ca\5\36")
        buf.write("\20\2\u00ca\u00ce\7\26\2\2\u00cb\u00cd\5\22\n\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3")
        buf.write("\2\2\2\u00d1\u00d3\7\27\2\2\u00d2\u00d4\7\3\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4!\3\2\2\2\u00d5")
        buf.write("\u00d6\7\25\2\2\u00d6\u00d7\5\36\20\2\u00d7\u00db\7\26")
        buf.write("\2\2\u00d8\u00da\5\22\n\2\u00d9\u00d8\3\2\2\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0\7\27\2")
        buf.write("\2\u00df\u00e1\7\3\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1#\3\2\2\2\u00e2\u00e7\5&\24\2\u00e3\u00e4")
        buf.write("\7\36\2\2\u00e4\u00e6\5&\24\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8%\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00ef\5(\25")
        buf.write("\2\u00eb\u00ec\7\35\2\2\u00ec\u00ee\5(\25\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\'\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2")
        buf.write("\u00f5\5*\26\2\u00f3\u00f4\t\3\2\2\u00f4\u00f6\5*\26\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6)\3\2\2")
        buf.write("\2\u00f7\u00fc\5,\27\2\u00f8\u00f9\t\4\2\2\u00f9\u00fb")
        buf.write("\5,\27\2\u00fa\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd+\3\2\2\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00ff\u0104\5.\30\2\u0100\u0101\t\5\2\2")
        buf.write("\u0101\u0103\5.\30\2\u0102\u0100\3\2\2\2\u0103\u0106\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105-")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\t\6\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010b\5\60\31\2\u010b/\3\2\2\2\u010c\u0114\5\62")
        buf.write("\32\2\u010d\u0114\7-\2\2\u010e\u010f\7\4\2\2\u010f\u0110")
        buf.write("\5\36\20\2\u0110\u0111\7\6\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0114\5\34\17\2\u0113\u010c\3\2\2\2\u0113\u010d\3\2\2")
        buf.write("\2\u0113\u010e\3\2\2\2\u0113\u0112\3\2\2\2\u0114\61\3")
        buf.write("\2\2\2\u0115\u0116\t\7\2\2\u0116\63\3\2\2\2\'8:DMRW\\")
        buf.write("_dinvy~\u0083\u008c\u0092\u009a\u00a1\u00a4\u00a8\u00ac")
        buf.write("\u00af\u00b6\u00bc\u00c0\u00ce\u00d3\u00db\u00e0\u00e7")
        buf.write("\u00ef\u00f5\u00fc\u0104\u0108\u0113")
        return buf.getvalue()


class BSLParser ( Parser ):

    grammarFileName = "BSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'\u0417\u043D\u0430\u0447'", 
                     "'\u041F\u0435\u0440\u0435\u043C'", "'\u042D\u043A\u0441\u043F\u043E\u0440\u0442'", 
                     "'\u041F\u0440\u043E\u0446\u0435\u0434\u0443\u0440\u0430'", 
                     "'\u041A\u043E\u043D\u0435\u0446\u041F\u0440\u043E\u0446\u0435\u0434\u0443\u0440\u044B'", 
                     "'\u0424\u0443\u043D\u043A\u0446\u0438\u044F'", "'\u041A\u043E\u043D\u0435\u0446\u0424\u0443\u043D\u043A\u0446\u0438\u0438'", 
                     "'\u0415\u0441\u043B\u0438'", "'\u0422\u043E\u0433\u0434\u0430'", 
                     "'\u0418\u043D\u0430\u0447\u0435\u0415\u0441\u043B\u0438'", 
                     "'\u0418\u043D\u0430\u0447\u0435'", "'\u041A\u043E\u043D\u0435\u0446\u0415\u0441\u043B\u0438'", 
                     "'\u0414\u043B\u044F'", "'\u041F\u043E'", "'\u041F\u043E\u043A\u0430'", 
                     "'\u0426\u0438\u043A\u043B'", "'\u041A\u043E\u043D\u0435\u0446\u0426\u0438\u043A\u043B\u0430'", 
                     "'\u0412\u043E\u0437\u0432\u0440\u0430\u0442'", "'\u0418\u0441\u0442\u0438\u043D\u0430'", 
                     "'\u041B\u043E\u0436\u044C'", "'Null'", "'Undefined'", 
                     "'\u0418'", "'\u0418\u041B\u0418'", "'\u041D\u0415'", 
                     "'&\u041D\u0430\u041A\u043B\u0438\u0435\u043D\u0442\u0435'", 
                     "'&\u041D\u0430\u0421\u0435\u0440\u0432\u0435\u0440\u0435'", 
                     "'&\u041D\u0430\u041A\u043B\u0438\u0435\u043D\u0442\u0435\u041D\u0430\u0421\u0435\u0440\u0432\u0435\u0440\u0435'", 
                     "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PEREM", "EXPORT", "PROCEDURE", 
                      "END_PROCEDURE", "FUNCTION", "END_FUNCTION", "IF", 
                      "THEN", "ELSE_IF", "ELSE", "END_IF", "FOR", "TO", 
                      "WHILE", "LOOP", "END_LOOP", "RETURN", "TRUE", "FALSE", 
                      "NULL", "UNDEFINED", "AND", "OR", "NOT", "DIRECTIVE_CLIENT", 
                      "DIRECTIVE_SERVER", "DIRECTIVE_CLIENT_SERVER", "PLUS", 
                      "MINUS", "MULT", "DIV", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", "ID", "STRING", 
                      "NUMBER", "WS", "COMMENT" ]

    RULE_bslFile = 0
    RULE_directive = 1
    RULE_variableDeclaration = 2
    RULE_localVariableDeclaration = 3
    RULE_procedure = 4
    RULE_function = 5
    RULE_parameterList = 6
    RULE_parameter = 7
    RULE_statement = 8
    RULE_assignment = 9
    RULE_ifStatement = 10
    RULE_returnStatement = 11
    RULE_argumentList = 12
    RULE_callStatement = 13
    RULE_expression = 14
    RULE_forStatement = 15
    RULE_whileStatement = 16
    RULE_logicalOrExpression = 17
    RULE_logicalAndExpression = 18
    RULE_comparisonExpression = 19
    RULE_additiveExpression = 20
    RULE_multiplicativeExpression = 21
    RULE_unaryExpression = 22
    RULE_primaryExpression = 23
    RULE_literal = 24

    ruleNames =  [ "bslFile", "directive", "variableDeclaration", "localVariableDeclaration", 
                   "procedure", "function", "parameterList", "parameter", 
                   "statement", "assignment", "ifStatement", "returnStatement", 
                   "argumentList", "callStatement", "expression", "forStatement", 
                   "whileStatement", "logicalOrExpression", "logicalAndExpression", 
                   "comparisonExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PEREM=6
    EXPORT=7
    PROCEDURE=8
    END_PROCEDURE=9
    FUNCTION=10
    END_FUNCTION=11
    IF=12
    THEN=13
    ELSE_IF=14
    ELSE=15
    END_IF=16
    FOR=17
    TO=18
    WHILE=19
    LOOP=20
    END_LOOP=21
    RETURN=22
    TRUE=23
    FALSE=24
    NULL=25
    UNDEFINED=26
    AND=27
    OR=28
    NOT=29
    DIRECTIVE_CLIENT=30
    DIRECTIVE_SERVER=31
    DIRECTIVE_CLIENT_SERVER=32
    PLUS=33
    MINUS=34
    MULT=35
    DIV=36
    LESS=37
    LESS_OR_EQUAL=38
    GREATER=39
    GREATER_OR_EQUAL=40
    EQUAL=41
    NOT_EQUAL=42
    ID=43
    STRING=44
    NUMBER=45
    WS=46
    COMMENT=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BslFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BSLParser.EOF, 0)

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(BSLParser.VariableDeclarationContext,i)


        def localVariableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.LocalVariableDeclarationContext)
            else:
                return self.getTypedRuleContext(BSLParser.LocalVariableDeclarationContext,i)


        def procedure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ProcedureContext)
            else:
                return self.getTypedRuleContext(BSLParser.ProcedureContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.FunctionContext)
            else:
                return self.getTypedRuleContext(BSLParser.FunctionContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_bslFile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBslFile" ):
                return visitor.visitBslFile(self)
            else:
                return visitor.visitChildren(self)




    def bslFile(self):

        localctx = BSLParser.BslFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_bslFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.PROCEDURE) | (1 << BSLParser.FUNCTION) | (1 << BSLParser.DIRECTIVE_CLIENT) | (1 << BSLParser.DIRECTIVE_SERVER) | (1 << BSLParser.DIRECTIVE_CLIENT_SERVER))) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.variableDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 51
                    self.localVariableDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 52
                    self.procedure()
                    pass

                elif la_ == 4:
                    self.state = 53
                    self.function()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(BSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_CLIENT(self):
            return self.getToken(BSLParser.DIRECTIVE_CLIENT, 0)

        def DIRECTIVE_SERVER(self):
            return self.getToken(BSLParser.DIRECTIVE_SERVER, 0)

        def DIRECTIVE_CLIENT_SERVER(self):
            return self.getToken(BSLParser.DIRECTIVE_CLIENT_SERVER, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = BSLParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.DIRECTIVE_CLIENT) | (1 << BSLParser.DIRECTIVE_SERVER) | (1 << BSLParser.DIRECTIVE_CLIENT_SERVER))) != 0)):
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


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PEREM(self):
            return self.getToken(BSLParser.PEREM, 0)

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def EXPORT(self):
            return self.getToken(BSLParser.EXPORT, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = BSLParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(BSLParser.PEREM)
            self.state = 64
            self.match(BSLParser.ID)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.EXPORT:
                self.state = 65
                self.match(BSLParser.EXPORT)


            self.state = 68
            self.match(BSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PEREM(self):
            return self.getToken(BSLParser.PEREM, 0)

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_localVariableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVariableDeclaration" ):
                return visitor.visitLocalVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def localVariableDeclaration(self):

        localctx = BSLParser.LocalVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_localVariableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(BSLParser.PEREM)
            self.state = 71
            self.match(BSLParser.ID)
            self.state = 72
            self.match(BSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(BSLParser.PROCEDURE, 0)

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def END_PROCEDURE(self):
            return self.getToken(BSLParser.END_PROCEDURE, 0)

        def directive(self):
            return self.getTypedRuleContext(BSLParser.DirectiveContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(BSLParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_procedure

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = BSLParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_procedure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.DIRECTIVE_CLIENT) | (1 << BSLParser.DIRECTIVE_SERVER) | (1 << BSLParser.DIRECTIVE_CLIENT_SERVER))) != 0):
                self.state = 74
                self.directive()


            self.state = 77
            self.match(BSLParser.PROCEDURE)
            self.state = 78
            self.match(BSLParser.ID)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__1:
                self.state = 79
                self.parameterList()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                self.state = 82
                self.statement()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(BSLParser.END_PROCEDURE)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 89
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BSLParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def END_FUNCTION(self):
            return self.getToken(BSLParser.END_FUNCTION, 0)

        def directive(self):
            return self.getTypedRuleContext(BSLParser.DirectiveContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(BSLParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = BSLParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.DIRECTIVE_CLIENT) | (1 << BSLParser.DIRECTIVE_SERVER) | (1 << BSLParser.DIRECTIVE_CLIENT_SERVER))) != 0):
                self.state = 92
                self.directive()


            self.state = 95
            self.match(BSLParser.FUNCTION)
            self.state = 96
            self.match(BSLParser.ID)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__1:
                self.state = 97
                self.parameterList()


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                self.state = 100
                self.statement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(BSLParser.END_FUNCTION)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 107
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(BSLParser.ParameterContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = BSLParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BSLParser.T__1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__4 or _la==BSLParser.ID:
                self.state = 111
                self.parameter()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BSLParser.T__2:
                    self.state = 112
                    self.match(BSLParser.T__2)
                    self.state = 113
                    self.parameter()
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 121
            self.match(BSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BSLParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BSLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__4:
                self.state = 123
                self.match(BSLParser.T__4)


            self.state = 126
            self.match(BSLParser.ID)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.EQUAL:
                self.state = 127
                self.match(BSLParser.EQUAL)
                self.state = 128
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BSLParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(BSLParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(BSLParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BSLParser.WhileStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(BSLParser.ReturnStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(BSLParser.CallStatementContext,0)


        def localVariableDeclaration(self):
            return self.getTypedRuleContext(BSLParser.LocalVariableDeclarationContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.callStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.localVariableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BSLParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BSLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BSLParser.ID)
            self.state = 141
            self.match(BSLParser.EQUAL)
            self.state = 142
            self.expression()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 143
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BSLParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BSLParser.THEN, 0)

        def END_IF(self):
            return self.getToken(BSLParser.END_IF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BSLParser.ELSE, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BSLParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(BSLParser.IF)
            self.state = 147
            self.expression()
            self.state = 148
            self.match(BSLParser.THEN)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                self.state = 149
                self.statement()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.ELSE:
                self.state = 155
                self.match(BSLParser.ELSE)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                    self.state = 156
                    self.statement()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 164
            self.match(BSLParser.END_IF)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 165
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BSLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BSLParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BSLParser.RETURN)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 169
                self.expression()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 172
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = BSLParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expression()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSLParser.T__2:
                self.state = 176
                self.match(BSLParser.T__2)
                self.state = 177
                self.expression()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(BSLParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = BSLParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(BSLParser.ID)
            self.state = 184
            self.match(BSLParser.T__1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.T__1) | (1 << BSLParser.TRUE) | (1 << BSLParser.FALSE) | (1 << BSLParser.NULL) | (1 << BSLParser.UNDEFINED) | (1 << BSLParser.NOT) | (1 << BSLParser.PLUS) | (1 << BSLParser.MINUS) | (1 << BSLParser.ID) | (1 << BSLParser.STRING) | (1 << BSLParser.NUMBER))) != 0):
                self.state = 185
                self.argumentList()


            self.state = 188
            self.match(BSLParser.T__3)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 189
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(BSLParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BSLParser.FOR, 0)

        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BSLParser.EQUAL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BSLParser.TO, 0)

        def LOOP(self):
            return self.getToken(BSLParser.LOOP, 0)

        def END_LOOP(self):
            return self.getToken(BSLParser.END_LOOP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = BSLParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BSLParser.FOR)
            self.state = 195
            self.match(BSLParser.ID)
            self.state = 196
            self.match(BSLParser.EQUAL)
            self.state = 197
            self.expression()
            self.state = 198
            self.match(BSLParser.TO)
            self.state = 199
            self.expression()
            self.state = 200
            self.match(BSLParser.LOOP)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                self.state = 201
                self.statement()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(BSLParser.END_LOOP)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 208
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BSLParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def LOOP(self):
            return self.getToken(BSLParser.LOOP, 0)

        def END_LOOP(self):
            return self.getToken(BSLParser.END_LOOP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BSLParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BSLParser.WHILE)
            self.state = 212
            self.expression()
            self.state = 213
            self.match(BSLParser.LOOP)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.PEREM) | (1 << BSLParser.IF) | (1 << BSLParser.FOR) | (1 << BSLParser.WHILE) | (1 << BSLParser.RETURN) | (1 << BSLParser.ID))) != 0):
                self.state = 214
                self.statement()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(BSLParser.END_LOOP)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSLParser.T__0:
                self.state = 221
                self.match(BSLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.OR)
            else:
                return self.getToken(BSLParser.OR, i)

        def getRuleIndex(self):
            return BSLParser.RULE_logicalOrExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = BSLParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.logicalAndExpression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSLParser.OR:
                self.state = 225
                self.match(BSLParser.OR)
                self.state = 226
                self.logicalAndExpression()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ComparisonExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.ComparisonExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.AND)
            else:
                return self.getToken(BSLParser.AND, i)

        def getRuleIndex(self):
            return BSLParser.RULE_logicalAndExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = BSLParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.comparisonExpression()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSLParser.AND:
                self.state = 233
                self.match(BSLParser.AND)
                self.state = 234
                self.comparisonExpression()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.AdditiveExpressionContext,i)


        def LESS(self):
            return self.getToken(BSLParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(BSLParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(BSLParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(BSLParser.GREATER_OR_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(BSLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BSLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_comparisonExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = BSLParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comparisonExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.additiveExpression()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.LESS) | (1 << BSLParser.LESS_OR_EQUAL) | (1 << BSLParser.GREATER) | (1 << BSLParser.GREATER_OR_EQUAL) | (1 << BSLParser.EQUAL) | (1 << BSLParser.NOT_EQUAL))) != 0):
                self.state = 241
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.LESS) | (1 << BSLParser.LESS_OR_EQUAL) | (1 << BSLParser.GREATER) | (1 << BSLParser.GREATER_OR_EQUAL) | (1 << BSLParser.EQUAL) | (1 << BSLParser.NOT_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.PLUS)
            else:
                return self.getToken(BSLParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.MINUS)
            else:
                return self.getToken(BSLParser.MINUS, i)

        def getRuleIndex(self):
            return BSLParser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = BSLParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.multiplicativeExpression()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSLParser.PLUS or _la==BSLParser.MINUS:
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==BSLParser.PLUS or _la==BSLParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.multiplicativeExpression()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(BSLParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.MULT)
            else:
                return self.getToken(BSLParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.DIV)
            else:
                return self.getToken(BSLParser.DIV, i)

        def getRuleIndex(self):
            return BSLParser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = BSLParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.unaryExpression()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSLParser.MULT or _la==BSLParser.DIV:
                self.state = 254
                _la = self._input.LA(1)
                if not(_la==BSLParser.MULT or _la==BSLParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.unaryExpression()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(BSLParser.PrimaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(BSLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BSLParser.MINUS, 0)

        def NOT(self):
            return self.getToken(BSLParser.NOT, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_unaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = BSLParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.NOT) | (1 << BSLParser.PLUS) | (1 << BSLParser.MINUS))) != 0):
                self.state = 261
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.NOT) | (1 << BSLParser.PLUS) | (1 << BSLParser.MINUS))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 264
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BSLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BSLParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(BSLParser.ExpressionContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(BSLParser.CallStatementContext,0)


        def getRuleIndex(self):
            return BSLParser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = BSLParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primaryExpression)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(BSLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(BSLParser.T__1)
                self.state = 269
                self.expression()
                self.state = 270
                self.match(BSLParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.callStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(BSLParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(BSLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BSLParser.FALSE, 0)

        def NULL(self):
            return self.getToken(BSLParser.NULL, 0)

        def UNDEFINED(self):
            return self.getToken(BSLParser.UNDEFINED, 0)

        def getRuleIndex(self):
            return BSLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BSLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSLParser.TRUE) | (1 << BSLParser.FALSE) | (1 << BSLParser.NULL) | (1 << BSLParser.UNDEFINED) | (1 << BSLParser.STRING) | (1 << BSLParser.NUMBER))) != 0)):
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





