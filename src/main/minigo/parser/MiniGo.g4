grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
preType = None
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        self.preType = tk
        return super().emit();
}

options{
    language=Python3;
}

program  : decl* EOF ;
decl: stmt|funcdecl | arraydecl | structdecl | interfacedecl |constdecl ;

vardecl: 'var' ID typ? '=' expr nl
    | 'var' ID typ nl ;

receiver: '(' ID typ ')' ;
funcdecl: 'func' receiver? ID PAREN_OPEN paramlist? PAREN_CLOSE (typ|(PAREN_OPEN paramlist PAREN_CLOSE))? '{' (stmt )* returnstmt? '}' nl ;


arraydecl: 'var' ID arraytype nl ;

arraytype: ('[' (INTLIT | ID) ']')+ basictype ;


structdecl: 'type' ID 'struct' '{' fielddecl* '}' nl;
fielddecl: (ID typ) (';'|nl);
typ: arraytype | basictype ;
basictype: TYPE | ID ;

interfacedecl: 'type' ID 'interface' '{' methoddecl* '}' nl;
methoddecl: ID '(' paramlist? ')' typ? nl ;
paramlist: param (',' param)* ;
param: ID (',' ID)* typ ;

constdecl: 'const' ID '=' expr nl ;

array_access: (funccall|ID) ('[' INTLIT ']')+ ;
struct_access: (ID|array_access) '.' (ID|array_access|funccall);

multi_array_literal: ('[' expr ']')+ typ '{' ( '{' expr (',' expr)* '}' ) (',' '{' expr (',' expr)* '}' )+ '}' ;
array_literal: ('[' expr ']')+ typ '{' expr (',' expr)* '}' ;

struct_literal: ID '{' struct_field_list? '}' ;
struct_field_list: struct_field (',' struct_field)* ;
struct_field: ID COLON expr ;

funccall: ID '(' arglist? ')' ;
arglist: expr (',' expr)* ;

methodcall: ((array_access|struct_access|ID) '.')+ ID '(' arglist? ')' ;

//stmt
stmt: vardecl| assignstmt 
    | ifstmt 
    | forstmt
    | breakstmt 
    | continuestmt 
    | returnstmt 
    | callstmt ;

assignstmt: (ID| struct_access|array_access  ) (OP_ASSEQ|OP_ASSIGN|OP_EQUAL) expr nl ;

ifstmt:(('if'  expr  block (NEWLINE? elseifstmt)* (NEWLINE? elsestmt)? )| ('if' '(' expr ')' block (NEWLINE? elseifstmt)* (NEWLINE? elsestmt)?) )nl;
elseifstmt:('else' 'if'   expr   block) | ('else' 'if'  '(' expr ')'  block) ;
elsestmt: 'else' block ;

forstmt: 'for' expr block nl
        | 'for'  forinit ';' expr ';' forupdate  block nl
        | 'for' ID  ',' ID OP_ASSEQ 'range' ID block nl ;
forinit: ((ID| struct_access|array_access  ) (OP_ASSEQ|OP_ASSIGN|OP_EQUAL) expr) | vardecl ;
forupdate: ((ID| struct_access|array_access  ) (OP_ASSEQ|OP_ASSIGN|OP_EQUAL) expr) ;

breakstmt: 'break' nl ;

continuestmt: 'continue' nl ;

returnstmt: 'return' expr? nl ;

callstmt: ID '(' arglist? ')' nl ;
block: '{' (stmt )* '}' ;
// Lexer rules
expr: expr OP_ARITH expr
    | expr OP_LOGIC expr
    | expr OP_COMPARE expr
    | '(' expr ')'
    | INTLIT
    | FLOATLIT
    | STRLIT
    | BOOLLIT
    | NILLIT
    | methodcall
    | funccall
    | multi_array_literal
    | array_literal
    | struct_literal
    | struct_access
    | array_access
    | ID;
// Operations
OP_COMPARE: '==' | '!=' | '<' | '<=' | '>' | '>=' ;
OP_ASSIGN:  '+=' | '-=' | '*=' | '/=' | '%=' ;
OP_LOGIC: '&&' | '||' | '!' ;
OP_ARITH: '+' | '-' | '*' | '/' | '%' ;
OP_EQUAL: '=' ;
OP_ASSEQ: ':=' ;
COLON: ':' ;

// Separators
PAREN_OPEN: '(' ;
PAREN_CLOSE: ')' ;  
BRACE_OPEN: '{' ;
BRACE_CLOSE: '}' ;  
BRACK_OPEN: '[' ;
BRACK_CLOSE: ']' ;
SEPARATOR_COMMA: ',' ;        
SEPARATOR_SEMI: ';' ;
OP_DOT: '.' ;

TYPE: 'int' | 'float' | 'boolean' | 'string' | 'array' | 'struct' | 'interface';
BOOLLIT: 'true' | 'false' ;
NILLIT: 'nil' ;
RETURN: 'return' ;
CONTINUE: 'continue' ;
BREAK: 'break' ;
KEYWORD: 'if' | 'else' | 'for' | 'func' | 'type'|
        'const' | 'var' | 'range' ;

FLOATLIT:  DIGITS FRAC EXP?;
fragment DIGIT: [0-9];
fragment DIGITS: '0' | DIGIT+;
fragment FRAC: '.'DIGIT*;
fragment EXP: [Ee][+-]? DIGITS;
INTLIT: DECIMAL_LITERAL | BINARY_LITERAL | OCTAL_LITERAL | HEXADECIMAL_LITERAL ;
STRLIT: '"' STRING_CHAR* '"' ;
fragment STRING_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];
ID: [a-zA-Z_][a-zA-Z0-9_]* ;


DECIMAL_LITERAL: [1-9] [0-9]* | '0' ;
BINARY_LITERAL: '0' [bB] [01]+ ;
OCTAL_LITERAL: '0' [oO] [0-7]+ ;
HEXADECIMAL_LITERAL: '0' [xX] [0-9a-fA-F]+ ;

nl:(NEWLINE|SEPARATOR_SEMI)|(EOF);
NEWLINE
    : ((' ')* '\r'? '\n')+ {
            if self.preType in [
                MiniGoLexer.ID,
                MiniGoLexer.INTLIT,
                MiniGoLexer.FLOATLIT,
                MiniGoLexer.STRLIT,
                MiniGoLexer.BOOLLIT,
                MiniGoLexer.NILLIT,     
                MiniGoLexer.TYPE,
                MiniGoLexer.RETURN,
                MiniGoLexer.CONTINUE,
                MiniGoLexer.BREAK,
                MiniGoLexer.PAREN_CLOSE,
                MiniGoLexer.BRACK_CLOSE,
                MiniGoLexer.BRACE_CLOSE,
            ] :
                self.text = ';'
            else:
                self.skip()
         }
    ;

WS : [ \t\r\f]+ -> skip ;
MULTILINE_COMMENT
    : '/*' (MULTILINE_COMMENT | .)*? '*/' -> skip;

COMMENT: '//' ~[\r\n]* -> skip ;



//ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STRING_CHAR* ('\n'|'\r'|EOF) {
    self.text = self.text.rstrip('\r\n')  
    raise UncloseString(self.text)
};

ILLEGAL_ESCAPE:'"' STRING_CHAR* ESC_ILLEGAL{
    raise IllegalEscape(self.text[:])
};
