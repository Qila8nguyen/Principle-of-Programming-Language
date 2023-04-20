import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl1(self):
        input = """x:array[0,1] of integer;"""
        expect = str(Program([VarDecl("x", ArrayType([0, 1], IntegerType()))]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl1(self):
        input = """x, y, z: integer = 1, 0.e5, !5;"""
        expect = str(Program([VarDecl("x", IntegerType(), IntegerLit(1)),
                              VarDecl("y", IntegerType(), FloatLit(float('0.e5'))),
                              VarDecl("z", IntegerType(), UnExpr("!", IntegerLit(5)))]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls1(self):
        input = """x, y, z: integer = 1+1, 2., !5;
		a, b: float;"""
        expect = str(Program([VarDecl("x", IntegerType(), BinExpr("+", IntegerLit(1), IntegerLit(1))),
                              VarDecl("y", IntegerType(), FloatLit(2.)),
                              VarDecl("z", IntegerType(), UnExpr("!", IntegerLit(5))),
                              VarDecl("a", FloatType()),
                              VarDecl("b", FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program1(self):
        """Simple program"""
        input = """main: function void () {
		}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program1(self):
        """More complex program"""
        input = """main: function void () {
			printInteger(4);
		}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_var_declaration1(self):
        """var  declaration with initialization"""''
        inp = """a: integer = a+7-7+3 * 5-(25-b(1));"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(a), IntegerLit(7)), IntegerLit(7)), BinExpr(*, IntegerLit(3), IntegerLit(5))), BinExpr(-, IntegerLit(25), FuncCall(b, [IntegerLit(1)]))))
])"""
        self.assertTrue(TestAST.test(inp, expect, 305))

    def test_var_declaration_21(self):
        """var type arrray declaration with initialization"""
        inp = """a: array[1, 5] of integer = {1,2,3,4,5};"""
        expect = str(Program([
            VarDecl("a", ArrayType([1, 5], IntegerType()),
                    ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 306))

    def test_var_declaration_31(self):
        """var string declaration with initialization"""
        inp = """a: string = "Hello";"""
        expect = str(Program([
            VarDecl("a", StringType(), StringLit("Hello"))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 307))

    def test_var_declaration_41(self):
        """var boolean declaration with initialization"""
        inp = """a: boolean = true;"""
        expect = str(Program([
            VarDecl("a", BooleanType(), BooleanLit(True))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 308))

    def test_var_declaration_51(self):
        """var float declaration with initialization"""
        inp = """a: float = 1.5;"""
        expect = str(Program([
            VarDecl("a", FloatType(), FloatLit(1.5))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 309))

    def test_var_declaration_61(self):
        """var float declaration with initialization"""
        inp = """a: float = 1.5e-5;"""
        expect = str(Program([
            VarDecl("a", FloatType(), FloatLit(1.5e-5))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 310))

    def test_var_declaration_71(self):
        """var float declaration with initialization"""
        inp = """a: float = 0.e5;"""
        expect = str(Program([
            VarDecl("a", FloatType(), FloatLit(0.e5))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 311))

    def test_var_declaration_81(self):
        """var float declaration with initialization"""
        inp = """a: float = 1.5e5;"""
        expect = str(Program([
            VarDecl("a", FloatType(), FloatLit(1.5e5))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 312))

    def test_var_declaration_91(self):
        """var array declaration with initialization"""
        inp = """a: array[1, 5] of integer = {1+1-2,2*3-4,0.e-5,1.5e5,1.5e-5};"""
        expect = str(Program([
            VarDecl("a", ArrayType([1, 5], IntegerType()), ArrayLit(
                [BinExpr("-", BinExpr("+", IntegerLit(1), IntegerLit(1)), IntegerLit(2)),
                 BinExpr("-", BinExpr("*", IntegerLit(2), IntegerLit(3)), IntegerLit(4)), FloatLit(0.e-5),
                 FloatLit(1.5e5), FloatLit(1.5e-5)]))
        ]))
        self.assertTrue(TestAST.test(inp, expect, 313))

    def test_function_call1(self):
        """function call"""
        inp = """a: integer = b(1);"""
        expect = Program([VarDecl("a", IntegerType(), FuncCall("b", [IntegerLit(1)]))])
        self.assertTrue(TestAST.test(inp, str(expect), 314))

    def test_short_vardecl11(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl11(self):
        input = """x, y, z: integer = 1, 2, 3;a:boolean;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_expression11(self):
        input = """
		foo1: function void(inherit out a: integer, b: integer) {
			a = a + b - 1 * 2 / 3 % (4 && b || !a);
		}
		"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [InheritOutParam(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(a), Id(b)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(||, BinExpr(&&, IntegerLit(4), Id(b)), UnExpr(!, Id(a))))))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 314))

    def test_expression21(self):
        input = """
		fefef : function integer() {
			do {
				arr[foo()] = arr[foo()]::arr[1,2];
			}
			while (  1 + 2 );
			return 1;
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), BlockStmt([AssignStmt(ArrayCell(arr, [FuncCall(foo, [])]), BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])))])), ReturnStmt(IntegerLit(1))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 315))

    def test_mixed11(self):
        input = """
		a8: function float ( out d5: auto) inherit c6
	{
		a8[19.8] = "aaaaa";
	}
e2,b1: string;
a2,c3,b10: float = 276,!158,true;
c9: function float (inherit out a6: float) 
	{
		if (c9(b10["this is string"]))
			if (e5[856,449])
				b5["aaaaa"] = true;
		else 	for (a7=599,"this is string",49.6)
				{}
		d10: integer = 781;
	}
e6: function void () inherit c3
	{}
		"""
        expect = """Program([
	FuncDecl(a8, FloatType, [OutParam(d5, AutoType)], c6, BlockStmt([AssignStmt(ArrayCell(a8, [FloatLit(19.8)]), StringLit(aaaaa))]))
	VarDecl(e2, StringType)
	VarDecl(b1, StringType)
	VarDecl(a2, FloatType, IntegerLit(276))
	VarDecl(c3, FloatType, UnExpr(!, IntegerLit(158)))
	VarDecl(b10, FloatType, BooleanLit(True))
	FuncDecl(c9, FloatType, [InheritOutParam(a6, FloatType)], None, BlockStmt([IfStmt(FuncCall(c9, [ArrayCell(b10, [StringLit(this is string)])]), IfStmt(ArrayCell(e5, [IntegerLit(856), IntegerLit(449)]), AssignStmt(ArrayCell(b5, [StringLit(aaaaa)]), BooleanLit(True)), ForStmt(AssignStmt(Id(a7), IntegerLit(599)), StringLit(this is string), FloatLit(49.6), BlockStmt([])))), VarDecl(d10, IntegerType, IntegerLit(781))]))
	FuncDecl(e6, VoidType, [], c3, BlockStmt([]))
])"""

        self.assertTrue(TestAST.test(input, expect, 316))

    def test_short_vardeclx1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardeclx1(self):
        input = """x, y, z: integer = 1, 2, 3;a:boolean;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardeclsx1(self):
        input = """x, y, z: integer = 1, 2, 3;
	a, b: float;"""

        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""

        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program11(self):
        """Simple program: integer main() {}"""
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 201))

    def test_decl_variable11(self):
        """test decl integer variable"""
        inp = r"""A, B: integer = 5, 6;"""
        expect = """Program([
	VarDecl(A, IntegerType, IntegerLit(5))
	VarDecl(B, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(inp, expect, 202))

    def test_decl_variable21(self):
        """test decl string variable"""
        inp = r"""A, B: string = "abc", "def";"""
        expect = """Program([
	VarDecl(A, StringType, StringLit(abc))
	VarDecl(B, StringType, StringLit(def))
])"""
        self.assertTrue(TestAST.test(inp, expect, 203))

    def test_decl_variable31(self):
        """test decl float variable"""
        inp = r"""A, B: float = 1.2, 3.4e-10;"""
        expect = """Program([
	VarDecl(A, FloatType, FloatLit(1.2))
	VarDecl(B, FloatType, FloatLit(3.4e-10))
])"""
        self.assertTrue(TestAST.test(inp, expect, 204))

    def test_decl_variable41(self):
        """test decl boolean variable"""
        inp = r"""A, B: boolean = true, false;"""
        expect = """Program([
	VarDecl(A, BooleanType, BooleanLit(True))
	VarDecl(B, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(inp, expect, 205))

#     def test_decl_variable51(self):
        """test decl array variable"""
        inp = r"""A, B: array[1,2] of integer = {1, 2}, {3, foo(4)};"""
        expect = """Program([
	VarDecl(A, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(B, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(3), FuncCall(foo, [IntegerLit(4)])]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 206))

    def test_decl_variable61(self):
        """test decl auto variable"""
        inp = r"""A, B: auto = 1, foo(4);"""
        expect = """Program([
	VarDecl(A, AutoType, IntegerLit(1))
	VarDecl(B, AutoType, FuncCall(foo, [IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 207))

    def test_decl_function11(self):
        """test decl function"""
        inp = r"""A: function integer() {}"""
        expect = """Program([
	FuncDecl(A, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 209))

    def test_decl_function21(self):
        """test decl function"""
        inp = r"""A: function integer() inherit foo {}"""
        expect = """Program([
	FuncDecl(A, IntegerType, [], foo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 210))

    def test_decl_function31(self):
        """test decl function"""
        inp = r""" 
			inc: function void(out n: integer) {
				n  = n+ 1;
				return n;
			}"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 211))

    def test_expr11(self):
        """test expr"""
        inp = r"""x:integer = a + b * c - d / e % f;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, Id(a), BinExpr(*, Id(b), Id(c))), BinExpr(%, BinExpr(/, Id(d), Id(e)), Id(f))))
])"""
        self.assertTrue(TestAST.test(inp, expect, 213))

    def test_expr21(self):
        """test expr"""
        inp = r"""x:float=1E-4+10.0;"""
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, FloatLit(0.0001), FloatLit(10.0)))
])"""
        self.assertTrue(TestAST.test(inp, expect, 214))

    def test_expr31(self):
        """test expr"""
        inp = r"""
		 boo: boolean =  a && b || c && !d;
		"""
        expect = """Program([
	VarDecl(boo, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), UnExpr(!, Id(d))))
])"""
        self.assertTrue(TestAST.test(inp, expect, 215))

    def test_expr41(self):
        """test expr"""
        inp = r"""

			newStr: string = "Hello "::"World!";

		"""
        expect = """Program([
	VarDecl(newStr, StringType, BinExpr(::, StringLit(Hello ), StringLit(World!)))
])"""
        self.assertTrue(TestAST.test(inp, expect, 216))

    def test_expr51(self):
        """test expr"""
        inp = r"""
		main: function void(){
			eq = a == b;
			neq = a != b;
			lt = a < b;
			le = a <= b;
			gt = a > b;
			ge = a >= b;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(eq), BinExpr(==, Id(a), Id(b))), AssignStmt(Id(neq), BinExpr(!=, Id(a), Id(b))), AssignStmt(Id(lt), BinExpr(<, Id(a), Id(b))), AssignStmt(Id(le), BinExpr(<=, Id(a), Id(b))), AssignStmt(Id(gt), BinExpr(>, Id(a), Id(b))), AssignStmt(Id(ge), BinExpr(>=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 217))

    def test_expr61(self):
        """test index operator"""
        inp = r"""
		main: function void(){
			Arr: array[5] of integer = {1,2,3,4,5};
			a = Arr[3+1];
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(Arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(a), ArrayCell(Arr, [BinExpr(+, IntegerLit(3), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 218))

    def test_expr71(self):
        """test index operator"""
        inp = r"""
		main: function void(){
			Arr: array[5] of integer;
			a = Arr[3];
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(Arr, ArrayType([5], IntegerType)), AssignStmt(Id(a), ArrayCell(Arr, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 219))

    def test_function11(self):
        """test function call"""
        inp = r"""
		main: function void(){
			foo(12);
			fee(13);
			fum(14+12, a&&b);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(12)), CallStmt(fee, IntegerLit(13)), CallStmt(fum, BinExpr(+, IntegerLit(14), IntegerLit(12)), BinExpr(&&, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 220))

    def test_function21(self):
        """test function call"""
        inp = r"""
		main: function void() {
			a : boolean = foo(12);
			b = fee(13);
			c = fum(14+12, a&&b);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(12)])), AssignStmt(Id(b), FuncCall(fee, [IntegerLit(13)])), AssignStmt(Id(c), FuncCall(fum, [BinExpr(+, IntegerLit(14), IntegerLit(12)), BinExpr(&&, Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 221))

    def test_function31(self):
        """test function call"""
        inp = r"""
		main: function void() {
		b = fee(foo(13));
		c = fum(14+12, foo(a&&b));
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), FuncCall(fee, [FuncCall(foo, [IntegerLit(13)])])), AssignStmt(Id(c), FuncCall(fum, [BinExpr(+, IntegerLit(14), IntegerLit(12)), FuncCall(foo, [BinExpr(&&, Id(a), Id(b))])]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 222))

    def test_stmt_assign11(self):
        """test assigment"""
        inp = r"""
		main: function void() {
			a : integer = 3;
			b : integer = a;
			a = b;
			b = foo(a&&b);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), VarDecl(b, IntegerType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), FuncCall(foo, [BinExpr(&&, Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 223))

    def test_stmt_assign21(self):
        """test assigment"""
        inp = r"""
		a : integer = f00(22-foo(a + too(a)));
		"""
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(f00, [BinExpr(-, IntegerLit(22), FuncCall(foo, [BinExpr(+, Id(a), FuncCall(too, [Id(a)]))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 224))

    def test_stmt_assign31(self):
        """test assignment"""
        inp = """
		b : integer = 5;
		a : integer = b6;
		"""
        expect = """Program([
	VarDecl(b, IntegerType, IntegerLit(5)), VarDecl(a, IntegerType, AssignStmt(Id(b), IntegerLit(6)))
])"""

    def test_stmt_ifelse11(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (a&&B) {
				a = b;
				c = d;
			} else  
				c = 1;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), Id(B)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(c), Id(d))]), AssignStmt(Id(c), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 230))

    def test_stmt_ifelse21(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (a&&B) {
				a = b;
				c = d;
			} else {} // empty
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), Id(B)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(c), Id(d))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 231))

    def test_stmt_ifelse31(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (a&&B) {
				a = b;
				c = d;
				return False;
			} else 
				break;
			return ;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), Id(B)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(c), Id(d)), ReturnStmt(Id(False))]), BreakStmt()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 232))

    def test_stmt_ifelse41(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (a&&B) {
				if (true) a = a + 1;
				else continue;
			} else  // no expr
				break;
			return true;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), Id(B)), BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ContinueStmt())]), BreakStmt()), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 233))

    def test_stmt_ifelse61(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (a&&B) {
				if (true) a = a + 1;
				else continue;
			} 
			else if (true) a = a + 1;
			else continue;
			return true;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(a), Id(B)), BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ContinueStmt())]), IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ContinueStmt())), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 235))

    def test_stmt_ifelse71(self):
        """test ifelse"""
        inp = r"""
		main: function void() {
			if (1+1 == 2)
			return true;
			else {if (1 + 1 != 3 && a)
			return false;}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(2)), ReturnStmt(BooleanLit(True)), BlockStmt([IfStmt(BinExpr(!=, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(&&, IntegerLit(3), Id(a))), ReturnStmt(BooleanLit(False)))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 236))

    def test_stmt_for11(self):
        """test for"""
        inp = r"""
		main: function void() {
			for (i = 1, i <= 10, 1 + i)
			{
				a = a + 1;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, IntegerLit(1), Id(i)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 237))

    def test_stmt_for21(self):
        """test for -- assign?"""
        inp = r"""
		main: function void() {
			for (i = 1, i <= 10,  1 + i)
				a = a + 1;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, IntegerLit(1), Id(i)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 238))

    def test_stmt_for41(self):
        """test for"""
        inp = r"""
		main: function void() {
			for (i = 1, i <= 10 && a || b,  1 + i)
			{
				a = a + 1;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(||, BinExpr(&&, IntegerLit(10), Id(a)), Id(b))), BinExpr(+, IntegerLit(1), Id(i)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 240))

    def test_stmt_for51(self):
        """test for"""
        inp = r"""
		main: function void() {
			for (i = 1, i <= 10 && a || b,  1 + i)
			{
				a = a + 1;
				if (a == 1) continue;
				else break;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(||, BinExpr(&&, IntegerLit(10), Id(a)), Id(b))), BinExpr(+, IntegerLit(1), Id(i)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ContinueStmt(), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 241))

    def test_stmt_for61(self):
        """test for"""
        inp = r"""
		main: function void() {
			for (i = foo(12 * 3), i <= 10 && a || b,  foo(i))
			{
				a = a + 1;
				if (a == 1) continue;
				else break;
			}
			return true;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(foo, [BinExpr(*, IntegerLit(12), IntegerLit(3))])), BinExpr(<=, Id(i), BinExpr(||, BinExpr(&&, IntegerLit(10), Id(a)), Id(b))), FuncCall(foo, [Id(i)]), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ContinueStmt(), BreakStmt())])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 242))

    def test_stmt_for71(self):
        """test for"""
        inp = r"""
		main: function void() {
			for (i = foo(12 * 3), i <= 10 && a || b,  foo(i))
				if (a == 1) continue;
				else break;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(foo, [BinExpr(*, IntegerLit(12), IntegerLit(3))])), BinExpr(<=, Id(i), BinExpr(||, BinExpr(&&, IntegerLit(10), Id(a)), Id(b))), FuncCall(foo, [Id(i)]), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ContinueStmt(), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 243))

    def test_stmt_while21(self):
        """test while"""
        inp = r"""
		main: function void() {
			while (foo(a&&b + f00(12) != 10 && A))
			{
				continue;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(FuncCall(foo, [BinExpr(!=, BinExpr(&&, Id(a), BinExpr(+, Id(b), FuncCall(f00, [IntegerLit(12)]))), BinExpr(&&, IntegerLit(10), Id(A)))]), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 245))

    def test_stmt_dowhile11(self):
        """test dowhile"""
        inp = r"""
		main: function void() {
			do {
				continue;
				}
			while (i != 10 + 12);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), BinExpr(+, IntegerLit(10), IntegerLit(12))), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 246))

    def test_stmt_dowhile21(self):
        """test dowhile"""
        inp = r"""
		main: function void() {
			do 
				{
					do{}while(false);
				}
			while (i != 10 + 12);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), BinExpr(+, IntegerLit(10), IntegerLit(12))), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 247))

    def test_stmt_dowhile31(self):
        """test dowhile"""
        inp = r"""
		main: function void() {
			do{do{}while(false);}while(false);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 248))

    def test_stmt_return11(self):
        """test return"""
        inp = r"""
		main: function void() {
			return;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 249))

    def test_stmt_return21(self):
        """test return"""
        inp = r"""
		main: function void() {
			return a && b + 10 % 12;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(&&, Id(a), BinExpr(+, Id(b), BinExpr(%, IntegerLit(10), IntegerLit(12)))))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 250))

    def test_stmt_fcall11(self):
        """test fcall"""
        inp = r"""
		main: function void() {
			foo(12);
			e2q(foo(12 + w(12)) + 21 && a || b);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(12)), CallStmt(e2q, BinExpr(||, BinExpr(&&, BinExpr(+, FuncCall(foo, [BinExpr(+, IntegerLit(12), FuncCall(w, [IntegerLit(12)]))]), IntegerLit(21)), Id(a)), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 251))

    def test_stmt_block11(self):
        """test block"""
        inp = r"""
		main: function void() {{{
				a = a + 1;
				b = b + 1;
				{
					a = a + 1;
				}
				b = b + 1;
			}}return;}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1))), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))])]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 252))

    def test_mixed121(self):
        """test mixed"""
        inp = r"""
		// program to print all odd number from 1 to 5000
		main: function void() {
			for (i = 1, i <= 5000,  i + 1)
			{
				/* check if i is odd or not */
				if (i % 2 == 1)
					printInt(i);
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(5000)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(1)), CallStmt(printInt, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 253))

    def test_mixed21(self):
        """test mixed"""
        inp = r"""
		// program to calculate the sum of all even numbers from 1 to 100
		calc: function void(out sum: integer) {
			sum = 0;
			for (i = 1, i <= 100,  i + 1)
			{
				/* check if i is even or not */
				if (i % 2 == 0)
					sum = sum + i;
			}
			return;
		}
		main: function void() {
			sum : integer;
			calc(sum);
		}
		"""
        expect = """Program([
	FuncDecl(calc, VoidType, [OutParam(sum, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))])), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(sum, IntegerType), CallStmt(calc, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 254))

    def test_mixed31(self):
        """test mixed"""
        inp = r"""
		// program to find the factorial of a number
		fact: function integer(n: integer) {
			if (n == 0)
				return 1;
			else
				return n * fact(n - 1);
		}
		main: function void() {
			printInt(fact(5));
		}
		"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInt, FuncCall(fact, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 255))

    def test_mixed41(self):
        """test mixed"""
        inp = r"""
		// program to find highest number in a matrix
		maxmat: function integer(out mat: array[3,3] of integer) {
			max : integer;
			max = mat[0,0];
			for (i = 0, i < 10,  i + 1)
			{
				for (j = 0, j < 10,  j + 1)
				{
					if (mat[i,j] > max)
						max = mat[i,j];
				}
			}
			return max;
		}
		main: function void() {
			mat : array[3,3] of integer = {{1,2,3},{4,5,6},{7,8,9}};
			printInt(maxmat(mat));
		}
		"""
        expect = """Program([
	FuncDecl(maxmat, IntegerType, [OutParam(mat, ArrayType([3, 3], IntegerType))], None, BlockStmt([VarDecl(max, IntegerType), AssignStmt(Id(max), ArrayCell(mat, [IntegerLit(0), IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(mat, [Id(i), Id(j)]), Id(max)), AssignStmt(Id(max), ArrayCell(mat, [Id(i), Id(j)])))]))])), ReturnStmt(Id(max))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(mat, ArrayType([3, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])])), CallStmt(printInt, FuncCall(maxmat, [Id(mat)]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 256))

    def test_mixed51(self):
        """test mixed"""
        inp = r"""
		// program to find the sum of all elements in a matrix
		summat: function integer(out mat: array[3,3] of integer) {
			sum : integer;
			sum = 0;
			for (i = 0, i < 10,  i + 1)
			{
				for (j = 0, j < 10,  j + 1)
				{
					sum = sum + mat[i,j];
				}
			}
			return sum;
		}
		main: function void() {
			mat : array[3,3] of integer = {{1,2,3},{4,5,6},{7,8,9}};
			printInt(summat(mat));
		}
		"""
        expect = """Program([
	FuncDecl(summat, IntegerType, [OutParam(mat, ArrayType([3, 3], IntegerType))], None, BlockStmt([VarDecl(sum, IntegerType), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(mat, [Id(i), Id(j)])))]))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(mat, ArrayType([3, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])])), CallStmt(printInt, FuncCall(summat, [Id(mat)]))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 257))

    def test_mixed61(self):
        """test mixed"""
        inp = r"""
		// bubble sort implementation
		bubble: function void(inherit out arr: array[10] of integer) {
			for (i = 0, i < 10,  i + 1)
			{
				for (j = 0, j < 10 - i - 1,  j + 1)
				{
					if (arr[j] > arr[j + 1])
					{
						temp : integer;
						temp = arr[j];
						arr[j] = arr[j + 1];
						arr[j + 1] = temp;
					}
				}
			}
			return;
		}
		main: function void() {
			arr : array[10] of integer = {1,2,3,4,5,6,7,8,9,10};
			bubble(arr);
			for (i = 0, i < 10,  i + 1)
				printInt(arr[i]);
		}

		"""
        expect = """Program([
	FuncDecl(bubble, VoidType, [InheritOutParam(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, IntegerLit(10), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([VarDecl(temp, IntegerType), AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))])), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), CallStmt(bubble, Id(arr)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInt, ArrayCell(arr, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(inp, expect, 258))

    def test_vardecl11(self):
        """test short variable decl"""
        input = """a: integer = 3;b,c:string = "abc","def";"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, StringType, StringLit(abc))
	VarDecl(c, StringType, StringLit(def))
])"""
        self.assertTrue(TestAST.test(input, expect, 259))

    def test_vardecl21(self):
        """test full variable decl"""
        input = """a, s, d: integer = 2, 3, 4;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(s, IntegerType, IntegerLit(3))
	VarDecl(d, IntegerType, IntegerLit(4))
])"""
        self.assertTrue(TestAST.test(input, expect, 260))

    def test_mixed71(self):
        """test return type in function decl"""
        input = r"""main: function void () {}
		fact: function integer (n: integer) {}
		inc: function void(out n: integer, delta: integer) {}
		autofact: function auto (n: integer) {}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
	FuncDecl(autofact, AutoType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 262))

    def test_mixed81(self):
        """mixed test"""
        input = r"""
		port : integer = 80;
		host : string = "localhost";
		startServer: function void() {
			server : auto = newServer(host, port);
			start(server);
		}
		main: function void() {
			startServer();
		}"""
        expect = """Program([
	VarDecl(port, IntegerType, IntegerLit(80))
	VarDecl(host, StringType, StringLit(localhost))
	FuncDecl(startServer, VoidType, [], None, BlockStmt([VarDecl(server, AutoType, FuncCall(newServer, [Id(host), Id(port)])), CallStmt(start, Id(server))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(startServer, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 263))

    def test_mixed91(self):
        """mixed test"""
        input = r"""
		inc: function void(inherit a: integer, inherit out b: integer, inherit c:boolean, out d:integer) {}
		"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, IntegerType), InheritParam(c, BooleanType), OutParam(d, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 264))

    def test_mixed101(self):
        """mixed test"""
        input = r"""
		caclPi: function float(n: integer) {
			pi : float = 0;
			for (i = 0, i < n, i + 1)
			{
				t : float = i % 2;
				if (t == 0)
					pi = pi + 4 / 2 * i + 1;
				else
					pi = pi - 4 / 2 * i + 1;
			}
			return pi;
		}
		main: function void() {
			do {
				n : integer;
				print("Enter n: ");
				n = readInt();
				print("Pi = ");
				printFloat(caclPi(n));
				print("\n");
			} while (n != 0);
		}

		"""
        expect = """Program([
	FuncDecl(caclPi, FloatType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(pi, FloatType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(t, FloatType, BinExpr(%, Id(i), IntegerLit(2))), IfStmt(BinExpr(==, Id(t), IntegerLit(0)), AssignStmt(Id(pi), BinExpr(+, BinExpr(+, Id(pi), BinExpr(*, BinExpr(/, IntegerLit(4), IntegerLit(2)), Id(i))), IntegerLit(1))), AssignStmt(Id(pi), BinExpr(+, BinExpr(-, Id(pi), BinExpr(*, BinExpr(/, IntegerLit(4), IntegerLit(2)), Id(i))), IntegerLit(1))))])), ReturnStmt(Id(pi))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Enter n: )), AssignStmt(Id(n), FuncCall(readInt, [])), CallStmt(print, StringLit(Pi = )), CallStmt(printFloat, FuncCall(caclPi, [Id(n)])), CallStmt(print, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 265))

    def test_mixed111(self):
        """mixed test"""
        input = r"""
		main: function void() {
			n : integer;
			print("Enter n: ");
			n = readInt();
			print("Factorial of ");
			printInt(n);
			print(" is ");
			printInt(fact(n));
		}
		fact: function integer(n: integer) {
			if (n == 0)
				return 1;
			else
				return n * fact(n - 1);
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Enter n: )), AssignStmt(Id(n), FuncCall(readInt, [])), CallStmt(print, StringLit(Factorial of )), CallStmt(printInt, Id(n)), CallStmt(print, StringLit( is )), CallStmt(printInt, FuncCall(fact, [Id(n)]))]))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 266))

    def test_mixed121x(self):
        """mixed test"""
        input = r"""
			foo2: function string (out a: integer, b: integer) inherit foo1 {
				for (i = 0, i < 10, i == 2) {
					a = -a;
				}
				/*foo3: function string() { 
					for (i = init(i), foo4(i), i == 2) 
						a = a + 1;
				}*/
				return "abc";
			}
		"""
        expect = """Program([
	FuncDecl(foo2, StringType, [OutParam(a, IntegerType), Param(b, IntegerType)], foo1, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(==, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), UnExpr(-, Id(a)))])), ReturnStmt(StringLit(abc))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 267))

    def test_mixed131(self):
        """mixed test"""
        input = r"""
		mat : array[1,2,3,4,3] of integer = {{1,2,3},{4,5,6},{7,8,9}};
		"""
        expect = """Program([
	VarDecl(mat, ArrayType([1, 2, 3, 4, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 268))

    def test_mixed151(self):
        """mixed test"""
        input = r"""
		main: function void() {
			n = {1,2,3}::{1,2,3};
			str1 = "23r"::"23432aa";
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), AssignStmt(Id(str1), BinExpr(::, StringLit(23r), StringLit(23432aa)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 270))

    def test_mixed161(self):
        """mixed test"""
        input = r"""
		main: function void() {
			n = ff()::dd();
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(::, FuncCall(ff, []), FuncCall(dd, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 271))

    def test_mixed171(self):
        """mixed test"""
        input = r"""
		main: function void() {
			a = {1+2,2/4};
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, IntegerLit(2), IntegerLit(4))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 272))

    def test_mixed181(self):
        """mixed test"""
        input = r"""
		main: function void() {
			n = {1,2,3}::{1,2,3};
			str1 = "23r"::n;
			for (i = 0, i < 10, i :: 23) {
				a = -a;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), AssignStmt(Id(str1), BinExpr(::, StringLit(23r), Id(n))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(::, Id(i), IntegerLit(23)), BlockStmt([AssignStmt(Id(a), UnExpr(-, Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 273))

    def test_mixed191(self):
        """mixed test"""
        input = r"""
		main: function void() {
			n = {1,2,3}::{1,2,3};
			str1 = "23r"::n;
			for (i = 0, i < 10, a :: 23) {
				a = -a;
			}
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), AssignStmt(Id(str1), BinExpr(::, StringLit(23r), Id(n))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(::, Id(a), IntegerLit(23)), BlockStmt([AssignStmt(Id(a), UnExpr(-, Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 274))

    def test_mixed221(self):
        """mixed test"""
        input = r"""
		main: function void() {
		 //   n = {1,2,3}::{1,2,3};
		 /**
			str1 = "23r"::n;
		*/
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 277))

    def test_mixed241(self):
        """mixed test"""
        input = r"""
		a,v: array[1,2,3,4,5] of integer = {1,2,3,4,5}, {1,2,3,4,5};
		"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	VarDecl(v, ArrayType([1, 2, 3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 279))

    def test_mixed261(self):
        """mixed test"""
        input = r"""
		fefef : function integer() {
			a, b: boolean = arr[0,1], arr[1,2];
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([VarDecl(a, BooleanType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)])), VarDecl(b, BooleanType, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 281))

    def test_mixed271(self):
        """mixed test"""
        input = r"""
		fefef : function integer() {
			a, b: boolean = arr[foo()], arr[1,2];
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([VarDecl(a, BooleanType, ArrayCell(arr, [FuncCall(foo, [])])), VarDecl(b, BooleanType, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 282))

    def test_mixed281(self):
        """mixed test"""
        input = r"""
		fefef : function integer() {
			do {
			}
			while ( arr[foo()]::arr[1,2] );
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 283))

    def test_mixed291(self):
        """mixed test"""
        input = r"""
		fefef : function integer() {
			while ( arr[foo()]::arr[1,2] ) {}
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 284))

    def test_mixed301(self):
        """mixed test"""
        input = r"""
		fefef : function integer() {
			do {
			}
			while ( arr[foo()]::arr[1,2] > 1 + 2 );
			return 1;
		}
		"""
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), BinExpr(>, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]), BinExpr(+, IntegerLit(1), IntegerLit(2)))), BlockStmt([])), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 285))

    def test_mixed321(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
				return !-1;
		}

		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(UnExpr(!, UnExpr(-, IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 287))

    def test_mixed341(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
				return !!!1;
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(1)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 289))

    def test_mixed351(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
				for (i = -foo(), i < 10, i :: 3E-10) {
					a = ---a;
					}
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), UnExpr(-, FuncCall(foo, []))), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(::, Id(i), FloatLit(3e-10)), BlockStmt([AssignStmt(Id(a), UnExpr(-, UnExpr(-, UnExpr(-, Id(a)))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 290))

    def test_mixed381(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			return foo(1_2 + 2 || 4 :: 5);
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, [BinExpr(::, BinExpr(||, BinExpr(+, IntegerLit(12), IntegerLit(2)), IntegerLit(4)), IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 293))

    def test_mixed391(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			return -----foo(1_2 + 2 || 4 :: 5);
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, FuncCall(foo, [BinExpr(::, BinExpr(||, BinExpr(+, IntegerLit(12), IntegerLit(2)), IntegerLit(4)), IntegerLit(5))])))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 294))

    def test_mixed401(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			return !32_23_12-3_6-2;
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(-, UnExpr(!, IntegerLit(322312)), IntegerLit(36)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 295))

    def test_mixed411(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			break; continue; break; continue;
			while (1) {
				break; continue; break; continue;
				}
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([BreakStmt(), ContinueStmt(), BreakStmt(), ContinueStmt(), WhileStmt(IntegerLit(1), BlockStmt([BreakStmt(), ContinueStmt(), BreakStmt(), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 296))

    def test_mixed421(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
            if (1) 
                if (2) 
                    if (3) 
                        a=4;
                    else
                        a=5;
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([IfStmt(IntegerLit(1), IfStmt(IntegerLit(2), IfStmt(IntegerLit(3), AssignStmt(Id(a), IntegerLit(4)), AssignStmt(Id(a), IntegerLit(5)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 297))

    def test_mixed441(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			return fooo("q423 \\");
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([ReturnStmt(FuncCall(fooo, [StringLit(q423 \\\\)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 298))

    def test_mixed451(self):
        """mixed test"""
        input = r"""
		learningtofly: function integer() {
			as, n : string = "q423 \\", "dwaf"::"dwad";
		}
		"""
        expect = """Program([
	FuncDecl(learningtofly, IntegerType, [], None, BlockStmt([VarDecl(as, StringType, StringLit(q423 \\\\)), VarDecl(n, StringType, BinExpr(::, StringLit(dwaf), StringLit(dwad)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 299))
