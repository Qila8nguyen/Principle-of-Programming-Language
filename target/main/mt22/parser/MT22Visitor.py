# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_decl.
    def visitArray_decl(self, ctx:MT22Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimen.
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomictype.
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_full.
    def visitVar_decl_full(self, ctx:MT22Parser.Var_decl_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_nullable_list.
    def visitVar_decl_nullable_list(self, ctx:MT22Parser.Var_decl_nullable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier.
    def visitIdentifier(self, ctx:MT22Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl_type.
    def visitDecl_type(self, ctx:MT22Parser.Decl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_decl.
    def visitParameter_decl(self, ctx:MT22Parser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_decl.
    def visitFunction_decl(self, ctx:MT22Parser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterdecl_list.
    def visitParameterdecl_list(self, ctx:MT22Parser.Parameterdecl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterdecl_nullable_list.
    def visitParameterdecl_nullable_list(self, ctx:MT22Parser.Parameterdecl_nullable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_param.
    def visitParam_param(self, ctx:MT22Parser.Param_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherit_parent_function_nullable.
    def visitInherit_parent_function_nullable(self, ctx:MT22Parser.Inherit_parent_function_nullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_body.
    def visitFunction_body(self, ctx:MT22Parser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_decl_type.
    def visitFunction_decl_type(self, ctx:MT22Parser.Function_decl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_logical.
    def visitExpr_logical(self, ctx:MT22Parser.Expr_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_adding.
    def visitExpr_adding(self, ctx:MT22Parser.Expr_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_multiplying.
    def visitExpr_multiplying(self, ctx:MT22Parser.Expr_multiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_notlogical.
    def visitExpr_notlogical(self, ctx:MT22Parser.Expr_notlogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_term.
    def visitExpr_term(self, ctx:MT22Parser.Expr_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_indexop.
    def visitExpr_indexop(self, ctx:MT22Parser.Expr_indexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_nullable_list.
    def visitExpression_nullable_list(self, ctx:MT22Parser.Expression_nullable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprime.
    def visitExprime(self, ctx:MT22Parser.ExprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_stmt.
    def visitElse_stmt(self, ctx:MT22Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_nullable_list.
    def visitStmt_nullable_list(self, ctx:MT22Parser.Stmt_nullable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_nullable.
    def visitExpression_nullable(self, ctx:MT22Parser.Expression_nullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body.
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        return self.visitChildren(ctx)



del MT22Parser