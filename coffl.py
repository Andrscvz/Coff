# Andres G. Cavazos - A01195067
# Manuel Viejo Gonzalez - A01195222

import ply.lex as lex

# Lista de palabras reservadas
reservadas = {
	'imprimir' 	: 'IMPRIMIR',
	'leer' 		: 'LEER',
	'vacio' 	: 'VACIO',
	'mientras' 	: 'MIENTRAS',
	'entero' 	: 'ENTERO',
	'decimal' 	: 'DECIMAL',
	'texto'		: 'TEXTO',
	'retorna' 	: 'RETORNA',
	'clase' 	: 'CLASE',
	'funcion' 	: 'FUNCION',
	'imprimir' 	: 'IMPRIMIR',
	'extiende' 	: 'EXTIENDE',
	'atributos' : 'ATRIBUTOS',
	'metodos'	: 'METODOS',
	'principal' : 'PRINCIPAL',
	'si' 		: 'SI',
	'o' 		: 'O',
	'ejec'		: 'EJEC',
	'asigna'	: 'ASIGNA'
}

# Lista de tokens
tokens = [	'IGUAL',		'MAYQUE',		'MENQUE',		'DIF',
			'IGUALQUE',		'MAYIGUALQUE',	'MENIGUALQUE',	'CONDICIONY', 'CONDICIONO',
			'SUMA',			'RESTA',		'MULT',			'DIV',		
			'PUNTOYCOMA',	'DOSPUNTOS',	'COMA',			'PUNTO',
			'BIZQ',			'BDER',			'PIZQ',			'PDER',
			'CIZQ',			'CDER',			'CTEENT',		'CTEDEC',		
			'CTETEXTO',		'AMP',			'ID'] + list(reservadas.values())

# Declaracion correspondiente a cada token con su expresion regular

t_ignore 			= ' \t'

t_PIZQ  			= r'\('
t_PDER  			= r'\)'
t_BIZQ 				= r'\{'
t_BDER 				= r'\}'
t_CIZQ 				= r'\['
t_CDER 				= r'\]'

t_CTEENT 			= r'[\+-]?\d+'
t_CTEDEC 			= r'[\+-]?\d+\.\d+'
t_CTETEXTO 			= r'\'.*\''

t_IGUAL  			= r'='
t_SUMA    			= r'\+'
t_RESTA   			= r'-'
t_MULT			   	= r'\*'
t_DIV  				= r'/'

t_MAYQUE      		= r'>'
t_MENQUE      		= r'<'
t_IGUALQUE  		= r'=='
t_MAYIGUALQUE  		= r'>='
t_MENIGUALQUE  		= r'<='
t_DIF		   		= r'!='
t_CONDICIONY   		= r'&&'
t_CONDICIONO   		= r'\|\|'

t_PUNTOYCOMA   		= r';'
t_PUNTO 			= r'\.'
t_DOSPUNTOS 		= r':'
t_COMA   			= r'\,'
t_AMP				= r'&'


# Regla para ID que checa palabras reservadas
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# Regla para rastrear el numero de lineas
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Regla para manejo de comentarios
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
	
# Regla de manejo de errores
def t_error(t):
	print("Error - '", t.value[0], "' - en linea - ", t.lexer.lineno)
	t.lexer.skip(1)

# Construir el lexer
lex.lex()