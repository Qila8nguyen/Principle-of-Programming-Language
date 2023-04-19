grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// ID: 2013859

// ------------------------------------
program: decl_program EOF;

decl: var_decl | function_decl;
decl_program: decl decl_program |;

// PARSER 
array_type_decl: ARRAY LSB dimensions RSB OF atomictype;
array_literal: LCB expression_list RCB;

//EBNF: dimensions: dimen (COMMA dimen)*;
dimensions: INTEGER_LITERAL COMMA dimensions | INTEGER_LITERAL;

atomictype: BOOLEAN | INTEGER | FLOAT | STRING;

// DECLARATION 1. <identifier-list> : <type> [= <expression-list>]?;
var_decl: (identifier_list COLON decl_type | var_decl_full) SEMI;
var_decl_full:
	IDENTIFIER COMMA var_decl_full COMMA expression
	| IDENTIFIER COLON decl_type ASSIGN expression;

//EBNF: identifier_list: IDENTIFIER (COMMA IDENTIFIER)*;
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;

decl_type: atomictype | AUTO | array_type_decl;

//3. <identifier>: function <return-type> (<paramter-list>) [inherit <function-name>]?
function_decl:
	IDENTIFIER COLON FUNCTION function_decl_type LP parameterdecl_list? RP (
		INHERIT IDENTIFIER
	)? block_stmt;
//EBNF: parameterdecl_list: parameter_decl (COMMA parameter_decl)*;
parameterdecl_list:
	parameter_decl COMMA parameterdecl_list
	| parameter_decl;
function_decl_type: decl_type | VOID;

// EXPRESSION
expression: expr STRCONCAT expr | expr;
expr:
	expr_logical (EQ | NEQ | GT | GTEQ | LT | LTEQ) expr_logical
	| expr_logical;
expr_logical: expr_logical (AND | OR) expr_adding | expr_adding;
expr_adding:
	expr_adding (ADDOP | SUBOP) expr_multiplying
	| expr_multiplying;
expr_multiplying:
	expr_multiplying (MULOP | MODULOP | DIVOP) expr_notlogical
	| expr_notlogical;
expr_notlogical: NOT expr_notlogical | expr_term;
expr_term: SUBOP expr_term | expr_indexop;
expr_indexop: index_operator | operand;

//EBNF: expression_list: expression (COMMA expression)*;
expression_list: expression COMMA expression_list | expression;

//2. [inherit]? [out]? <identifier>: <type>
parameter_decl: INHERIT? OUT? IDENTIFIER COLON decl_type;

// STATEMENTS
stmt: (
		assign_stmt
		| if_stmt
		| for_stmt
		| while_stmt
		| dowhile_stmt
		| break_stmt
		| continue_stmt
		| return_stmt
		| call_stmt
		| block_stmt
	);

operand:
	INTEGER_LITERAL
	| function_call
	| array_literal
	| FLOAT_LITERAL
	| STRING_LITERAL
	| BOOLEAN_LITERAL
	| IDENTIFIER;

index_operator: IDENTIFIER LSB expression_list RSB;

assign_stmt: (index_operator | IDENTIFIER) ASSIGN expression SEMI;
if_stmt: IF LP expression RP stmt (ELSE stmt)?;
for_stmt:
	FOR LP IDENTIFIER ASSIGN expression COMMA expression COMMA expression RP stmt;

//EBNF: while_stmt: WHILE LP expression RP stmt*;
while_stmt: WHILE LP expression RP stmt_nullable_list;
stmt_nullable_list: stmt stmt_nullable_list |;

dowhile_stmt: DO block_stmt WHILE LP expression RP SEMI;
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;

//EBNF: return_stmt: RETURN expression? SEMI;
return_stmt: RETURN expression? SEMI;

// call_stmt: IDENTIFIER LP expression_list? RP SEMI;
call_stmt: function_call SEMI;

// block_stmt: LCB (stmt | var_decl)* RCB;
block_stmt: LCB block_body RCB;
bbody: stmt | var_decl;
block_body: bbody block_body |;

//EBNF: function_call: IDENTIFIER LP expression_list? RP;
function_call: IDENTIFIER LP expression_list? RP;

// Type system and values //// KEYWORDS
BOOLEAN_LITERAL: TRUE | FALSE;
// -- 
BOOLEAN: 'boolean';
FLOAT: 'float';
INTEGER: 'integer';
STRING: 'string';
ARRAY: 'array';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
FOR: 'for';
OF: 'of';
BREAK: 'break';
CONTINUE: 'continue';
TRUE: 'true';
FALSE: 'false';
AUTO: 'auto';
VOID: 'void';
RETURN: 'return';
OUT: 'out';
FUNCTION: 'function';
INHERIT: 'inherit';

// OPERATORS
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODULOP: '%';
/* boolean operator */
NOT: '!';
AND: '&&';
OR: '||';
/* int + float + boolean operator */
EQ: '==';
NEQ: '!=';

GT: '>';
GTEQ: '>=';
LT: '<';
LTEQ: '<=';

// String operator -> Scope Resolution: which namespace or class a symbol belongs
STRCONCAT: '::';

// SEPERATORS
ASSIGN: '=';
SEMI: ';';
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
COLON: ':';
PERIOD: '.';
COMMA: ',';

STRING_LITERAL:
	DOUBLEQ CHAR* DOUBLEQ {self.text = self.text[1:-1]};
fragment CHAR: '\\' DOUBLEQ | ~([\r\n"\\]) | STRING_ESCSEQ;
FLOAT_LITERAL:
	INT_PART DECIMAL {self.text = self.text.replace("_", "")}
	| DECIMAL EXPONENTIAL
	| INT_PART DECIMAL? EXPONENTIAL {self.text = self.text.replace("_", "")};

fragment INT_PART: '0' | NONZERO_DIGIT (UNDERSCORE? DIGIT+)*;
fragment NONZERO_DIGIT: [1-9];
fragment DIGIT: [0-9];
fragment DECIMAL: '.' DIGIT*;
fragment EXPONENTIAL: [eE][-+]? DIGIT+;

INTEGER_LITERAL:
	'0'
	| NONZERO_DIGIT (UNDERSCORE? DIGIT+)* {self.text = self.text.replace("_", "")};

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

fragment STRING_ESCSEQ:
	BACKLASH
	| BACKSPACE
	| FORM_FEED
	| HORIZONTAL_TAB
	| SINGLEQ
	| NEWLINE
	| CARRIAGE_RETURN
	| BACKLASH;
// ESCAPE SEQUENCE ???
fragment BACKSPACE: '\\b';
fragment FORM_FEED: '\\f';
fragment CARRIAGE_RETURN: '\\r';
fragment NEWLINE: '\\n';
fragment HORIZONTAL_TAB: '\\t';
fragment SINGLEQ: '\'';
fragment BACKLASH: '\\\\';

fragment DOUBLEQ: '"';
fragment UNDERSCORE: '_';

fragment ILLEGAL_ESCSEQ:
	'\\' ~('b' | 't' | 'f' | 'r' | 'n' | '\'' | '\\');

//WhiteSpace
WS: [ \t\b\f\r\n]+ -> skip;
// Comment C-style
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

UNCLOSE_STRING:
	'"' CHAR* ([\r\n\\] | EOF) {
		if self.text[-1] in ['\b', '\n','\t', '\f', '\r','\\', EOFError]:
			raise UncloseString(self.text[1:-1])
		else: 
			raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE:
	'"' CHAR* ILLEGAL_ESCSEQ {raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};