from carbine import parse, CarbineException, CarbineExceptionCiclo
from types import *
from ext_func import *
from copy import copy

#funciones con d is 3
#Scope de variables
#listas->[['lst', 'i', 'nombres']]
#valores[j] concatenar con eso y summon....
#----------------------------------------------------------------------------------------------
#Auxiliares

def valorVar(table,lsta):
	for i in xrange(len(lsta)):
		if isinstance(lsta[i],list):
			valorVar(table,lsta[i])
		elif isinstance(lsta[i],str) and '"' not in lsta[i]:
			lsta[i]=table[lsta[i]]
	return table,lsta


def quitarstr(xlst):
	for i in range(len(xlst)):
		if isinstance(xlst[i],str):
			xlst[i]=quitar(xlst[i])
		elif isinstance(xlst[i],list):
			quitar(xlst[i])
	return xlst


def quitar(x):
	y=''
	for i in x:
		if i != '\"':
			y= y + i
	return y


def poner(x):
	y='"'
	for i in x:
		y= y + i
	y=y+'"'
	return y


def tipolista(x):#indica si es lista
	return isinstance(x,list)


def tipostr(x):#indica donde estan los string
        if x != '[' and x != ']'and x != ':':
                return 1
        else:
                return 0


def tipostr2(x):#indica si existe una cadena 
        if isinstance(x,str):
                if '"' in x:
                        return 1
                else:
                        return 0
        else:
                return 0


def indicestr(y):#indice donde esta la variable
    for i in y:
        if '"' not in i:
            return y.index(i)


def indicesummon(y):#indice donde esta summon
    for i in y:
        if i[0] in statement_dict:
            return y.index(i)


def tipoenlst(x):#regresa lista de tipos de elementos
    lst=[]
    for i in x:
        lst.append(type(i))
    return lst


def posList(y):#posicion de la listas
        for i in y:
                if type(i) is ListType:
                        return y.index(i)
                


def posString(y):#posicion del string
        for i in y:
                if type(i) is StringType:
                        return y.index(i)


def posInteger(y):#posicion del entero
        for i in y:
                if type(i) is IntType:
                        return y.index(i)


def mismotipo(x):#Elementos de lst mismo tipo
    if type(x[0]) == type(x[1]):
        return True
    else:
        return False



#----------------------------------------------------------------------------------------------
#End of Auxiliares
#----------------------------------------------------------------------------------------------

def create_table(lst):
        vardict = {
            'isletra' : impl_isletra,
            'isnum' : impl_isnum,
            'len' : impl_len,
            'islower' : impl_islower,
            'isupper' : impl_isupper,
            'isspace' : impl_isspace,
            'upper' : impl_upper,
            'lower' : impl_lower,
            'append' : impl_append,
            'insert' : impl_insert,
            'remove' : impl_remove,
            'sort' : impl_sort,
	    	'reverse' : impl_reverse,
            'pop' : impl_pop,
            'num' : impl_num,
            'str' : impl_str,
            'list' : impl_list,
            'endswith' : impl_endswith,
            'startswith' : impl_startswith,
            'split' : impl_split,
            'strip' : impl_strip,
            'find' : impl_find,
	    	'raiz' : impl_raiz,
	    	'range': impl_range,
	    	'forward': impl_forward,
	    	'get_parameter_value': impl_getParamVal,
	    	'get_parameter_values': impl_getParamVals,
	    	'get_parameter_names': impl_getParamNames,
	    	'get_header_value':impl_getHeaderVal,
	    	'get_header_names':impl_getHeadersNames,
	    	'set_header_value':impl_setHeaderValue,
			'get_session_value':impl_getSessionValue,
			'set_session_value':impl_setSessionValue
            }
	for i in xrange(1,len(lst)):
		if isinstance(lst[i],list):
			x = lst[i]
			if x[1] in vardict:
				raise CarbineException("Duplicate variable: '%s'" % x[1])
			vardict[x[1]] = 0
			statement_dict[x[0]](vardict,x[1:])
		else:
			if lst[i] in vardict:
				raise CarbineException("Duplicate variable: '%s'" % lst[i])
			vardict[lst[i]] = 0
	return vardict


def eval_expr(table, expr):
	if isinstance(expr, int):
		return expr
	if isinstance(expr, str) and '"' not in expr:
		if expr in table:
			return table[expr]
		else:
			raise CarbineException("Undefined variable: '%s'" % expr)
	if isinstance(expr, str) and '"' in expr:
		expr=quitar(expr)
		return expr
	if len(expr) == 0:
		return expr
	elif (expr[0] not in uniop_dict) and (expr[0] not in binop_dict) and (expr[0] not in statement_dict):
		return expr
	elif len(expr) == 2:
		try:
			return uniop_dict[expr[0]](eval_expr(table,expr[1]))
		except TypeError:
			raise CarbineException("not supported operatation: '%s'" % expr[1])
	else:
		if expr[0] != 'funlist' and expr[0] != 'summon' and expr[0] !='lst' and expr[0] != ';':
			try:
				final= binop_dict[expr[0]](eval_expr(table, expr[1]),eval_expr(table, expr[2]))
			except TypeError:
				raise CarbineException("not supported operatation for operators: '%s' and '%s'" % (expr[1],expr[2]))
			if isinstance(final,str):
				final=poner(final)
			return final
		else:
			return statement_dict[expr[0]](table,expr[1:])


salida =[]

def execute_write(table, args):
        global salida
	temp = args[0]
	if isinstance(args[0],int) or '"' in args[0]:
		tempWrite = args[0]
		#print tempWrite
		salida.append(str(tempWrite))
	elif isinstance(args[0],list):
		if len(temp) > 0:
			if temp[0] in statement_dict:
				tempWrite=statement_dict[temp[0]](table,temp[1:])
				#print tempWrite
				salida.append(str(tempWrite))
			elif temp[0] in uniop_dict or temp[0] in binop_dict:
				tempWrite=eval_expr(table,args[0])
				#print tempWrite
				salida.append(str(tempWrite))
			else:
				waka=valorVar(table,args[0])
				table=waka[0]
				args[0]=waka[1]
				tempWrite = args[0]
				#print tempWrite
				salida.append(str(tempWrite))
		else:
			tempWrite = args[0]
			#print tempWrite
			salida.append(str(tempWrite))
	else:
		tempWrite=eval_expr(table,args[0])
		#print tempWrite
		salida.append(str(tempWrite))


def execute_if(table, args):
	temp = args[0]
	if 'else' in args:
		if isinstance(args[0],list):
			if len(temp) == 0:
				if eval_expr(table,args[0]):
					execute_statements(table, args[1])
				else:
					execute_statements(table, [args[2:]])
			else:	
				if temp[0] in statement_dict:
					raise CarbineException("wrong sentence: '%s'" % temp[0])
				elif temp[0] in uniop_dict or temp[0] in binop_dict:
					if eval_expr(table,args[0]):
						execute_statements(table, args[1])
					else:
						execute_statements(table, [args[2:]])
				else:
					if args[0]:
						execute_statements(table, args[1])
					else:
						execute_statements(table, [args[2:]])
		else:
			if args[0]:
				execute_statements(table, args[1])
			else:
				execute_statements(table, [args[2:]])
	else:
		if isinstance(args[0],list):
			if len(temp) == 0:
				if eval_expr(table,args[0]):
					execute_statements(table, args[1])
			else:
				if temp[0] in statement_dict:
					raise CarbineException("wrong sentence: '%s'" % temp[0])
				elif temp[0] in uniop_dict or temp[0] in binop_dict:
					if (isinstance(temp[1],str) and '"' not in temp[1]):
						print temp[1]
						temp[1]=table[temp[1]]
						print temp[1]
					if (isinstance(temp[2],str) and '"' not in temp[2]):
						temp[2]=table[temp[2]]
					#print args[0]
					if eval_expr(table,args[0]):
						execute_statements(table, args[1])
				else:
					if args[0]:
						execute_statements(table, args[1])
		else:
			if args[0]:
				execute_statements(table, args[1])


def execute_else(table, args):
	temp = args[0]
	if 'else' in args:
		execute_statements(table,temp)
		execute_statements(table, [args[1:]])
	else:
		execute_statements(table,temp)


def execute_var(table, args):
	for i in xrange(0,len(args)):
		if isinstance(args[i],list):
			x = args[i]
			if x[1] in table:
				raise CarbineException("Duplicate variable: '%s'" % x[1])
			table[x[1]] = 0
			statement_dict[x[0]](table,x[1:])
		else:
			if args[i] in table:
				raise CarbineException("Duplicate variable: '%s'" % args[i])
			table[args[i]] = 0
	return table
	
	
def execute_for(table, args):
	if args[0] in table:
		#variable iterable declarada
		if isinstance(args[1],str):
			#elemento iterado ID o cadena
			if '"' in args[1]:
				#cadena
				var=args[0]
				lst=quitar(args[1])
				it=iter(lst)
				try:
					while True:
						table[var]=it.next()
						try:
							execute_statements(table, args[2])
						except CarbineExceptionCiclo:
							break
				except StopIteration:
							pass
			else:
				if (args[1] in table and isinstance(table[args[1]],list)) or (args[1] in table and isinstance(table[args[1]],str)):
					#ID
					args[1]=table[args[1]]
					execute_for(table, args)
				else:
					raise CarbineException("Undefined variable or variable not a list: '%s'" % args[1])
		elif isinstance(args[1],list):
			temp=args[1]
			if len(temp) > 0:
				if temp[0] in statement_dict:
					args[1]=eval_expr(table,args[1])
					execute_for(table,args)
				else:
					#lista
					var=args[0]
					lst=args[1]
					it=iter(lst)
					try:
						while True:
							table[var]=it.next()
							try:
								execute_statements(table, args[2])
							except CarbineExceptionCiclo:
								break
					except StopIteration:
								pass
			else:
				#lista vacia
				var=args[0]
				lst=args[1]
				it=iter(lst)
				try:
					while True:
						table[var]=it.next()
						try:
							execute_statements(table, args[2])
						except CarbineExceptionCiclo:
							break
				except StopIteration:
							pass
        else:
                raise CarbineException("Undefined variable: '%s'" % args[0])



def execute_whila(table, args):
	if isinstance(args[0],list):
		temp = args[0]
		if len(temp) == 0:
			while eval_expr(table,args[0]):
				try:
					execute_statements(table, args[1])
				except CarbineExceptionCiclo:
					break
		else:
			if temp[0] in statement_dict:
				if temp[0] == 'funlist'or temp[0] =='lst' or temp[0] == 'summon':
					while eval_expr(table,args[0]):
						try:
							execute_statements(table, args[1])
						except CarbineExceptionCiclo:
							break
				else:
					raise CarbineException("wrong condicion: '%s'" % temp[0])
			elif temp[0] in uniop_dict or temp[0] in binop_dict:
				while eval_expr(table,args[0]):
					try:
						execute_statements(table, args[1])
					except CarbineExceptionCiclo:
						break
			else:
				while args[0]:
					try:
						execute_statements(table, args[1])
					except CarbineExceptionCiclo:
						break
	else:
		while args[0]:
			try:
				execute_statements(table, args[1])
			except CarbineExceptionCiclo:
				break
			
			
def execute_break(table, args):
	raise CarbineExceptionCiclo("break")



def execute_is(table, args):
	if isinstance(args[0],list):
		#se quiere modificar una lista
		t=args[0]
		if t[-1] in table:
			#la variable existe en la tabla
			if isinstance(table[t[-1]],list):
				#la variable es una lista
				val=table[t[-1]]
				#val es igual a la lista que se modificara
				if isinstance(args[1],int) or '"' in args[1]:
					#se va a modificar con un entero o una cadena
					pos=eval_expr(table, t[1])
					try:
						val[pos]= args[1]
					except TypeError:
						raise CarbineException("invalid parameter: '%s'" % pos)
					table[t[-1]]=val
					return table[t[-1]]
				elif isinstance(args[1],list):
					#se va a modificar con una lista
					temp = args[1]
					if len(temp) == 0:
						waka=valorVar(table,args[1])
						table=waka[0]
						args[1]=waka[1]
						pos=eval_expr(table, t[1])
						try:
							val[pos]= args[1]
						except TypeError:
							raise CarbineException("invalid parameter: '%s'" % pos)
						table[t[-1]]=val
						return table[t[-1]]
					else:
						if temp[0] in statement_dict:
							#es un statement el nuevo valor
							pos=eval_expr(table, t[1])
							try:
								val[pos]= statement_dict[temp[0]](table,temp[1:])
							except TypeError:
								raise CarbineException("invalid parameter: '%s'" % pos)
							table[t[-1]] = val
							return table[t[-1]]
						elif temp[0] in uniop_dict or temp[0] in binop_dict:
							#es una suma,comparacion o negacion
							pos=eval_expr(table, t[1])
							try:
								val[pos]= eval_expr(table, args[1])
							except TypeError:
								raise CarbineException("invalid parameter: '%s'" % pos)
							table[t[-1]] = val
							return table[t[-1]]
						else:
							#lista
							waka=valorVar(table,args[1])
							table=waka[0]
							args[1]=waka[1]
							pos=eval_expr(table, t[1])
							try:
								val[pos]= args[1]
							except TypeError:
								raise CarbineException("invalid parameter: '%s'" % pos)
							table[t[-1]]=val
							return table[t[-1]]
				else:
					#se va a modificar con un ID
					if args[1] in table:
						pos=eval_expr(table, t[1])
						try:
							val[pos]=table[args[1]]
						except TypeError:
							raise CarbineException("invalid parameter: '%s'" % pos)
						table[t[-1]]=val
						return table[t[-1]]
					else:
						raise CarbineException("Undefined variable: '%s'" % args[1])	
			else:
				raise CarbineException("Variable: '%s' is not a list" % t[-1]) [['lst', 0, 'y'], 'z']
		else:
			raise CarbineException("Undefined variable: '%s'" % args[0])	
	elif args[0] in table:
		if args[0] not in reserved_words:
			temp = args[1]
			if isinstance(args[1],int) or '"' in args[1]:
				table[args[0]] = args[1]
				return table[args[0]]
			elif isinstance(args[1],list):
				if len(temp) != 0:
					if temp[0] in statement_dict:
						table[args[0]] = statement_dict[temp[0]](table,temp[1:])
						return table[args[0]]
					elif temp[0] in uniop_dict or temp[0] in binop_dict:
						table[args[0]] = eval_expr(table, args[1])
						return table[args[0]]
					else:
						waka=valorVar(table,args[1])
						table=waka[0]
						args[1]=waka[1]
						table[args[0]] = args[1]
						return table[args[0]]
				else:
					waka=valorVar(table,args[1])
					table=waka[0]
					args[1]=waka[1]
					table[args[0]] = args[1]
					return table[args[0]]
			else:
				table[args[0]] = eval_expr(table, args[1])
				return table[args[0]]
		else:
			raise CarbineException("variable: '%s' pre-established as a function" % args[0])
	else:
		raise CarbineException("Undefined variable: '%s'" % args[0])
		
		
def execute_summon(table, args):
	global salida
	if args[0] in table:
		temp=table[args[0]]
		if type(temp)== TupleType:
			tabla_local={
				'isletra' : impl_isletra,
				'isnum' : impl_isnum,
				'len' : impl_len,
				'islower' : impl_islower,
				'isupper' : impl_isupper,
				'isspace' : impl_isspace,
				'upper' : impl_upper,
				'lower' : impl_lower,
				'append' : impl_append,
				'insert' : impl_insert,
				'remove' : impl_remove,
				'sort' : impl_sort,
				'reverse' : impl_reverse,
				'pop' : impl_pop,
				'num' : impl_num,
				'str' : impl_str,
				'list' : impl_list,
				'endswith' : impl_endswith,
				'startswith' : impl_startswith,
				'split' : impl_split,
				'strip' : impl_strip,
				'find' : impl_find,
				'raiz' : impl_raiz,
				'range': impl_range,
				'forward': impl_forward,
				'get_parameter_value': impl_getParamVal,
				'get_parameter_values': impl_getParamVals,
				'get_parameter_names': impl_getParamNames,
				'get_header_value':impl_getHeaderVal,
				'get_header_names':impl_getHeadersNames,
				'set_header_value':impl_setHeaderValue,
				'get_session_value':impl_getSessionValue,
				'set_session_value':impl_setSessionValue
				}
			param=temp[0]
			state=temp[1]
			#hayList=tipoenlst(param)
			#numList=hayList.count(ListType)
			#necParam=len(param)-numList
			# if ListType in hayList
			# or len(args[1]) >= necParam
			if len(param) == len(args[1]):
				argsTemp=args[1]
				#param=[['is', 'c', 6]]
				#state=[['write', 'c']]
				#argsTemp=args[1]=[]
				#['x', []]
				for i in xrange(len(param)):
					if isinstance(argsTemp[i],list):
						#parametro es lista
						tempfor=argsTemp[i]
						if len(tempfor) == 0:
							tabla_local[param[i]]=tempfor
						else:
							if tempfor[0] in uniop_dict or tempfor[0] in binop_dict or tempfor[0] in statement_dict:
								#menos,suma comparacion
								#funlist,lst,summon,concatenar
								la=eval_expr(table, tempfor)
								tabla_local[param[i]]=la
							elif tempfor[0] != 'is':
								#lista
								tabla_local[param[i]]=tempfor
							else:
								raise CarbineException("invalid parameter, can\'t asign: '%s' " % tempfor)
					else:
						#parametro es un ID, entero,cadena
						if isinstance(argsTemp[i],int):
							#entero
							tabla_local[param[i]]=argsTemp[i]
						else:
							#ID o Cadena
							if '"' in argsTemp[i]:
								#cadena
								tabla_local[param[i]]=argsTemp[i]
							else:
								#ID
								la=eval_expr(table,argsTemp[i])
								tabla_local[param[i]]=la
				try:
					return execute_statements(tabla_local, state)
				except CarbineException,e:
					return e.value
			else:
				raise CarbineException("invalid number of parameters: '%i' received, needed '%i'" % (len(args[1]),len(param)))
		elif type(temp) == FunctionType:
			valorPara= copy(args[1])
			if len(valorPara) == 0:
				valorPara.append(table)
				return table[args[0]](valorPara)
			elif len(valorPara) == 1:
				if isinstance(valorPara[0],list):
					tempfun=valorPara[0]
					if len(tempfun) == 0:
						valorPara[0]=valorPara[0]
					else:
						if tempfun[0] in uniop_dict or tempfun[0] in binop_dict or tempfun[0] in statement_dict:
							#menos,suma,comparacion
							#funlist,lst,summon,concatenar
							valorPara[0]=eval_expr(table, tempfun)
							return execute_summon(table,[args[0],valorPara])
						else:
							valorPara[0]=valorPara[0]
				elif isinstance(valorPara[0],str) and '"' not in valorPara[0]:
					#el parametro es un ID
					try:
						valorPara[0]=table[valorPara[0]]
					except KeyError:
						raise CarbineException("variable is not a define: '%s'" % valorPara[0])
					else:
						if args[0] == 'forward' or args[0] == 'get_parameter_value' or args[0] == 'get_parameter_values' or args[0] == 'get_parameter_names'or args[0] == 'get_header_value':
							print args
							valorPara.append(table)
					#	return execute_summon(table,[args[0],valorPara])
				
				elif isinstance(valorPara[0],str) and '"' in valorPara[0]:
					#es una cadena el parametro
					if args[0] == 'forward' or args[0] == 'get_parameter_value' or args[0] == 'get_parameter_values' or args[0] == 'get_parameter_names'or args[0] == 'get_header_value':
						valorPara.append(table)
					valorPara[0]=valorPara[0]
					#valorPara[0]=quitar(valorPara[0])
				else:
					valorPara[0]=valorPara[0]
				
				if args[0] == 'forward':
					salidaF=table[args[0]](valorPara)
					salidaF.append(salida)
					salida = salidaF
					return salida
				else:
					return table[args[0]](valorPara)
			elif len(valorPara) == 2:
				#primer parametro
				if isinstance(valorPara[0],list):
					#posible expresion a evaluar como primer argumento
					tempfun=valorPara[0]
					if len(tempfun) == 0:
						valorPara[0]=valorPara[0]
					else:
						try:
							if tempfun[0] in uniop_dict or tempfun[0] in binop_dict or tempfun[0] in statement_dict:
								#menos,suma comparacion
								#funlist,lst,summon,concatenar
								valorPara[0]=eval_expr(table, tempfun)
								return execute_summon(table,[args[0],valorPara])
							else:
								valorPara[0]=valorPara[0]
						except TypeError:
							valorPara[0]=valorPara[0]
				elif isinstance(valorPara[0],str) and '"' not in valorPara[0]:
					#el primer parametro es un ID
					try:
						valorPara[0]=table[valorPara[0]]
					except KeyError:
						raise CarbineException("variable is not a define: '%s'" % valorPara[0])
					#else:
					#return execute_summon(table,[args[0],valorPara])
						
				elif isinstance(valorPara[0],str) and '"' in valorPara[0]:
					#es una cadena el parametro
					#if args[0] != 'append':
					#	valorPara[0]=valorPara[0]
						#valorPara[0]=quitar(valorPara[0])
					#else:
					valorPara[0]=valorPara[0]
				else:
					valorPara[0]=valorPara[0]
						
				#segundo parametro
				if isinstance(valorPara[1],list):
					#posible expresion a evaluar de elemento a evaluar
					tempfun=valorPara[1]
					if len(tempfun) == 0:
						valorPara[1]=valorPara[1]
					else:
						if tempfun[0] in uniop_dict or tempfun[0] in binop_dict or tempfun[0] in statement_dict:
							#menos,suma comparacion
							#funlist,lst,summon,concatenar
							valorPara[1]=eval_expr(table, tempfun)
							return execute_summon(table,[args[0],valorPara])
						else:
							valorPara[1]=valorPara[1]
				elif isinstance(valorPara[1],str) and '"' not in valorPara[1]:
					#es un ID el segundo parametro
					try:
						valorPara[1]=table[valorPara[1]]
					except KeyError:
						raise CarbineException("variable is not a define: '%s'" % valorPara[1])
					#else:
					#	return execute_summon(table,[args[0],valorPara])
						
				elif isinstance(valorPara[1],str) and '"' in valorPara[1]:
					#es una cadena el parametro
					valorPara[0]=valorPara[0]
					#valorPara[1]=quitar(valorPara[1])			
				else:
					#es una entero el parametro
					valorPara[1]=valorPara[1]
					
				if args[0]=='set_header_value':
					headerNew=table[args[0]](valorPara)
					try:
						tempsal=salida[0]
					except IndexError:
						tempsal=""
					if isinstance(tempsal,list):
						tempsal.append(headerNew)
					else:
						salida.insert(0,[headerNew])
				else:
					return table[args[0]](valorPara)
			elif len(valorPara) == 3:
				for i in xrange(len(valorPara)):
					if isinstance(valorPara[i],list):
						tempfun=valorPara[i]
						if len(tempfun) == 0:
							valorPara[i]=valorPara[i]
						else:
							if tempfun[0] in uniop_dict or tempfun[0] in binop_dict or tempfun[0] in statement_dict:
								valorPara[i]=eval_expr(table, tempfun)
								return execute_summon(table,[args[0],valorPara])
							else:
								valorPara[i]=valorPara[i]
					elif isinstance(valorPara[i],str) and '"' not in valorPara[i]:
						try:
							valorPara[i]=table[valorPara[i]]
						except KeyError:
							raise CarbineException("variable is not a define: '%s'" % valorPara[i])
						#else:
						#	return execute_summon(table,[args[0],valorPara])
					elif isinstance(valorPara[i],str) and '"' in valorPara[i]:
						valorPara[0]=valorPara[0]
						#valorPara[i]=quitar(valorPara[i])
					else:
						valorPara[i]=valorPara[i]
				return table[args[0]](valorPara)
			else:
				for i in xrange(len(valorPara)):
					if isinstance(valorPara[i],list):
						tempfun=valorPara[i]
						if len(tempfun) == 0:
							valorPara[i]=valorPara[i]
						else:
							if tempfun[0] in uniop_dict or tempfun[0] in binop_dict or tempfun[0] in statement_dict:
								valorPara[i]=eval_expr(table, tempfun)
								return execute_summon(table,[args[0],valorPara])
							else:
								valorPara[i]=valorPara[i]
					elif isinstance(valorPara[i],str) and '"' not in valorPara[i]:
						try:
							valorPara[i]=table[valorPara[i]]
						except KeyError:
							raise CarbineException("variable is not a define: '%s'" % valorPara[i])
						#else:
						#	return execute_summon(table,[args[0],valorPara])
					elif isinstance(valorPara[i],str) and '"' in valorPara[i]:
						valorPara[i]=quitar(valorPara[i])
					else:
						valorPara[i]=valorPara[i]
				return table[args[0]](valorPara)
		else:
			raise CarbineException("variable is not a function: '%s'" % args[0])
		
	else:
		raise CarbineException("Undefined funtion: '%s'" % args[0])


def execute_func(table, args):
	table[args[0]] = (args[1], args[2])
	return table


def execute_return(table, args):
	if isinstance(args[0],list):
		temp=args[0]
		if len(temp) == 0:
			raise CarbineException(args[0])
		else:
			if temp[0] in statement_dict:
				la=statement_dict[temp[0]](table,temp[1:])
				raise CarbineException(la)
			elif temp[0] in uniop_dict or temp[0] in binop_dict:
				la=eval_expr(table, temp)
				raise CarbineException(la)
			else:
				waka=valorVar(table,args[0])
				table=waka[0]
				args[0]=waka[1]
				raise CarbineException(args[0])
	elif isinstance(args[0],int) or '"' in args[0]:
		raise CarbineException(args[0])
	else:
		la=eval_expr(table, args[0])
		raise CarbineException(la)


def execute_concatenar(table, args):
		if len(args)== 2:
			#2 elementos por concatenar
			if mismotipo(args):
				#mimso tipo
				if type(args[0]) is StringType:
					#string
					if '"' in args[0] and '"' in args[1]:
						#ambos elementos son cadenas
						args[0]=quitar(args[0])
						args[1]=quitar(args[1])
						temp=args[0]+args[1]
						temp=poner(temp)
						return temp
					elif '"' in args[0] or '"' in args[1]:
						#un elemento es una cadena
						cadena=indicestr(args)
						args[cadena]=eval_expr(table,args[cadena])
						return execute_concatenar(table,args)
					elif args[0] in table and args[1] in table:
						#ID
						args[0]=eval_expr(table,args[0])
						args[1]=eval_expr(table,args[1])
						return execute_concatenar(table,args)
					else:
						#variables no registradas o solo una 
						raise CarbineException("Undefined variable(s): '%s','%s'" % (args[0],args[1]))
				elif type(args[0]) is ListType:
					#lista o summon
					temp1=args[0]
					temp2=args[1]
					if temp1 == [] or temp2 == []:
						return args[0]+args[1]
					else:
						if temp1[0] not in statement_dict and temp2[0] not in statement_dict:
							#ambos elementos son listas
							return args[0]+args[1]
						elif temp1[0] not in statement_dict or temp2[0] not in statement_dict:
							#un elemento es un summon
							lista=indicesummon(args)
							temp=args[lista]
							args[lista]=statement_dict[temp[0]](table,temp[1:])
							return execute_concatenar(table,args)
						else:
							#ambos elementos son summon
							args[0]=statement_dict[temp1[0]](table,temp1[1:])
							args[1]=statement_dict[temp2[0]](table,temp2[1:])
							return execute_concatenar(table,args)
				else:
					#enteros
					raise CarbineException("Can't concatenate int elements, should use '+' operator: '%s','%s'" % (args[0],args[1]))
			else:
				#dif tipo
				listatipos=tipoenlst(args)
				if ListType in listatipos:
					#un elemento es una lista o summon
					posLst=posList(args)
					templst=args[posLst]
					if templst == []:
						posStr=posString(args)
						if IntType in listatipos:
							raise CarbineException("Can't concatenate an int with a list: '%s','%s'" % (args[0],args[1]))
						elif '"' in args[posStr]:
							args[posStr]=quitar(args[posStr])
							args[posLst]=str(args[posLst])
							tempelement=args[0]+args[1]
							tempelement=poner(tempelement)
							return tempelement
						else:
							args[posStr]=eval_expr(table,args[posStr])
							return execute_concatenar(table,args)
					else:
						if templst[0] not in statement_dict:
							#un elemento es lista
							posStr=posString(args)
							if IntType in listatipos:
								#lista con entero
								raise CarbineException("Can't concatenate an int with a list: '%s','%s'" % (args[0],args[1]))
							elif '"' in args[posStr]:
								#cadena con lista
								args[posStr]=quitar(args[posStr])
								args[posLst]=str(args[posLst])
								tempelement=args[0]+args[1]
								tempelement=poner(tempelement)
								return tempelement
							else:
								#lista con ID
								args[posStr]=eval_expr(table,args[posStr])
								return execute_concatenar(table,args)
						else:
							#summon con (ID o cadena o entero)
							posStr=posString(args)
							if IntType in listatipos:
								#summon con entero
								args[posLst]=statement_dict[templst[0]](table,templst[1:])
								return execute_concatenar(table,args)
							elif '"' in args[posStr]:
								#summon con cadena
								args[posLst]=statement_dict[templst[0]](table,templst[1:])
								return execute_concatenar(table,args)
							else:
								#summon con ID
								args[posLst]=statement_dict[templst[0]](table,templst[1:])
								args[posStr]=eval_expr(table,args[posStr])
								return execute_concatenar(table,args)
				else:
					#un elemento es entero
					posInt=posInteger(args)
					posStr=posString(args)
					if '"' in args[posStr]:
						#entero con cadena
						args[posStr]=quitar(args[posStr])
						args[posInt]=str(args[posInt])
						tempelement=args[0]+args[1]
						tempelement=poner(tempelement)
						return tempelement
					else:
						#entero con ID
						args[posStr]=eval_expr(table,args[posStr])
						return execute_concatenar(table,args)
		else:
			#muchos elementos por concatenar
			first2ele=[args.pop(0),args.pop(0)]
			accum=execute_concatenar(table,first2ele)
			args.insert(0,accum)
			while len(args)> 1:
				ele2conc=[args.pop(0),args.pop(1)]
				args.pop(0)
				accum=execute_concatenar(table,ele2conc)
				args.insert(0,accum)
			return args[0]


def execute_funlist(table, args):
        if args[-1] in table:
                #variable existe
                if isinstance(table[args[-1]],list) or isinstance(table[args[-1]],str):
                        #variable es una lista
                        lista=eval_expr(table,args[-1])
			if lista == []:
				raise CarbineException("List is empty: '%s'" % lista)
                        if len(args) == 3:
                                #no hay limites
                                return lista
                        nostrings=map(tipostr,args)
                        nostrings.pop()
                        cadena=map(tipostr2,args)
                        if 1 in cadena:
                                #existe un string como limite
                                ind= cadena.index(1)
                                raise CarbineException("String in limit: '%s'" % args[ind])
                        elif len(args) == 5:
                                #solo se brinda un limite
                                numstr2=nostrings.index(1)
                                if isinstance(args[numstr2],list):
                                        #limite dado una expresion o lista o statement
                                        temp1=args[numstr2]
                                        if temp1[0] in statement_dict or isinstance(temp1[0],int):
                                                #limite dado es una lista o un statement
                                                raise CarbineException("Wrong limit: '%s'" % temp)
                                        elif numstr2 == 1:
                                                #limite inferior dado (expresion)
                                                return lista[eval_expr(table,args[1]):]
                                        else:
                                                #limite superior dado (expresion )
                                                return lista[:eval_expr(table,args[2])]
                                else:
                                        if numstr2 == 1:
                                                #limite inferior dado (ID o entero)
                                                return lista[eval_expr(table,args[1]):]
                                        else:
                                                #limite superior dado (ID o entero)
                                                return lista[:eval_expr(table,args[2])]
                        else:
                                #se brindaron los 2 limites
                                if isinstance(args[1],list) or isinstance(args[3],list):
                                        #un limite es una lista (expresion o lista o statement)
                                        listas=map(tipolista,args)
                                        numlst=listas.count(True)
                                        lstindex=listas.index(True)
                                        if numlst == 2:
                                                #los dos limites son expresiones o listas o statements
                                                temp1=args[1]
                                                temp2=args[0]
                                                if temp1[0] in statement_dict or temp2[0] in statement_dict or isinstance(temp1[0],int) or isinstance(temp2[0],int):
                                                        #Uno o los dos limites son statements o listas
                                                        raise CarbineException("Wrong limits: '%s' and '%s'" % (args[1],args[3]))
                                                else:
                                                        #los dos limites son expresiones
                                                        return lista[eval_expr(table,args[1]):eval_expr(table,args[3])]
                                        else:
                                                #solo una limite es expresion o lista o statement
                                                temp3 = args[lstindex]
                                                if temp3[0] in statement_dict or isinstance(temp3[0],int):
                                                        #Un limite es un statement o una lista
                                                        raise CarbineException("Wrong limits: '%s' and '%s'" % (args[1],args[3]))
                                                else:
                                                        #limites correctos
                                                        return lista[eval_expr(table,args[1]):eval_expr(table,args[3])]
                                else:
                                        #limites dados son ID o enteros
                                        return lista[eval_expr(table,args[1]):eval_expr(table,args[3])]
                else:
                        #variable no es lista
                        raise CarbineException("Variable: '%s' is not a list" % args[-1])
        else:
                #variable no declarada
                raise CarbineException("Undefined variable: '%s'" % args[-1])


def execute_lst(table,args):
	if args[-1] in table:
		#la varaible existe
		#print "lst->",args
		if isinstance(table[args[-1]],list) or isinstance(table[args[-1]],str):
			#variable es una lista
			cadena=map(tipostr2,args)
			lista=eval_expr(table,args[-1])
			if lista == []:
				raise CarbineException("List is empty: '%s'" % lista)
			if 1 in cadena:
				#una cadema como parametro
				ind= cadena.index(1)
				raise CarbineException("Invalid parameter: '%s'" % args[ind])
			if isinstance(args[0],list):
				#parametro es una lista
				temp=args[0]
				if temp[0] in uniop_dict or temp[0] in binop_dict:
					#parametro es una suma o comparacion o menos
					return lista[eval_expr(table,args[0])]
				elif temp[0] == 'lst' or temp[0] == 'summon':
					#parametro es una expresion lista o invocacion
					try:
						return lista[statement_dict[temp[0]](table,temp[1:])]
					except TypeError:
						#el valor que se regreso no son enteros
						raise CarbineException("Invalid parameter: '%s'" % args[0])
				else:
					#parametros son una lista o los statement asignacion o expresion lista
					raise CarbineException("Invalid parameter: '%s'" % args[0])
			else:
				#parametro es ID o entero
				try:
					return lista[eval_expr(table,args[0])]
				except TypeError:
					raise CarbineException("Invalid parameter: '%s'" % eval_expr(table,args[0]))
		else:
			#variable no es una lista
			raise CarbineException("Variable: '%s' is not a list" % args[-1])
	else:
		#variable no declarada
		raise CarbineException("Undefined variable: '%s'" % args[-1])


def execute_statements(table, statements):
        for s in statements:
                statement_dict[s[0]](table, s[1:])


def interpret(input,*tabla_ext):
	global salida
	salida = []
	ast = parse(input)
	if tabla_ext == ():
		table = create_table(ast[0])
	else:
		if isinstance(tabla_ext[0],dict):
			table = tabla_ext[0]
		else:
			temp_tu=tabla_ext[0]
			table = create_table(ast[0])
			table[temp_tu[0]]=temp_tu[1]
			temphead=temp_tu[2]
			table[temphead[0]]= temphead[1]
	execute_statements(table, ast[1])
	return salida


uniop_dict = {
    '-': lambda x: -x
}
      
binop_dict = {
    '<': lambda x, y: int(x < y),
    '>': lambda x, y: int(x > y),
    '<=': lambda x, y: int(x <= y),
    '>=': lambda x, y: int(x >= y),
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y,
    '^': lambda x, y: x ** y,
    '&&': lambda x, y: int (x and y),
    '||': lambda x, y: int(x or y),
    'siis': lambda x, y: int (x == y),
    'nois': lambda x, y: int (x != y)
}
    
    
statement_dict = {
    'write': execute_write,
    'break': execute_break,
    'if': execute_if,
    'else': execute_else,
    'var': execute_var,
    'for': execute_for,
    'whila': execute_whila,
    'is': execute_is,
    'summon': execute_summon,
    'func': execute_func,
    'return': execute_return,
    ';' : execute_concatenar,
    'funlist' : execute_funlist,
    'lst' : execute_lst
}


reserved_words = ['isletra','isnum','len','islower','isletra','isupper',
                  'isspace','upper','lower','append','insert','remove',
                  'sort','pop','num','str','list','endswith','startswith',
                  'split','strip','find','reverse','raiz','range','forward',
                  'get_parameter_value','get_parameter_values','get_parameter_names',
                  'get_header_value','get_header_names','set_header_value',
                  'get_session_value','set_session_value']

##Fin
#'read': execute_read
#def execute_read(table,args)
