# Generated from C:/Diplom/Diplom/src/parser/BSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BSLParser import BSLParser
else:
    from BSLParser import BSLParser

# This class defines a complete listener for a parse tree produced by BSLParser.
class BSLListener(ParseTreeListener):

    # Enter a parse tree produced by BSLParser#file.
    def enterFile(self, ctx:BSLParser.FileContext):
        pass

    # Exit a parse tree produced by BSLParser#file.
    def exitFile(self, ctx:BSLParser.FileContext):
        pass


    # Enter a parse tree produced by BSLParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:BSLParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by BSLParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:BSLParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by BSLParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:BSLParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by BSLParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:BSLParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by BSLParser#procedure.
    def enterProcedure(self, ctx:BSLParser.ProcedureContext):
        pass

    # Exit a parse tree produced by BSLParser#procedure.
    def exitProcedure(self, ctx:BSLParser.ProcedureContext):
        pass


    # Enter a parse tree produced by BSLParser#function.
    def enterFunction(self, ctx:BSLParser.FunctionContext):
        pass

    # Exit a parse tree produced by BSLParser#function.
    def exitFunction(self, ctx:BSLParser.FunctionContext):
        pass


    # Enter a parse tree produced by BSLParser#parameterList.
    def enterParameterList(self, ctx:BSLParser.ParameterListContext):
        pass

    # Exit a parse tree produced by BSLParser#parameterList.
    def exitParameterList(self, ctx:BSLParser.ParameterListContext):
        pass


    # Enter a parse tree produced by BSLParser#parameter.
    def enterParameter(self, ctx:BSLParser.ParameterContext):
        pass

    # Exit a parse tree produced by BSLParser#parameter.
    def exitParameter(self, ctx:BSLParser.ParameterContext):
        pass


    # Enter a parse tree produced by BSLParser#statement.
    def enterStatement(self, ctx:BSLParser.StatementContext):
        pass

    # Exit a parse tree produced by BSLParser#statement.
    def exitStatement(self, ctx:BSLParser.StatementContext):
        pass


    # Enter a parse tree produced by BSLParser#assignment.
    def enterAssignment(self, ctx:BSLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by BSLParser#assignment.
    def exitAssignment(self, ctx:BSLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by BSLParser#ifStatement.
    def enterIfStatement(self, ctx:BSLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by BSLParser#ifStatement.
    def exitIfStatement(self, ctx:BSLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by BSLParser#returnStatement.
    def enterReturnStatement(self, ctx:BSLParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by BSLParser#returnStatement.
    def exitReturnStatement(self, ctx:BSLParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by BSLParser#argumentList.
    def enterArgumentList(self, ctx:BSLParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by BSLParser#argumentList.
    def exitArgumentList(self, ctx:BSLParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by BSLParser#callStatement.
    def enterCallStatement(self, ctx:BSLParser.CallStatementContext):
        pass

    # Exit a parse tree produced by BSLParser#callStatement.
    def exitCallStatement(self, ctx:BSLParser.CallStatementContext):
        pass


    # Enter a parse tree produced by BSLParser#expression.
    def enterExpression(self, ctx:BSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#expression.
    def exitExpression(self, ctx:BSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#forStatement.
    def enterForStatement(self, ctx:BSLParser.ForStatementContext):
        pass

    # Exit a parse tree produced by BSLParser#forStatement.
    def exitForStatement(self, ctx:BSLParser.ForStatementContext):
        pass


    # Enter a parse tree produced by BSLParser#whileStatement.
    def enterWhileStatement(self, ctx:BSLParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by BSLParser#whileStatement.
    def exitWhileStatement(self, ctx:BSLParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by BSLParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:BSLParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:BSLParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:BSLParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:BSLParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:BSLParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:BSLParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:BSLParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:BSLParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:BSLParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:BSLParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#unaryExpression.
    def enterUnaryExpression(self, ctx:BSLParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#unaryExpression.
    def exitUnaryExpression(self, ctx:BSLParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:BSLParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by BSLParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:BSLParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by BSLParser#literal.
    def enterLiteral(self, ctx:BSLParser.LiteralContext):
        pass

    # Exit a parse tree produced by BSLParser#literal.
    def exitLiteral(self, ctx:BSLParser.LiteralContext):
        pass



del BSLParser