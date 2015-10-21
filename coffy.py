# Andres G. Cavazos - A01195067
# Manuel Viejo Gonzalez - A01195222
import ply.yacc as yacc
import coffl #Importa la info del lexer
import sys

# Lista de tokens del lexer
tokens = coffl.tokens

# Funciones de las reglas gramaticales

#Estructura general del programa
#CLASES VARIABLES FUNCION PRINCIPAL
def p_programa(p):
	'''programa : p1 p2 p3 principal'''
	
def p_p1(p):
	'''p1 : empty
			| clases p1'''
			
def p_p2(p):
	'''p2 : empty
			| funcion p2'''
			
def p_p3(p):
	'''p3 : empty
			| variables p3'''

#Funcion principal donde arranca el programa
#funcion TIPO principal PARAMETROS { variables estatuto RETORNA expresion;}
def p_principal(p):
	'''principal : PRINCIPAL pr1 ID parametros BIZQ pr2 BDER'''

def p_pr1(p):
	'''pr1 : tiposimple
			| VACIO'''

def p_pr2(p):
	'''pr2 : pr21 pr22'''

def p_pr22(p):
	'''pr21 : empty
			| estatuto pr21'''

def p_pr23(p):
	'''pr22 : empty
			| RETORNA expresion PUNTOYCOMA'''

#Tipos de datos
def p_tipo(p):
	'''tipo : ENTERO
			| DECIMAL
			| TEXTO
			| ID'''

#Declaracion de variables
def p_variables(p):
	'''variables : tipo v1 PUNTOYCOMA'''

def p_v1(p):
	'''v1 : ID v2'''

def p_v2(p):
	'''v2 : empty
			| IGUAL valordeclaracion v6
			| v3
			| CIZQ CTEENT CDER v4'''
		
def p_v3(p):
	'''v3 : COMA v1'''

def p_v4(p):
	'''v4 : v6
			| IGUAL CIZQ valordeclaracion v5 CDER v6'''
			
def p_v5(p):
	'''v5 : empty
			| COMA valordeclaracion v5'''			
def p_v6(p):
	'''v6 : empty
			| v3'''
	
#Valor para las declaraciones de variables
def p_valordeclaracion(p):
	'''valordeclaracion : CTEENT
							| CTEDEC
							| CTETEXTO'''

#Valor para asignaciones y operaciones
def p_valor(p):
	'''valor : valordeclaracion
				| ID va1'''

def p_va1(p):
	'''va1 : empty
				| PIZQ expresion va2 PDER
				| CIZQ CTEENT CDER va3
				| va4'''

def p_va2(p):
	'''va2 : empty
				| COMA expresion va2'''

def p_va3(p):
	'''va3 : empty
				| va4'''
			
def p_va4(p):
	'''va4 : PUNTO ID va5'''
	
def p_va5(p):
	'''va5 : empty
				| PIZQ expresion va2 PDER'''

#Tipo simple
def p_tiposimple(p):
	'''tiposimple : ENTERO
					| DECIMAL
					| TEXTO'''
					
#Parametros que se mandan a las funciones o metodos
def p_parametros(p):
	'''parametros : PIZQ pa1 PDER'''

def p_pa1(p):
	'''pa1 : empty 
			| tiposimple pa2 ID pa3'''

def p_pa2(p):
	'''pa2 : empty
			| AMP'''

def p_pa3(p):
	'''pa3 : empty
			| COMA pa1'''

#LLamar una funcion desde un estatuto
def p_llamarfunmet(p):
	'''llamarfunmet : ID ll1 PIZQ ll2 PDER PUNTOYCOMA'''

def p_ll1(p):
	'''ll1 : empty
			| PUNTO ID'''
	
def p_ll2(p):
	'''ll2 : empty
			| expresion ll3'''

def p_ll3(p):
	'''ll3 : empty
			| COMA expresion ll3'''
			
#Expresion 
def p_expresion(p):
	'''expresion : declaracion ex1'''

def p_ex1(p):
	'''ex1 : empty
			| CONDICIONY expresion
			| CONDICIONO expresion'''

#Declaracion Comparacion de expresiones
def p_declaracion(p):
	'''declaracion : exp de1'''
	
def p_de1(p):
	'''de1 : empty
			| de2 exp'''
			
def p_de2(p):
	'''de2 : MAYQUE
			| MENQUE
			| IGUALQUE
			| DIF
			| MAYIGUALQUE
			| MENIGUALQUE'''

#EXP
def p_exp(p):
	'''exp : termino exp1'''
	
def p_exp1(p):
	'''exp1 : empty
			| SUMA exp
			| RESTA exp'''
	
#Termino
def p_termino(p):
	'''termino : factor t1'''
	
def p_t1(p):
	'''t1 : empty
			| MULT termino
			| DIV termino'''

#Factor
def p_factor(p):
	'''factor : f1 valor
				| PIZQ expresion PDER'''
				
def p_f1(p):
	'''f1 : empty
			| SUMA
			| RESTA'''
			
#Funcion
def p_funcion(p):
	'''funcion : FUNCION fun1 ID parametros BIZQ fun2 BDER'''

def p_fun1(p):
	'''fun1 : tipo
			| VACIO'''

def p_fun2(p):
	'''fun2 : fun21 fun22'''

def p_fun22(p):
	'''fun21 : empty
			| estatuto fun21'''

def p_fun23(p):
	'''fun22 : empty
			| RETORNA expresion PUNTOYCOMA'''
			
#Bloque
def p_bloque(p):
	'''bloque : BIZQ b1 BDER'''

def p_b1(p):
	'''b1 : empty
			| estatuto b1'''

def p_bloquesimple(p):
	'''bloquesimple : BIZQ bs1 BDER'''

def p_bs1(p):
	'''bs1 : empty
			| estatutosimple b1'''

			
#Asignacion
def p_asignacion(p):
	'''asignacion : ID a1 a2 IGUAL expresion PUNTOYCOMA'''

def p_a1(p):
	'''a1 : empty
			| PUNTO ID'''	

def p_a2(p):
	'''a2 : empty
			| CIZQ expresion CDER'''		
		
#Mientras
def p_mientras(p):
	'''mientras : MIENTRAS PIZQ expresion PDER bloquesimple'''
	
#Estatuto
def p_estatuto(p):
	'''estatuto : variables
				| EJEC llamarfunmet
				| ASIGNA asignacion
				| mientras
				| si
				| escritura
				| lectura'''
	
#Estatuto que evita variables de bloque en los mientras	
def p_estatutosimple(p):
	'''estatutosimple : EJEC llamarfunmet
				| ASIGNA asignacion
				| mientras
				| si
				| escritura
				| lectura'''

#Escritura
def p_escritura(p):
	'''escritura : IMPRIMIR PIZQ expresion e1 PDER PUNTOYCOMA'''
			
def p_e1(p):
	'''e1 : empty
			| COMA expresion e1'''

#Lectura CHECAR
def p_lectura(p):
	'''lectura : LEER PIZQ ID l1 l2 PDER PUNTOYCOMA'''
			
def p_l1(p):
	'''l1 : empty
			| PUNTO ID'''
	
def p_l2(p):
	'''l2 : empty
			| CIZQ expresion CDER'''
			
#SI (IF)
def p_si(p):
	'''si : SI PIZQ expresion PDER bloque si1'''
			
def p_si1(p):
	'''si1 : empty
			| O bloque'''
			
#Clase
def p_clases(p):
	'''clases : CLASE ID cl1 BIZQ atributos metodos BDER'''

def p_cl1(p):
	'''cl1 : empty
			| EXTIENDE ID'''
			
#Atributos
def p_atributos(p):
	'''atributos : ATRIBUTOS DOSPUNTOS atr1'''

def p_atr1(p):
	'''atr1 : empty
			| variables atr1'''
			
#Metodos
def p_metodos(p):
	'''metodos : METODOS DOSPUNTOS met1'''

def p_met1(p):
	'''met1 : empty
			| funcion met1'''
			
#Vacio
def p_empty(p):
	'''empty : '''

# Funcion de manejo de errores
def p_error(token):
	print ("Error de sintaxis '%s' en la linea %s " % (token.value, token.lineno))
	global error
	error = 0

# Construye el parser
yacc.yacc()

# Lee el archivo dado y determina si esentrada exitosa o error
error = 1
try:
	f = open(sys.argv[1], "r") 
	s = f.readlines()
	entry = ""
	for line in s:
		entry += line
	yacc.parse(entry)
	if error:
		print("Programa Exitoso")
except EOFError:
	print ("No se pudo abrir el archivo %s." % sys.argv[1])
