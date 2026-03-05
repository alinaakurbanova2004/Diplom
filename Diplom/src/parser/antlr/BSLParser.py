# Generated from C:/Diplom/Diplom/src/parser/BSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,270,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,5,0,53,8,0,10,
        0,12,0,56,9,0,1,0,1,0,1,1,1,1,1,1,3,1,63,8,1,1,1,1,1,1,2,1,2,1,2,
        3,2,70,8,2,1,2,1,2,1,3,1,3,1,3,3,3,77,8,3,1,3,5,3,80,8,3,10,3,12,
        3,83,9,3,1,3,1,3,3,3,87,8,3,1,4,1,4,1,4,3,4,92,8,4,1,4,5,4,95,8,
        4,10,4,12,4,98,9,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,5,5,108,8,
        5,10,5,12,5,111,9,5,3,5,113,8,5,1,5,1,5,1,6,3,6,118,8,6,1,6,1,6,
        1,6,3,6,123,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,131,8,7,1,8,1,8,1,8,
        1,8,3,8,137,8,8,1,9,1,9,1,9,1,9,5,9,143,8,9,10,9,12,9,146,9,9,1,
        9,1,9,5,9,150,8,9,10,9,12,9,153,9,9,3,9,155,8,9,1,9,1,9,3,9,159,
        8,9,1,10,1,10,3,10,163,8,10,1,10,3,10,166,8,10,1,11,1,11,1,11,5,
        11,171,8,11,10,11,12,11,174,9,11,1,12,1,12,1,12,3,12,179,8,12,1,
        12,1,12,3,12,183,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,195,8,14,10,14,12,14,198,9,14,1,14,1,14,3,14,202,8,
        14,1,15,1,15,1,15,1,15,5,15,208,8,15,10,15,12,15,211,9,15,1,15,1,
        15,3,15,215,8,15,1,16,1,16,1,16,5,16,220,8,16,10,16,12,16,223,9,
        16,1,17,1,17,1,17,5,17,228,8,17,10,17,12,17,231,9,17,1,18,1,18,1,
        18,3,18,236,8,18,1,19,1,19,1,19,5,19,241,8,19,10,19,12,19,244,9,
        19,1,20,1,20,1,20,5,20,249,8,20,10,20,12,20,252,9,20,1,21,3,21,255,
        8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,266,8,22,
        1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,0,5,1,0,34,39,1,0,30,31,1,0,32,33,1,0,29,
        31,2,0,23,26,41,42,289,0,54,1,0,0,0,2,59,1,0,0,0,4,66,1,0,0,0,6,
        73,1,0,0,0,8,88,1,0,0,0,10,103,1,0,0,0,12,117,1,0,0,0,14,130,1,0,
        0,0,16,132,1,0,0,0,18,138,1,0,0,0,20,160,1,0,0,0,22,167,1,0,0,0,
        24,175,1,0,0,0,26,184,1,0,0,0,28,186,1,0,0,0,30,203,1,0,0,0,32,216,
        1,0,0,0,34,224,1,0,0,0,36,232,1,0,0,0,38,237,1,0,0,0,40,245,1,0,
        0,0,42,254,1,0,0,0,44,265,1,0,0,0,46,267,1,0,0,0,48,53,3,2,1,0,49,
        53,3,4,2,0,50,53,3,6,3,0,51,53,3,8,4,0,52,48,1,0,0,0,52,49,1,0,0,
        0,52,50,1,0,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,5,0,0,1,58,1,1,0,0,0,59,
        60,5,6,0,0,60,62,5,40,0,0,61,63,5,7,0,0,62,61,1,0,0,0,62,63,1,0,
        0,0,63,64,1,0,0,0,64,65,5,1,0,0,65,3,1,0,0,0,66,67,5,6,0,0,67,69,
        5,40,0,0,68,70,5,7,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,
        71,72,5,1,0,0,72,5,1,0,0,0,73,74,5,8,0,0,74,76,5,40,0,0,75,77,3,
        10,5,0,76,75,1,0,0,0,76,77,1,0,0,0,77,81,1,0,0,0,78,80,3,14,7,0,
        79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,
        0,0,0,83,81,1,0,0,0,84,86,5,9,0,0,85,87,5,1,0,0,86,85,1,0,0,0,86,
        87,1,0,0,0,87,7,1,0,0,0,88,89,5,10,0,0,89,91,5,40,0,0,90,92,3,10,
        5,0,91,90,1,0,0,0,91,92,1,0,0,0,92,96,1,0,0,0,93,95,3,14,7,0,94,
        93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,
        0,98,96,1,0,0,0,99,101,5,11,0,0,100,102,5,1,0,0,101,100,1,0,0,0,
        101,102,1,0,0,0,102,9,1,0,0,0,103,112,5,2,0,0,104,109,3,12,6,0,105,
        106,5,3,0,0,106,108,3,12,6,0,107,105,1,0,0,0,108,111,1,0,0,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,112,
        104,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,4,0,0,115,
        11,1,0,0,0,116,118,5,5,0,0,117,116,1,0,0,0,117,118,1,0,0,0,118,119,
        1,0,0,0,119,122,5,40,0,0,120,121,5,38,0,0,121,123,3,26,13,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,13,1,0,0,0,124,131,3,16,8,0,125,
        131,3,18,9,0,126,131,3,28,14,0,127,131,3,30,15,0,128,131,3,20,10,
        0,129,131,3,24,12,0,130,124,1,0,0,0,130,125,1,0,0,0,130,126,1,0,
        0,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,15,1,0,0,
        0,132,133,5,40,0,0,133,134,5,38,0,0,134,136,3,26,13,0,135,137,5,
        1,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,17,1,0,0,0,138,139,5,12,
        0,0,139,140,3,26,13,0,140,144,5,13,0,0,141,143,3,14,7,0,142,141,
        1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,154,
        1,0,0,0,146,144,1,0,0,0,147,151,5,15,0,0,148,150,3,14,7,0,149,148,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,155,
        1,0,0,0,153,151,1,0,0,0,154,147,1,0,0,0,154,155,1,0,0,0,155,156,
        1,0,0,0,156,158,5,16,0,0,157,159,5,1,0,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,19,1,0,0,0,160,162,5,22,0,0,161,163,3,26,13,0,162,161,
        1,0,0,0,162,163,1,0,0,0,163,165,1,0,0,0,164,166,5,1,0,0,165,164,
        1,0,0,0,165,166,1,0,0,0,166,21,1,0,0,0,167,172,3,26,13,0,168,169,
        5,3,0,0,169,171,3,26,13,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,
        1,0,0,0,172,173,1,0,0,0,173,23,1,0,0,0,174,172,1,0,0,0,175,176,5,
        40,0,0,176,178,5,2,0,0,177,179,3,22,11,0,178,177,1,0,0,0,178,179,
        1,0,0,0,179,180,1,0,0,0,180,182,5,4,0,0,181,183,5,1,0,0,182,181,
        1,0,0,0,182,183,1,0,0,0,183,25,1,0,0,0,184,185,3,32,16,0,185,27,
        1,0,0,0,186,187,5,17,0,0,187,188,5,40,0,0,188,189,5,38,0,0,189,190,
        3,26,13,0,190,191,5,18,0,0,191,192,3,26,13,0,192,196,5,20,0,0,193,
        195,3,14,7,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,
        197,1,0,0,0,197,199,1,0,0,0,198,196,1,0,0,0,199,201,5,21,0,0,200,
        202,5,1,0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,29,1,0,0,0,203,204,
        5,19,0,0,204,205,3,26,13,0,205,209,5,20,0,0,206,208,3,14,7,0,207,
        206,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,
        212,1,0,0,0,211,209,1,0,0,0,212,214,5,21,0,0,213,215,5,1,0,0,214,
        213,1,0,0,0,214,215,1,0,0,0,215,31,1,0,0,0,216,221,3,34,17,0,217,
        218,5,28,0,0,218,220,3,34,17,0,219,217,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,221,222,1,0,0,0,222,33,1,0,0,0,223,221,1,0,0,0,224,229,
        3,36,18,0,225,226,5,27,0,0,226,228,3,36,18,0,227,225,1,0,0,0,228,
        231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,35,1,0,0,0,231,229,
        1,0,0,0,232,235,3,38,19,0,233,234,7,0,0,0,234,236,3,38,19,0,235,
        233,1,0,0,0,235,236,1,0,0,0,236,37,1,0,0,0,237,242,3,40,20,0,238,
        239,7,1,0,0,239,241,3,40,20,0,240,238,1,0,0,0,241,244,1,0,0,0,242,
        240,1,0,0,0,242,243,1,0,0,0,243,39,1,0,0,0,244,242,1,0,0,0,245,250,
        3,42,21,0,246,247,7,2,0,0,247,249,3,42,21,0,248,246,1,0,0,0,249,
        252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,41,1,0,0,0,252,250,
        1,0,0,0,253,255,7,3,0,0,254,253,1,0,0,0,254,255,1,0,0,0,255,256,
        1,0,0,0,256,257,3,44,22,0,257,43,1,0,0,0,258,266,3,46,23,0,259,266,
        5,40,0,0,260,261,5,2,0,0,261,262,3,26,13,0,262,263,5,4,0,0,263,266,
        1,0,0,0,264,266,3,24,12,0,265,258,1,0,0,0,265,259,1,0,0,0,265,260,
        1,0,0,0,265,264,1,0,0,0,266,45,1,0,0,0,267,268,7,4,0,0,268,47,1,
        0,0,0,36,52,54,62,69,76,81,86,91,96,101,109,112,117,122,130,136,
        144,151,154,158,162,165,172,178,182,196,201,209,214,221,229,235,
        242,250,254,265
    ]

class BSLParser ( Parser ):

    grammarFileName = "BSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'\\u0417\\u043D\\u0430\\u0447'", 
                     "'\\u041F\\u0435\\u0440\\u0435\\u043C'", "'\\u042D\\u043A\\u0441\\u043F\\u043E\\u0440\\u0442'", 
                     "'\\u041F\\u0440\\u043E\\u0446\\u0435\\u0434\\u0443\\u0440\\u0430'", 
                     "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u041F\\u0440\\u043E\\u0446\\u0435\\u0434\\u0443\\u0440\\u044B'", 
                     "'\\u0424\\u0443\\u043D\\u043A\\u0446\\u0438\\u044F'", 
                     "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0424\\u0443\\u043D\\u043A\\u0446\\u0438\\u0438'", 
                     "'\\u0415\\u0441\\u043B\\u0438'", "'\\u0422\\u043E\\u0433\\u0434\\u0430'", 
                     "'\\u0418\\u043D\\u0430\\u0447\\u0435\\u0415\\u0441\\u043B\\u0438'", 
                     "'\\u0418\\u043D\\u0430\\u0447\\u0435'", "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0415\\u0441\\u043B\\u0438'", 
                     "'\\u0414\\u043B\\u044F'", "'\\u041F\\u043E'", "'\\u041F\\u043E\\u043A\\u0430'", 
                     "'\\u0426\\u0438\\u043A\\u043B'", "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0426\\u0438\\u043A\\u043B\\u0430'", 
                     "'\\u0412\\u043E\\u0437\\u0432\\u0440\\u0430\\u0442'", 
                     "'\\u0418\\u0441\\u0442\\u0438\\u043D\\u0430'", "'\\u041B\\u043E\\u0436\\u044C'", 
                     "'Null'", "'Undefined'", "'\\u0418'", "'\\u0418\\u041B\\u0418'", 
                     "'\\u041D\\u0415'", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'<='", "'>'", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PEREM", "EXPORT", "PROCEDURE", 
                      "END_PROCEDURE", "FUNCTION", "END_FUNCTION", "IF", 
                      "THEN", "ELSE_IF", "ELSE", "END_IF", "FOR", "TO", 
                      "WHILE", "LOOP", "END_LOOP", "RETURN", "TRUE", "FALSE", 
                      "NULL", "UNDEFINED", "AND", "OR", "NOT", "PLUS", "MINUS", 
                      "MULT", "DIV", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", "ID", "STRING", 
                      "NUMBER", "WS", "COMMENT" ]

    RULE_file = 0
    RULE_moduleDeclaration = 1
    RULE_variableDeclaration = 2
    RULE_procedure = 3
    RULE_function = 4
    RULE_parameterList = 5
    RULE_parameter = 6
    RULE_statement = 7
    RULE_assignment = 8
    RULE_ifStatement = 9
    RULE_returnStatement = 10
    RULE_argumentList = 11
    RULE_callStatement = 12
    RULE_expression = 13
    RULE_forStatement = 14
    RULE_whileStatement = 15
    RULE_logicalOrExpression = 16
    RULE_logicalAndExpression = 17
    RULE_comparisonExpression = 18
    RULE_additiveExpression = 19
    RULE_multiplicativeExpression = 20
    RULE_unaryExpression = 21
    RULE_primaryExpression = 22
    RULE_literal = 23

    ruleNames =  [ "file", "moduleDeclaration", "variableDeclaration", "procedure", 
                   "function", "parameterList", "parameter", "statement", 
                   "assignment", "ifStatement", "returnStatement", "argumentList", 
                   "callStatement", "expression", "forStatement", "whileStatement", 
                   "logicalOrExpression", "logicalAndExpression", "comparisonExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "primaryExpression", "literal" ]

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
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    LESS=34
    LESS_OR_EQUAL=35
    GREATER=36
    GREATER_OR_EQUAL=37
    EQUAL=38
    NOT_EQUAL=39
    ID=40
    STRING=41
    NUMBER=42
    WS=43
    COMMENT=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BSLParser.EOF, 0)

        def moduleDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.ModuleDeclarationContext)
            else:
                return self.getTypedRuleContext(BSLParser.ModuleDeclarationContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(BSLParser.VariableDeclarationContext,i)


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
            return BSLParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = BSLParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1344) != 0):
                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.moduleDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.variableDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.procedure()
                    pass

                elif la_ == 4:
                    self.state = 51
                    self.function()
                    pass


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(BSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDeclarationContext(ParserRuleContext):
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
            return BSLParser.RULE_moduleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDeclaration" ):
                listener.enterModuleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDeclaration" ):
                listener.exitModuleDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleDeclaration" ):
                return visitor.visitModuleDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def moduleDeclaration(self):

        localctx = BSLParser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_moduleDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(BSLParser.PEREM)
            self.state = 60
            self.match(BSLParser.ID)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 61
                self.match(BSLParser.EXPORT)


            self.state = 64
            self.match(BSLParser.T__0)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

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
            self.state = 66
            self.match(BSLParser.PEREM)
            self.state = 67
            self.match(BSLParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 68
                self.match(BSLParser.EXPORT)


            self.state = 71
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

        def parameterList(self):
            return self.getTypedRuleContext(BSLParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_procedure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure" ):
                listener.enterProcedure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure" ):
                listener.exitProcedure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = BSLParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_procedure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(BSLParser.PROCEDURE)
            self.state = 74
            self.match(BSLParser.ID)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 75
                self.parameterList()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(BSLParser.END_PROCEDURE)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 85
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

        def parameterList(self):
            return self.getTypedRuleContext(BSLParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BSLParser.StatementContext,i)


        def getRuleIndex(self):
            return BSLParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = BSLParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(BSLParser.FUNCTION)
            self.state = 89
            self.match(BSLParser.ID)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 90
                self.parameterList()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                self.state = 93
                self.statement()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(BSLParser.END_FUNCTION)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 100
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = BSLParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BSLParser.T__1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5 or _la==40:
                self.state = 104
                self.parameter()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 105
                    self.match(BSLParser.T__2)
                    self.state = 106
                    self.parameter()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 114
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BSLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 116
                self.match(BSLParser.T__4)


            self.state = 119
            self.match(BSLParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 120
                self.match(BSLParser.EQUAL)
                self.state = 121
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


        def getRuleIndex(self):
            return BSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.callStatement()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BSLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BSLParser.ID)
            self.state = 133
            self.match(BSLParser.EQUAL)
            self.state = 134
            self.expression()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 135
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BSLParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BSLParser.IF)
            self.state = 139
            self.expression()
            self.state = 140
            self.match(BSLParser.THEN)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                self.state = 141
                self.statement()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 147
                self.match(BSLParser.ELSE)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                    self.state = 148
                    self.statement()
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 156
            self.match(BSLParser.END_IF)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 157
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BSLParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BSLParser.RETURN)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 161
                self.expression()


            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 164
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = BSLParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.expression()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 168
                self.match(BSLParser.T__2)
                self.state = 169
                self.expression()
                self.state = 174
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallStatement" ):
                listener.enterCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallStatement" ):
                listener.exitCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = BSLParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(BSLParser.ID)
            self.state = 176
            self.match(BSLParser.T__1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7700465319940) != 0):
                self.state = 177
                self.argumentList()


            self.state = 180
            self.match(BSLParser.T__3)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 181
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = BSLParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BSLParser.FOR)
            self.state = 187
            self.match(BSLParser.ID)
            self.state = 188
            self.match(BSLParser.EQUAL)
            self.state = 189
            self.expression()
            self.state = 190
            self.match(BSLParser.TO)
            self.state = 191
            self.expression()
            self.state = 192
            self.match(BSLParser.LOOP)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                self.state = 193
                self.statement()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(BSLParser.END_LOOP)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 200
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BSLParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BSLParser.WHILE)
            self.state = 204
            self.expression()
            self.state = 205
            self.match(BSLParser.LOOP)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099516481536) != 0):
                self.state = 206
                self.statement()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(BSLParser.END_LOOP)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 213
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = BSLParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.logicalAndExpression()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 217
                self.match(BSLParser.OR)
                self.state = 218
                self.logicalAndExpression()
                self.state = 223
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = BSLParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.comparisonExpression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 225
                self.match(BSLParser.AND)
                self.state = 226
                self.comparisonExpression()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpression" ):
                listener.enterComparisonExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpression" ):
                listener.exitComparisonExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = BSLParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparisonExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.additiveExpression()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0):
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = BSLParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.multiplicativeExpression()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.multiplicativeExpression()
                self.state = 244
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = BSLParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.unaryExpression()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.unaryExpression()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = BSLParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                self.state = 253
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 256
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = BSLParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primaryExpression)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(BSLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(BSLParser.T__1)
                self.state = 261
                self.expression()
                self.state = 262
                self.match(BSLParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BSLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6597195595776) != 0)):
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





