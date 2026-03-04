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
        4,1,41,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,0,1,0,1,1,1,1,
        1,1,3,1,57,8,1,1,1,1,1,1,2,1,2,1,2,3,2,64,8,2,1,2,1,2,1,3,1,3,1,
        3,3,3,71,8,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,1,3,3,3,81,8,3,
        1,4,1,4,1,4,3,4,86,8,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,4,1,4,3,
        4,96,8,4,1,5,1,5,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,3,5,107,8,
        5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,115,8,6,1,7,1,7,1,7,1,7,3,7,121,8,
        7,1,8,1,8,1,8,1,8,5,8,127,8,8,10,8,12,8,130,9,8,1,8,1,8,5,8,134,
        8,8,10,8,12,8,137,9,8,3,8,139,8,8,1,8,1,8,3,8,143,8,8,1,9,1,9,3,
        9,147,8,9,1,9,3,9,150,8,9,1,10,1,10,1,10,5,10,155,8,10,10,10,12,
        10,158,9,10,1,11,1,11,1,11,3,11,163,8,11,1,11,1,11,3,11,167,8,11,
        1,12,1,12,1,13,1,13,1,13,5,13,174,8,13,10,13,12,13,177,9,13,1,14,
        1,14,1,14,5,14,182,8,14,10,14,12,14,185,9,14,1,15,1,15,1,15,3,15,
        190,8,15,1,16,1,16,1,16,5,16,195,8,16,10,16,12,16,198,9,16,1,17,
        1,17,1,17,5,17,203,8,17,10,17,12,17,206,9,17,1,18,3,18,209,8,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,220,8,19,1,20,
        1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,0,5,1,0,31,36,1,0,27,28,1,0,29,30,1,0,26,28,2,0,20,23,38,
        39,238,0,48,1,0,0,0,2,53,1,0,0,0,4,60,1,0,0,0,6,67,1,0,0,0,8,82,
        1,0,0,0,10,97,1,0,0,0,12,114,1,0,0,0,14,116,1,0,0,0,16,122,1,0,0,
        0,18,144,1,0,0,0,20,151,1,0,0,0,22,159,1,0,0,0,24,168,1,0,0,0,26,
        170,1,0,0,0,28,178,1,0,0,0,30,186,1,0,0,0,32,191,1,0,0,0,34,199,
        1,0,0,0,36,208,1,0,0,0,38,219,1,0,0,0,40,221,1,0,0,0,42,47,3,2,1,
        0,43,47,3,4,2,0,44,47,3,6,3,0,45,47,3,8,4,0,46,42,1,0,0,0,46,43,
        1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,0,0,1,52,1,1,0,
        0,0,53,54,5,5,0,0,54,56,5,37,0,0,55,57,5,6,0,0,56,55,1,0,0,0,56,
        57,1,0,0,0,57,58,1,0,0,0,58,59,5,1,0,0,59,3,1,0,0,0,60,61,5,5,0,
        0,61,63,5,37,0,0,62,64,5,6,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,
        1,0,0,0,65,66,5,1,0,0,66,5,1,0,0,0,67,68,5,7,0,0,68,70,5,37,0,0,
        69,71,3,10,5,0,70,69,1,0,0,0,70,71,1,0,0,0,71,75,1,0,0,0,72,74,3,
        12,6,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,
        78,1,0,0,0,77,75,1,0,0,0,78,80,5,8,0,0,79,81,5,1,0,0,80,79,1,0,0,
        0,80,81,1,0,0,0,81,7,1,0,0,0,82,83,5,9,0,0,83,85,5,37,0,0,84,86,
        3,10,5,0,85,84,1,0,0,0,85,86,1,0,0,0,86,90,1,0,0,0,87,89,3,12,6,
        0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,
        1,0,0,0,92,90,1,0,0,0,93,95,5,10,0,0,94,96,5,1,0,0,95,94,1,0,0,0,
        95,96,1,0,0,0,96,9,1,0,0,0,97,106,5,2,0,0,98,103,5,37,0,0,99,100,
        5,3,0,0,100,102,5,37,0,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,
        1,0,0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,106,98,1,
        0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,4,0,0,109,11,1,0,
        0,0,110,115,3,14,7,0,111,115,3,16,8,0,112,115,3,18,9,0,113,115,3,
        22,11,0,114,110,1,0,0,0,114,111,1,0,0,0,114,112,1,0,0,0,114,113,
        1,0,0,0,115,13,1,0,0,0,116,117,5,37,0,0,117,118,5,35,0,0,118,120,
        3,24,12,0,119,121,5,1,0,0,120,119,1,0,0,0,120,121,1,0,0,0,121,15,
        1,0,0,0,122,123,5,11,0,0,123,124,3,24,12,0,124,128,5,12,0,0,125,
        127,3,12,6,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,
        129,1,0,0,0,129,138,1,0,0,0,130,128,1,0,0,0,131,135,5,14,0,0,132,
        134,3,12,6,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,
        136,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,138,131,1,0,0,0,138,
        139,1,0,0,0,139,140,1,0,0,0,140,142,5,15,0,0,141,143,5,1,0,0,142,
        141,1,0,0,0,142,143,1,0,0,0,143,17,1,0,0,0,144,146,5,19,0,0,145,
        147,3,24,12,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,
        150,5,1,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,19,1,0,0,0,151,156,
        3,24,12,0,152,153,5,3,0,0,153,155,3,24,12,0,154,152,1,0,0,0,155,
        158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,21,1,0,0,0,158,156,
        1,0,0,0,159,160,5,37,0,0,160,162,5,2,0,0,161,163,3,20,10,0,162,161,
        1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,166,5,4,0,0,165,167,
        5,1,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,23,1,0,0,0,168,169,3,
        26,13,0,169,25,1,0,0,0,170,175,3,28,14,0,171,172,5,25,0,0,172,174,
        3,28,14,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,27,1,0,0,0,177,175,1,0,0,0,178,183,3,30,15,0,179,180,
        5,24,0,0,180,182,3,30,15,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,29,1,0,0,0,185,183,1,0,0,0,186,189,3,
        32,16,0,187,188,7,0,0,0,188,190,3,32,16,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,31,1,0,0,0,191,196,3,34,17,0,192,193,7,1,0,0,193,195,
        3,34,17,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,33,1,0,0,0,198,196,1,0,0,0,199,204,3,36,18,0,200,201,
        7,2,0,0,201,203,3,36,18,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,35,1,0,0,0,206,204,1,0,0,0,207,209,7,
        3,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,211,3,
        38,19,0,211,37,1,0,0,0,212,220,3,40,20,0,213,220,5,37,0,0,214,215,
        5,2,0,0,215,216,3,24,12,0,216,217,5,4,0,0,217,220,1,0,0,0,218,220,
        3,22,11,0,219,212,1,0,0,0,219,213,1,0,0,0,219,214,1,0,0,0,219,218,
        1,0,0,0,220,39,1,0,0,0,221,222,7,4,0,0,222,41,1,0,0,0,30,46,48,56,
        63,70,75,80,85,90,95,103,106,114,120,128,135,138,142,146,149,156,
        162,166,175,183,189,196,204,208,219
    ]

class BSLParser ( Parser ):

    grammarFileName = "BSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'\\u041F\\u0435\\u0440\\u0435\\u043C'", 
                     "'\\u042D\\u043A\\u0441\\u043F\\u043E\\u0440\\u0442'", 
                     "'\\u041F\\u0440\\u043E\\u0446\\u0435\\u0434\\u0443\\u0440\\u0430'", 
                     "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u041F\\u0440\\u043E\\u0446\\u0435\\u0434\\u0443\\u0440\\u044B'", 
                     "'\\u0424\\u0443\\u043D\\u043A\\u0446\\u0438\\u044F'", 
                     "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0424\\u0443\\u043D\\u043A\\u0446\\u0438\\u0438'", 
                     "'\\u0415\\u0441\\u043B\\u0438'", "'\\u0422\\u043E\\u0433\\u0434\\u0430'", 
                     "'\\u0418\\u043D\\u0430\\u0447\\u0435\\u0415\\u0441\\u043B\\u0438'", 
                     "'\\u0418\\u043D\\u0430\\u0447\\u0435'", "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0415\\u0441\\u043B\\u0438'", 
                     "'\\u041F\\u043E\\u043A\\u0430'", "'\\u0426\\u0438\\u043A\\u043B'", 
                     "'\\u041A\\u043E\\u043D\\u0435\\u0446\\u0426\\u0438\\u043A\\u043B\\u0430'", 
                     "'\\u0412\\u043E\\u0437\\u0432\\u0440\\u0430\\u0442'", 
                     "'\\u0418\\u0441\\u0442\\u0438\\u043D\\u0430'", "'\\u041B\\u043E\\u0436\\u044C'", 
                     "'Null'", "'Undefined'", "'\\u0418'", "'\\u0418\\u041B\\u0418'", 
                     "'\\u041D\\u0415'", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'<='", "'>'", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PEREM", "EXPORT", "PROCEDURE", "END_PROCEDURE", 
                      "FUNCTION", "END_FUNCTION", "IF", "THEN", "ELSE_IF", 
                      "ELSE", "END_IF", "WHILE", "LOOP", "END_LOOP", "RETURN", 
                      "TRUE", "FALSE", "NULL", "UNDEFINED", "AND", "OR", 
                      "NOT", "PLUS", "MINUS", "MULT", "DIV", "LESS", "LESS_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", 
                      "ID", "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_file = 0
    RULE_moduleDeclaration = 1
    RULE_variableDeclaration = 2
    RULE_procedure = 3
    RULE_function = 4
    RULE_parameterList = 5
    RULE_statement = 6
    RULE_assignment = 7
    RULE_ifStatement = 8
    RULE_returnStatement = 9
    RULE_argumentList = 10
    RULE_callStatement = 11
    RULE_expression = 12
    RULE_logicalOrExpression = 13
    RULE_logicalAndExpression = 14
    RULE_comparisonExpression = 15
    RULE_additiveExpression = 16
    RULE_multiplicativeExpression = 17
    RULE_unaryExpression = 18
    RULE_primaryExpression = 19
    RULE_literal = 20

    ruleNames =  [ "file", "moduleDeclaration", "variableDeclaration", "procedure", 
                   "function", "parameterList", "statement", "assignment", 
                   "ifStatement", "returnStatement", "argumentList", "callStatement", 
                   "expression", "logicalOrExpression", "logicalAndExpression", 
                   "comparisonExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PEREM=5
    EXPORT=6
    PROCEDURE=7
    END_PROCEDURE=8
    FUNCTION=9
    END_FUNCTION=10
    IF=11
    THEN=12
    ELSE_IF=13
    ELSE=14
    END_IF=15
    WHILE=16
    LOOP=17
    END_LOOP=18
    RETURN=19
    TRUE=20
    FALSE=21
    NULL=22
    UNDEFINED=23
    AND=24
    OR=25
    NOT=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    LESS=31
    LESS_OR_EQUAL=32
    GREATER=33
    GREATER_OR_EQUAL=34
    EQUAL=35
    NOT_EQUAL=36
    ID=37
    STRING=38
    NUMBER=39
    WS=40
    COMMENT=41

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
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 672) != 0):
                self.state = 46
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.moduleDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 43
                    self.variableDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 44
                    self.procedure()
                    pass

                elif la_ == 4:
                    self.state = 45
                    self.function()
                    pass


                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.state = 53
            self.match(BSLParser.PEREM)
            self.state = 54
            self.match(BSLParser.ID)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 55
                self.match(BSLParser.EXPORT)


            self.state = 58
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
            self.state = 60
            self.match(BSLParser.PEREM)
            self.state = 61
            self.match(BSLParser.ID)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 62
                self.match(BSLParser.EXPORT)


            self.state = 65
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
            self.state = 67
            self.match(BSLParser.PROCEDURE)
            self.state = 68
            self.match(BSLParser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 69
                self.parameterList()


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439479808) != 0):
                self.state = 72
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(BSLParser.END_PROCEDURE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 79
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
            self.state = 82
            self.match(BSLParser.FUNCTION)
            self.state = 83
            self.match(BSLParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 84
                self.parameterList()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439479808) != 0):
                self.state = 87
                self.statement()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(BSLParser.END_FUNCTION)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 94
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BSLParser.ID)
            else:
                return self.getToken(BSLParser.ID, i)

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
            self.state = 97
            self.match(BSLParser.T__1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 98
                self.match(BSLParser.ID)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 99
                    self.match(BSLParser.T__2)
                    self.state = 100
                    self.match(BSLParser.ID)
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 108
            self.match(BSLParser.T__3)
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
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
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
        self.enterRule(localctx, 14, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(BSLParser.ID)
            self.state = 117
            self.match(BSLParser.EQUAL)
            self.state = 118
            self.expression()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 119
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
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(BSLParser.IF)
            self.state = 123
            self.expression()
            self.state = 124
            self.match(BSLParser.THEN)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439479808) != 0):
                self.state = 125
                self.statement()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 131
                self.match(BSLParser.ELSE)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137439479808) != 0):
                    self.state = 132
                    self.statement()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 140
            self.match(BSLParser.END_IF)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 141
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
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BSLParser.RETURN)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 145
                self.expression()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 148
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
        self.enterRule(localctx, 20, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.expression()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 152
                self.match(BSLParser.T__2)
                self.state = 153
                self.expression()
                self.state = 158
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
        self.enterRule(localctx, 22, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BSLParser.ID)
            self.state = 160
            self.match(BSLParser.T__1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 962558164996) != 0):
                self.state = 161
                self.argumentList()


            self.state = 164
            self.match(BSLParser.T__3)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 165
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
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.logicalOrExpression()
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
        self.enterRule(localctx, 26, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.logicalAndExpression()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 171
                self.match(BSLParser.OR)
                self.state = 172
                self.logicalAndExpression()
                self.state = 177
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
        self.enterRule(localctx, 28, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.comparisonExpression()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 179
                self.match(BSLParser.AND)
                self.state = 180
                self.comparisonExpression()
                self.state = 185
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
        self.enterRule(localctx, 30, self.RULE_comparisonExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.additiveExpression()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0):
                self.state = 187
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
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
        self.enterRule(localctx, 32, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.multiplicativeExpression()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 192
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self.multiplicativeExpression()
                self.state = 198
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
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.unaryExpression()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 200
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 201
                self.unaryExpression()
                self.state = 206
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
        self.enterRule(localctx, 36, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 210
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
        self.enterRule(localctx, 38, self.RULE_primaryExpression)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BSLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(BSLParser.T__1)
                self.state = 215
                self.expression()
                self.state = 216
                self.match(BSLParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 218
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
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 824649449472) != 0)):
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





