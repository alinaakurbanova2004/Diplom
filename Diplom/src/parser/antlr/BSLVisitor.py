# Generated from C:/Diplom/Diplom/src/parser/BSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BSLParser import BSLParser
else:
    from BSLParser import BSLParser

# This class defines a complete generic visitor for a parse tree produced by BSLParser.

class BSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BSLParser#file.
    def visitFile(self, ctx:BSLParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#moduleDeclaration.
    def visitModuleDeclaration(self, ctx:BSLParser.ModuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:BSLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#procedure.
    def visitProcedure(self, ctx:BSLParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#function.
    def visitFunction(self, ctx:BSLParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#parameterList.
    def visitParameterList(self, ctx:BSLParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#statement.
    def visitStatement(self, ctx:BSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#assignment.
    def visitAssignment(self, ctx:BSLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#ifStatement.
    def visitIfStatement(self, ctx:BSLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#returnStatement.
    def visitReturnStatement(self, ctx:BSLParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#argumentList.
    def visitArgumentList(self, ctx:BSLParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#callStatement.
    def visitCallStatement(self, ctx:BSLParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#expression.
    def visitExpression(self, ctx:BSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:BSLParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:BSLParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:BSLParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:BSLParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:BSLParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#unaryExpression.
    def visitUnaryExpression(self, ctx:BSLParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:BSLParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLParser#literal.
    def visitLiteral(self, ctx:BSLParser.LiteralContext):
        return self.visitChildren(ctx)



del BSLParser