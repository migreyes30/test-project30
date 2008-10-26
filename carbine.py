# File: carbine.py
    
import ply.lex as lex
import ply.yacc as yacc

#--------------------------------------------------------------------
# Scanner definition

class CarbineException(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)
	#pass
	
class CarbineExceptionCiclo(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)
	#pass


tokens = (
    'IS',       'COMA',       'DOSPUNTOS', 'END',       'ENTERO',   'ID',
    'IF',       'ELSE',       'FOR',      'WHILA',     'RETURN',   'READ',
    'SUMMON',   'MAS',        'MENOS',    'PARDER',    'PARIZQ',   'POR',
    'WRITE',    'THEN',       'VAR',      'MAYOR',     'MAYORIGUAL','BREAK',
    'MENOR',    'MENORIGUAL', 'IGUAL',    'NOIGUAL',   'IN',
    'FUNC',     'ENTRE',      'MODULO',   'POTENCIA',  'CORCHIZQ', 'CORCHDER',
    'CADENA',   'AND',        'OR',	  'DECIMAL',    'PUNTOCOMA') 
 
t_COMA      = r','
t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_MAS       = r'[+]'
t_MENOS     = r'[-]'
t_POR       = r'[*]'
t_ENTRE     = r'[/]'
t_MODULO    = r'[%]'
t_POTENCIA  = r'\^'
t_MAYOR     = r'>'
t_MAYORIGUAL= r'>='
t_MENOR     = r'\<'
t_MENORIGUAL= r'<='
t_PARDER    = r'[)]'
t_PARIZQ    = r'[(]'
t_CORCHIZQ  = r'[\[]'
t_CORCHDER  = r'[\]]'
t_AND 	    = r'&&'
t_OR 	    = r'\|\|'

reservadas = {
    'is':       'IS',
    'end':      'END',
    'siis':	'IGUAL',
    'nois':	'NOIGUAL',
    'if':       'IF',
    'else':     'ELSE',
    'for':      'FOR',
    'whila':    'WHILA',
    'return':   'RETURN',
    'read':     'READ',
    'summon':   'SUMMON',
    'write':    'WRITE',    
    'then':     'THEN',
    'var':      'VAR',
    'break':    'BREAK',
    'in':       'IN',
    'func':     'FUNC'
}    

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t    

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]\w*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = str(t.value)
    return t

t_ignore = ' \t'

def t_comentario(t):
    r'@.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    raise CarbineException("Illegal character '%s'" % t.value[0])

lex.lex()

#--------------------------------------------------------------------
# Parser definition

raiz = None

def p_programa(p):
    '''programa : variables enunciados
    '''
    global raiz
    p[0] = [p[1], p[2]]
    raiz = p[0]
    
def p_vacio(p):
    'vacio :'
    pass        

                
def p_enunciados(p):
    '''enunciados : enunciado enunciados
                  | vacio
    '''
    if len(p) == 2:
        p[0] = []        
    else:
        p[0] = [p[1]] + p[2]        
        
def p_enunciado(p):
    '''enunciado : enunciado_print
                 | enunciado_loop
                 | enunciado_if
                 | enunciado_read
                 | enunciado_asignacion
                 | enunciado_invocar
                 | enunciado_declaracion
                 | enunciado_return
		 | enunciados_ciclos
		 | variables
		 | expresion_comparacion
    '''
    p[0] = p[1]

def p_variables(p):
    '''variables     : VAR ID mas_variables
		     | VAR enunciado_asignacion mas_variables
		     | vacio
    '''

    if len(p) == 2:
        p[0] = []                
    else:
        p[0] = [p[1], p[2]] + p[3]

def p_mas_variables(p):
    '''mas_variables : COMA ID mas_variables
		     | COMA enunciado_asignacion mas_variables
		     | vacio
    '''

    if len(p) == 2:
        p[0] = []                
    else:
        p[0] = [p[2]] + p[3]

def p_enunciado_print(p):
    'enunciado_print : WRITE expresion'
    p[0] = [p[1], p[2]]                                    

def p_enunciado_loop(p):
    '''enunciado_loop : enunciado_whila
                      | enunciado_for
    '''
    p[0] = p[1]                                    

def p_enunciados_ciclos(p):
    '''enunciados_ciclos : enunciados
                         | BREAK
    '''
    if isinstance(p[1],list):
	    p[0] = p[1]
    else:
	    p[0] = [p[1]]
    
def p_expresion_condicion(p):
    '''expresion_condicion : expresion_suma
                           | expresion_comparacion
    '''
    p[0]=p[1]

def p_enunciado_whila(p):
    'enunciado_whila : WHILA expresion_condicion THEN enunciados_ciclos END'
    p[0] = [p[1], p[2], p[4]]

def p_expfor(p):
	'''expfor : lista
		  | CADENA
		  | ID
		  | expresion_lista
		  | enunciado_invocar
	'''
	p[0] = p[1]

def p_enunciado_for(p):
    'enunciado_for : FOR ID IN expfor enunciados_ciclos END'
    p[0] = [p[1], p[2], p[4], p[5]]

def p_enunciado_if(p):
    'enunciado_if : IF expresion_condicion THEN enunciados END enunciado_else'
    p[0] = [p[1], p[2], p[4]] + p[6]

def p_enunciado_else(p):
    '''enunciado_else : ELSE enunciados END enunciado_else
    		      | vacio
    '''
    if len(p) == 2:
        p[0] = []        
    else:
        p[0] = [p[1], p[2]] + p[4]
    
def p_enunciado_read(p):
    'enunciado_read : READ expresion'
    p[0] = [p[1], p[2]]

def p_enunciado_asignacion(p):
    '''enunciado_asignacion : ID IS expresion
				| expresion_lst IS expresion
    '''
    p[0] = [p[2], p[1], p[3]]

def p_enunciado_invocar(p):
    'enunciado_invocar : SUMMON ID PARIZQ parametros PARDER'
    p[0] = [p[1], p[2], p[4]]

def p_enunciado_declaracion(p):
    'enunciado_declaracion : FUNC ID PARIZQ parametrosf PARDER enunciados END'
    p[0] = [p[1], p[2], p[4], p[6]]


def p_parametrosf(p):
    '''parametrosf : ID mas_elementosf
    		   | ID IS expresion mas_elementosf
    		  | vacio
    '''
    if len(p) == 2:
        p[0] = []
    elif len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
	p[0]= [[p[2],p[1],p[3]]] + p[4]

def p_mas_elementosf(p):
	'''mas_elementosf : COMA ID mas_elementosf
			 | COMA ID IS expresion mas_elementosf
                         | vacio
	'''
	if len(p) == 2:
		p[0] = []
	elif len(p) == 4:
		p[0] = [p[2]] + p[3]
	else:
		p[0]= [[p[2],p[3],p[4]]] + p[5]

def p_enunciado_return(p):
    'enunciado_return : RETURN expresion'
    p[0] = [p[1], p[2]]

def p_expresion(p):
    '''expresion : expresion_suma
                 | expresion_comparacion
                 | expresion_concatenacion
    '''
    p[0] = p[1]

	
def p_expresion_lista(p):
	''' expresion_lista : ID CORCHIZQ DOSPUNTOS CORCHDER 
                            | ID CORCHIZQ limite DOSPUNTOS CORCHDER 
                            | ID CORCHIZQ DOSPUNTOS limite CORCHDER
                            | ID CORCHIZQ limite DOSPUNTOS limite CORCHDER 
   	'''
	if len(p) == 5:
		p[0] = ['funlist',p[2], p[4] , p[1]]
	elif len(p) == 6:
		p[0] = ['funlist',p[2], p[3], p[4], p[5] , p[1]]
	else:
		p[0] = ['funlist',p[2], p[3], p[4], p[5], p[6] , p[1]]

def p_expresion_lst(p):
	'expresion_lst : ID CORCHIZQ pos CORCHDER '
	
	p[0]= ['lst',p[3], p[1]]

def p_pos(p):
    '''pos : ENTERO
	      | MENOS pos
	      | ID
	      | expresion_condicion
	      | PARIZQ pos PARDER
    '''
    if len(p) == 3:
        p[0] = [p[1], p[2]]
    elif len(p)== 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_limite(p):
    '''limite : ENTERO
	      | MENOS limite
	      | ID
	      | expresion_condicion
	      | PARIZQ limite PARDER
	      | vacio
    '''
    if len(p) == 3:
        p[0] = [p[1], p[2]]
    elif p[1] == None:
        p[0] = [] 
    elif len(p)== 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_parametros(p):
    '''parametros : expresion mas_elementos
    		  | vacio
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]	
	
def p_expresion_suma(p):
    '''expresion_suma  : expresion_mul operador_suma expresion_suma
    		       | expresion_mul 
                      
       expresion_mul   : expresion_pow operador_mul expresion_mul
                       | expresion_pow 

       expresion_pow   : expresion_simple POTENCIA expresion_simple
       		       | expresion_simple
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = [p[2], p[1], p[3]]        

def p_operador_suma(p):
    '''operador_suma : MAS
                     | MENOS'''
    p[0] = p[1]

def p_operador_mul(p):
    '''operador_mul  : POR
                     | ENTRE
                     | MODULO
    '''
    p[0] = p[1]



def p_expresion_comparacion(p):
    '''expresion_comparacion : expresion operador_comparacion expresion2'''
    p[0] = [p[2], p[1], p[3]]

def p_expresion2(p):
	''' expresion2 : expresion_suma
                       | expresion_comparacion
                       | expresion_concatenacion
	'''
	p[0] = p[1]
	
def p_operador_comparacion(p):
    '''operador_comparacion : AND
                            | OR
                            | MAYOR
                            | MENOR
                            | MAYORIGUAL
                            | MENORIGUAL
                            | IGUAL
                            | NOIGUAL
    '''
    p[0] = p[1]



def p_expresion_concatenacion(p):
    'expresion_concatenacion : concatenables PUNTOCOMA concatenables mas_cadenas'
    p[0] = [p[2], p[1], p[3]] + p[4]

def p_concatenables(p):
    '''concatenables : CADENA
		    | ID
		    | ENTERO
		    | lista
		    | enunciado_invocar
    '''
    
    p[0] = p[1]

def p_mas_cadenas(p):
    '''mas_cadenas : PUNTOCOMA concatenables mas_cadenas
    		   | vacio
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1], p[2]] + p[3]

def p_lista(p):
    '''lista   :  CORCHIZQ CORCHDER
               |  CORCHIZQ expresion mas_elementos CORCHDER
    '''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]

def p_mas_elementos(p):
	'''mas_elementos : COMA expresion mas_elementos
                         | vacio
	'''
	if len(p) == 2:
		p[0] = []
	else:
		p[0] = [p[2]] + p[3]

def p_expresion_simple(p):
    '''expresion_simple : ID
                        | ENTERO
                        | MENOS expresion_simple
                        | PARIZQ expresion PARDER
			| expresion_lista
			| expresion_lst
                        | enunciado_invocar
                        | enunciado_asignacion
                        | lista
                        | CADENA
			| DECIMAL
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:    
        p[0] = [p[1], p[2]]
    else:
        p[0] = p[2]
        

def p_error(p):
    raise CarbineException(
        "Unexpected end of input" if p == None else "Syntax error at line %d in '%s'" % (p.lineno, p.value))

yacc.yacc()

#--------------------------------------------------------------------
# Facade for this module 

def parse(input):
    yacc.parse(input)
    return raiz 
