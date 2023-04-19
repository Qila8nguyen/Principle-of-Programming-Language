from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
class ASTGeneration(MT22Visitor):

    # Visit a parse tree produced by MT22Parser#program.
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decl_program()))

    # Visit a parse tree produced by MT22Parser#decl_program.
    def visitDecl_program(self, ctx:MT22Parser.Decl_programContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_program())


    # Visit a parse tree produced by MT22Parser#decl.
    # decl: var_decl | function_decl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        return self.visit(ctx.function_decl())


    # Visit a parse tree produced by MT22Parser#array_decl.
    # array_type_decl: ARRAY LSB dimensions RSB OF atomictype;
    def visitArray_type_decl(self, ctx:MT22Parser.Array_type_declContext):
        dimensionsArr = self.visit(ctx.dimensions())
        typ = self.visit(ctx.atomictype())
        return ArrayType(dimensionsArr, typ)

    # Visit a parse tree produced by MT22Parser#array_literal.
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        exp_list = self.visit(ctx.expression_list())
        return ArrayLit(exp_list)


    # Visit a parse tree produced by MT22Parser#dimensions.
    # dimensions: INTEGER_LITERAL COMMA dimensions | INTEGER_LITERAL;
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.COMMA():
            return [IntegerLit(ctx.INTEGER_LITERAL().getText())] + self.visit(ctx.dimensions())
        return [IntegerLit(ctx.INTEGER_LITERAL().getText())]


    # Visit a parse tree produced by MT22Parser#var_decl.
    #   var_decl: (identifier_list COLON decl_type | var_decl_full) SEMI;

    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        if ctx.COLON():
            id_list = self.visit(ctx.identifier_list())
            typ = self.visit(ctx.decl_type())
            return list(map(lambda id: VarDecl(name = id, typ = typ, init = None), id_list))
        else: 
            id_list, exp_list, typ = self.visit(ctx.var_decl_full())
            return list(map(lambda id, exp: VarDecl(name = id, typ = typ, init = exp), id_list, exp_list))


    # Visit a parse tree produced by MT22Parser#var_decl_full.
    #   var_decl_full:
    # 	IDENTIFIER COMMA var_decl_full COMMA expression
    # 	| IDENTIFIER COLON decl_type ASSIGN expression;
    def visitVar_decl_full(self, ctx:MT22Parser.Var_decl_fullContext):
        id = ctx.IDENTIFIER().getText()
        exp = self.visit(ctx.expression())
        if ctx.COMMA():
            id_sub, exp_sub, typ = self.visit(ctx.var_decl_full())
            id_list = [id] + id_sub
            exp_list = exp_sub + [exp]
            return id_list, exp_list, typ
        else:
            typ2 = self.visit(ctx.decl_type())
            return [id],[exp], str(typ2)



    # Visit a parse tree produced by MT22Parser#identifier_list.
    # identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;

    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        id = ctx.IDENTIFIER().getText()
        if ctx.COMMA():
            return [Id(id)] + self.visit(ctx.identifier_list())
        return [Id(id)]


    # Visit a parse tree produced by MT22Parser#atomictype.
    # atomictype: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()

    # Visit a parse tree produced by MT22Parser#decl_type.
    # decl_type: atomictype | AUTO | array_decl;
    def visitDecl_type(self, ctx:MT22Parser.Decl_typeContext):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by MT22Parser#function_decl.
    # function_decl: IDENTIFIER COLON FUNCTION function_decl_type LP parameterdecl_list? RP (
	# 	INHERIT IDENTIFIER
	# )? block_stmt;
    def visitFunction_decl(self, ctx:MT22Parser.Function_declContext):
        name = ctx.IDENTIFIER()
        typ = self.visit(ctx.function_decl_type())
        param_list = []
        parent = None
        if ctx.parameterdecl_list(): 
            param_list = self.visit(ctx.parameterdecl_list())
        if ctx.INHERIT():
            parent = ctx.IDENTIFIER().getText()
        func_body = self.visit(ctx.block_stmt())
        return FuncDecl(name = name, return_type = typ, params = param_list, inherit = parent, body = func_body)


    # Visit a parse tree produced by MT22Parser#parameterdecl_list.
    # parameterdecl_list: parameter_decl COMMA parameterdecl_list| parameter_decl;
    def visitParameterdecl_list(self, ctx:MT22Parser.Parameterdecl_listContext):
        if ctx.COMMA():
            return [self.visit(ctx.parameter_decl())] + self.visit(ctx.parameterdecl_list())
        else:
            return [self.visit(ctx.parameter_decl())]


    # Visit a parse tree produced by MT22Parser#parameter_decl.
    # parameter_decl: INHERIT? OUT? IDENTIFIER COLON decl_type;
    def visitParameter_decl(self, ctx:MT22Parser.Parameter_declContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        name = str(ctx.IDENTIFIER().getText())
        declare_typ = self.visit(ctx.decl_type())
        return ParamDecl(name = name, typ = declare_typ, inherit = inherit, out = out)


    # Visit a parse tree produced by MT22Parser#function_decl_type.
    # function_decl_type: decl_type | VOID;
    def visitFunction_decl_type(self, ctx:MT22Parser.Function_decl_typeContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.decl_type())


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        if ctx.getChildCount() != 1:
            op = ctx.getChild(1)
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinExpr(op = op, left = left, right = right)
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() != 1:
            op = ctx.getChild(1)
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinExpr(op = op, left = left, right = right)
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr_logical.
    def visitExpr_logical(self, ctx:MT22Parser.Expr_logicalContext):
        if ctx.getChildCount() != 1:
            op = ctx.getChild(1)
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinExpr(op = op, left = left, right = right)
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr_adding.
    def visitExpr_adding(self, ctx:MT22Parser.Expr_addingContext):
        if ctx.getChildCount() != 1:
            op = ctx.getChild(1)
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinExpr(op = op, left = left, right = right)
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr_multiplying.
    # expr_multiplying: expr_multiplying (MULOP | MODULOP | DIVOP) expr_notlogical
	# | expr_notlogical;
    def visitExpr_multiplying(self, ctx:MT22Parser.Expr_multiplyingContext):
        if ctx.getChildCount() != 1:
            op = ctx.getChild(1)
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinExpr(op = op, left = left, right = right)
        return self.visit(ctx.getChild(0))
        

    # Visit a parse tree produced by MT22Parser#expr_notlogical.
    # expr_notlogical: NOT expr_notlogical | expr_term;
    def visitExpr_notlogical(self, ctx:MT22Parser.Expr_notlogicalContext):
        if ctx.NOT():
            op = ctx.NOT()
            val = self.visit(ctx.expr_notlogical())
            return UnExpr(op = op, val = val)
        return self.visit(ctx.expr_term())


    # Visit a parse tree produced by MT22Parser#expr_term.
    # expr_term: SUBOP expr_term | expr_indexop;
    def visitExpr_term(self, ctx:MT22Parser.Expr_termContext):
        op = ctx.SUBOP()
        expr_term = self.visit(ctx.expr_term())
        return UnExpr(op = op, val = expr_term)


    # Visit a parse tree produced by MT22Parser#expr_indexop.
    def visitExpr_indexop(self, ctx:MT22Parser.Expr_indexopContext):
        if ctx.operand():
            self.visit(ctx.operand())
        return self.visit(ctx.index_operator())


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    # operand:
	# INTEGER_LITERAL
	# | function_call
    # | array_lit
	# | FLOAT_LITERAL
	# | STRING_LITERAL
	# | BOOLEAN_LITERAL
	# | IDENTIFIER;
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.INTEGER_LITERAL():
            return IntegerLit(ctx.INTEGER_LITERAL().getText())
        if ctx.FLOAT_LITERAL():
            return FloatLit(ctx.FLOAT_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return StringLit(ctx.STRING_LITERAL().getText())
        if ctx.BOOLEAN_LITERAL():
            return BooleanLit(ctx.BOOLEAN_LITERAL().getText() == 'true')
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.array_lit():
            return self.visit(ctx.array_list())
        return self.visit(ctx.function_call())


    # Visit a parse tree produced by MT22Parser#index_operator.
    # index_operator: IDENTIFIER LSB expression_list RSB;
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        id = ctx.IDENTIFIER().getText()
        exp_list = self.visit(ctx.expression_list())
        return ArrayCell(name = id, cell = exp_list)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
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
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.expression:
            exp = self.visit(ctx.expressioin())
            return ReturnStmt(exp)
        return ReturnStmt()


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bbody.
    def visitBbody(self, ctx:MT22Parser.BbodyContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#block_body.
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.bbody()) + self.visit(ctx.block_body())


    # Visit a parse tree produced by MT22Parser#function_call.
    # function_call: IDENTIFIER LP expression_list? RP;
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        id = ctx.IDENTIFIER().getText()
        exp_list = self.visit(ctx.expression_list())
        return FuncCall(name = id, args = exp_list)
