grammar coff;

options {
  language=Python2;
}

//=======================================================
// Reglas de gramatica
//=======================================================



programa : p1 p2 p3 principal
    ;

p1 : clases p1
    | 
    ;

p2 : variables p2
    | 
    ;

p3 : funcion p3
    | 
    ;

principal : PRINCIPAL pr1 ID parametros BIZQ pr2 BDER
    ;

pr1 : pr11
    | pr12
    ;

pr11 : tiposimple
    ;

pr12 : VACIO
    ;

pr2 : pr21 pr22
    ;

pr21 : estatuto pr21
    | 
    ;

pr22 : RETORNA expresion PUNTOYCOMA
    | 
    ;


tipo : ENTERO
    | DECIMAL
    | TEXTO
    | ID
    ;


variables : tipo v1 PUNTOYCOMA
    ;

v1 : ID v2
    ;

v2 : CIZQ CTEENT CDER v4
    | IGUAL valordeclaracion v6
    | v3
    | 
    ;   

v3 : COMA v1
    ;

v4 : v6
    | IGUAL CIZQ valordeclaracion v5 CDER v6
    ;       

v5 : COMA valordeclaracion v5
    |           
    ;
    
v6 : v3
    | 
    ;

valordeclaracion : CTEENT
    | CTEDEC
    | CTETEXTO
    ;

valor : valordeclaracion
    | ID va1
    ;

va1 : va4
    | PIZQ expresion va2 PDER
    | CIZQ CTEENT CDER
    | 
    ;

va2 : COMA expresion va2
    | 
    ;

va3 : va4
    | 
    ;       

va4 : PUNTO ID va5
    ;

va5 : PIZQ expresion va2 PDER
    | 
    ;

tiposimple : ENTERO
    | DECIMAL
    | TEXTO
    ;               

parametros : PIZQ pa1 PDER
    ;

pa1 : pa11 
    | 
    ;

pa11 : tiposimple pa2 ID pa3
    ;

pa2 : AMP
    | 
    ;

pa3 : COMA pa1
    | 
    ;

llamarfunmet : ID ll1 PIZQ ll2 PDER PUNTOYCOMA
    ;

ll1 : PUNTO ID
    | 
    ;

ll2 : expresion ll3
    | 
    ;

ll3 : COMA expresion ll3
    | 
    ;   

expresion : declaracion ex1
    ;

ex1 : CONDICIONO expresion
    | CONDICIONY expresion
    | 
    ;

declaracion : exp de1
    ;

de1 : de2 exp
    | 
    ;   

de2 : MAYQUE
    | MENQUE
    | IGUALQUE
    | DIF
    | MAYIGUALQUE
    | MENIGUALQUE
    ;

exp : termino exp1
    ;
    
exp1 : RESTA exp
    | SUMA exp
    | 
    ;
    
termino : factor t1
    ;

t1 : DIV termino
    | MULT termino
    | 
    ;

factor : f1 valor
    | PIZQ expresion PDER
    ;       

f1 : RESTA
    | SUMA
    | 
    ;
            

funcion : FUNCION fun1 ID parametros BIZQ fun2 BDER
    ;

fun1 : fun11
    | fun12
    ;

fun11 : tipo
    ;

fun12 : VACIO
    ;

fun2 : fun21 fun22
    ;

fun21 : estatuto fun21
    | 
    ;

fun22 : RETORNA expresion PUNTOYCOMA
    | 
    ;

bloque : BIZQ b1 BDER
    ;

b1 : estatuto b1
    | 
    ;

bloquesimple : BIZQ bs1 BDER
    ;

bs1 : estatutosimple b1
    | 
    ;

asignacion : ID a1 a2 IGUAL expresion PUNTOYCOMA
    ;

a1 : PUNTO ID
    |   
    ;

a2 : CIZQ expresion CDER
    |       
    ;

mientras : MIENTRAS PIZQ expresion PDER bloquesimple
    ;

estatuto : variables
    | EJEC llamarfunmet
    | ASIGNA asignacion
    | mientras
    | si
    | escritura
    | lectura
    ;

estatutosimple : EJEC llamarfunmet
    | ASIGNA asignacion
    | mientras
    | si
    | escritura
    | lectura
    ;

escritura : IMPRIMIR PIZQ expresion e1 PDER PUNTOYCOMA
    ;

e1 : COMA expresion e1
    | 
    ;

lectura : LEER PIZQ ID l1 l2 PDER PUNTOYCOMA
    ;

l1 : PUNTO ID
    | 
    ;

l2 : CIZQ expresion CDER
    | 
    ;

si : SI PIZQ expresion PDER bloque si1
    ;

si1 : O bloque
    | 
    ;

clases : CLASE ID cl1 cl2
    ;

cl1 : EXTIENDE ID
    | 
    ;

cl2 : BIZQ atributos metodos BDER
    ;

atributos : ATRIBUTOS DOSPUNTOS atr1
    ;

atr1 : variables atr1
    | 
    ;       

metodos : METODOS DOSPUNTOS met1
    ;

met1 : funcion met1
    | 
    ;




//=============================================
//Tokens
//=============================================


IMPRIMIR:                'imprimir';
LEER:                    'leer';
VACIO:                   'vacio';
MIENTRAS:                'mientras';
ENTERO:                  'entero';
DECIMAL:                 'decimal';
TEXTO:                   'texto';
RETORNA:                 'retorna';
CLASE:                   'clase';
FUNCION:                 'funcion';
EXTIENDE:                'extiende';
ATRIBUTOS:               'atributos';
METODOS:                 'metodos';
PRINCIPAL:               'principal';
SI:                      'si';
O:                       'o';
EJEC:                    'ejec';
ASIGNA:                  'asigna';
PIZQ:                    '(' ;
PDER:                    ')' ;
BIZQ:                    '{' ;
BDER:                    '}' ;
CIZQ:                    '[' ;
CDER:                    ']' ;
SUMA:                    '+' ;
RESTA:                   '-' ;
DIV:                     '/' ;
MULT:                    '*' ;
IGUALQUE:                '==';
IGUAL:                   '=' ;
MENQUE:                  '<' ;
MAYQUE:                  '>' ;
MAYIGUALQUE:             '>=';
MENIGUALQUE:             '<=';
DIF:                     '!=';
CONDICIONO:              '||' ;
CONDICIONY:              '&&' ;
AMP:                     '&' ;
COMA:                    ',' ;
PUNTOYCOMA:              ';' ;
DOSPUNTOS:               ':' ;
PUNTO:                   '.' ;
ID:                      [a-zA-Z][a-zA-Z0-9]* ;
CTEENT:                  '-'?DIGIT+ ;
CTEDEC:                  '-'?DIGIT+'.'DIGIT+ ;
CTETEXTO:                  '"' ( WS | ~('"'|'\\') )* '"' ;
WS                      : 
                        ( ' '
                        | '\t'
                        | '\r'    
                        | '\n'    
                        )
                        -> skip
                        ;
fragment DIGIT : '0'..'9' ;