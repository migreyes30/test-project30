from carbine import parse, CarbineException,CarbineExceptionCiclo
from types import *
from math import sqrt
from os.path import *

def ponerenFun(x):
	y='"'
	for i in x:
		y= y + i
	y=y+'"'
	return y
	
def quitar(x):
	y=''
	for i in x:
		if i != '\"':
			y= y + i
	return y

def impl_raiz(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if isinstance(args[0],int):
        val= sqrt(float(args[0]))
        return int(val) 
    else:
        raise CarbineException("Tipo de dato no aceptado")

    
def impl_len(args):
	if len(args) != 1:
		raise CarbineException("Numero incorrecto de argumentos")
	if not(isinstance(args[0], list) or isinstance(args[0], str)):
		raise CarbineException("Tipo de dato no aceptado")
	if isinstance(args[0], str):
 		args[0]=quitar(args[0])
	return len(args[0])

def impl_isletra(args):
	if len(args) != 1:
		raise CarbineException("Numero incorrecto de argumentos")
	if not isinstance(args[0], str):
		raise CarbineException("No se introdujo un string como parametro")
	args[0]=quitar(args[0])
	return int(args[0].isalpha())


def impl_isnum(args):
	if len(args) != 1:
		raise CarbineException("Numero incorrecto de argumentos")
	if not isinstance(args[0], str):
		raise CarbineException("No se introdujo un string como parametro")
	args[0]=quitar(args[0])
	return int(args[0].isdigit())


def impl_islower(args):
	if len(args) != 1:
		raise CarbineException("Numero incorrecto de argumentos")
	if not isinstance(args[0], str):
		raise CarbineException("No se introdujo un string como parametro")
	args[0]=quitar(args[0])
	return int(args[0].islower())
    

def impl_isupper(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], str):
        raise CarbineException("No se introdujo un string como parametro")
    args[0]=quitar(args[0])
    return int(args[0].isupper())

def impl_isspace(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], str):
        raise CarbineException("No se introdujo un string como parametro")
    args[0]=quitar(args[0])
    return int(args[0].isspace())
  

def impl_upper(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], str):
        raise CarbineException("No se introdujo un string como parametro")
    args[0]=quitar(args[0])
    upStr= ponerenFun(args[0].upper())
    return upStr

def impl_lower(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], str):
        raise CarbineException("No se introdujo un string como parametro")
    args[0]=quitar(args[0])
    downStr= ponerenFun(args[0].lower())
    return downStr

#append(lista, elem)
def impl_append(args):
	if len(args) != 2:
		raise CarbineException("Numero incorrecto de argumentos")
	if not isinstance(args[0], list):
		raise CarbineException("No se introdujo una lista como parametro")
	args[0].append(args[1])
	return args[0]

#insert(lista, index, elem)
def impl_insert(args):
    if len(args) != 3:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], list):
        raise CarbineException("No se introdujo una lista como parametro")
    if isinstance(args[1],int):
        args[0].insert(args[1], args[2])
        return args[0]
    else:
        raise CarbineException("No se introdujo un entero como posicion")
            
#remove(lista, elem)
def impl_remove(args):
	if len(args) != 2:
		raise CarbineException("Numero incorrecto de argumentos")
	if not isinstance(args[0], list):
		raise CarbineException("No se introdujo una lista como parametro")
	try:
		args[0].remove(args[1])
	except ValueError:
		raise CarbineException("Elemento no en lista")
	else:
		return args[0]

#sort(lista)
def impl_sort(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], list):
        raise CarbineException("No se introdujo una lista como parametro")

    args[0].sort()  # aqui podriamos poner si quieren un return
                             # de la lista que se crea
    return args[0]

def impl_reverse(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], list):
        raise CarbineException("No se introdujo una lista como parametro")

    args[0].reverse()  # aqui podriamos poner si quieren un return
                             # de la lista que se crea
    return args[0]

#pop(lista)
def impl_pop(args):
    if not(len(args) == 1 or len(args)==2):
            raise CarbineException("Numero incorrecto de argumentos")
    if not isinstance(args[0], list):
            raise CarbineException("No se introdujo una lista como parametro")
    if len(args) == 1:
            if len(args[0]) == 0:
                    raise CarbineException("Lista vacia")
            else:
                    return args[0].pop()
    else:
            if not isinstance(args[1],int):
                    raise CarbineException("No se introdujo una posicion correcta (int) %s" % args[1])
            elif args[1] >= len(args[0]):
                    raise CarbineException("Posicion fuera de rango")
            else:
                    return args[0].pop(args[1])
            
            

def impl_num(args):
    if len(args)!= 1:
        raise CarbineException('Numero incorrecto de argumentos')
    if isinstance(args[0],str):
        args[0]=quitar(args[0])
        if not args[0].isdigit():
            raise CarbineException('El argumento necesita tener unicamente digitos')
        return int(args[0])
    elif isinstance(args[0],int):
        return int(args[0])
    else:
        raise CarbineException('El argumento debe ser un string')

def impl_str(args):
    if len(args)!= 1:
        raise CarbineException('Numero incorrecto de argumentos')
    if not(isinstance(args[0],list) or isinstance(args[0],int) or isinstance(args[0],str)):
        raise CarbineException('El argumento no puede ser de ese tipo')
    if not isinstance(args[0],str):
        listaStr= ponerenFun(str(args[0]))
    else:
	    listaStr=args[0]
    return listaStr

def impl_list(args):
    if len(args)!= 1:
        raise CarbineException('Numero incorrecto de argumentos')
    if not(isinstance(args[0],list) or isinstance(args[0],str)):
        raise CarbineException('El argumento no puede ser de ese tipo')
    if isinstance(args[0],str): 
        args[0]=quitar(args[0])
        listaList= map(ponerenFun,list(args[0]))
    else:
        listaList= list(args[0])
    return listaList

#manejo de expeciones para las funciones stratswith y endswith y find 
def exep_fourargs(args):
    if not(len(args)> 1 and len(args)<5):
        raise CarbineException('Numero incorrecto de argumentos')
    if not(isinstance(args[0],str) or isinstance(args[1],str)):
        raise CarbineException("No se introdujo un string como parametro")
    if len(args) > 2:
        if not isinstance(args[2],int):
            raise CarbineException("El parametro %s deber ser un entero" %(args[2]))
    if len(args) > 3:
        if not isinstance(args[3],int):
            raise CarbineException("El parametro %s deber ser un entero" %(args[3]))

def impl_endswith(args):
    exep_fourargs(args)
    if len(args)== 2:
        if isinstance(args[0],str) and isinstance(args[1],str):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].endswith(args[1]))
        else:
            raise CarbineException("parametros necesarios (str,str) recibidos (%s,%s)" %(type(args[0]),type(args[1]))) 
    if len(args)== 3:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].endswith(args[1],args[2]))
        else:
            raise CarbineException("parametros necesarios (str,str,int) recibidos (%s,%s,%s)" %(type(args[0]),type(args[1]),type(args[2]))) 
    if len(args)== 4:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int) and isinstance(args[3],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].endswith(args[1],args[2],args[3]))
        else:
            raise CarbineException("parametros necesarios (str,str,int,int) recibidos (%s,%s,%s,%s)" %(type(args[0]),type(args[1]),type(args[2]),type(args[3])))
                         
def impl_startswith(args):
    exep_fourargs(args)
    if len(args)== 2:
        if isinstance(args[0],str) and isinstance(args[1],str):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].startswith(args[1]))
        else:
            raise CarbineException("parametros necesarios (str,str) recibidos (%s,%s)" %(type(args[0]),type(args[1]))) 
    if len(args)== 3:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].startswith(args[1],args[2]))
        else:
            raise CarbineException("parametros necesarios (str,str,int) recibidos (%s,%s,%s)" %(type(args[0]),type(args[1]),type(args[2]))) 
    if len(args)== 4:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int) and isinstance(args[3],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].startswith(args[1],args[2],args[3]))
        else:
            raise CarbineException("parametros necesarios (str,str,int,int) recibidos (%s,%s,%s,%s)" %(type(args[0]),type(args[1]),type(args[2]),type(args[3])))
                         
def impl_split(args):
	if not(len(args)>= 1 and len(args) < 4):
		raise CarbineException('Numero incorrecto de argumentos')
	if len(args) == 2:
		if not(isinstance(args[0],str) or isinstance(args[1],str)):
			raise CarbineException("No se introdujo un string como parametro")
	if len(args) == 3:
		if len(args) > 1:
			if not isinstance(args[2],int):
				raise CarbineException("El parametro %s deber ser un entero" %(args[2]))
	if len(args)== 1:
		if isinstance(args[0],str):
			args[0]=quitar(args[0])
			listaSplit= map(ponerenFun,args[0].split())
			return listaSplit
		else:
			raise CarbineException("El elemento %s deber ser un string" %(args[0]))
	if len(args)== 2:
		if isinstance(args[0],str) and isinstance(args[1],str):
			args[0]=quitar(args[0])
			args[1]=quitar(args[1])
			listaSplit= map(ponerenFun,args[0].split(args[1]))
			return listaSplit
		else:
			raise CarbineException("los parametros %s (%s) y %s (%s) deben ser un strings" %(args[0],type(args[0]),args[1],type(args[1]))) 
	if len(args)== 3:
		if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int):
			args[0]=quitar(args[0])
			args[1]=quitar(args[1])
			listaSplit= map(ponerenFun,args[0].split(args[1],args[2]))
			return listaSplit
		else:
			raise CarbineException("parametros necesarios (str,str,int) recibidos (%s,%s,%s)" %(type(args[0]),type(args[1]),type(args[2]))) 
    

def impl_strip(args):
    if len(args) != 2:
        raise CarbineException("Numero incorrecto de argumentos")
    if not(isinstance(args[0], str) or isinstance(args[1],str)):
        raise CarbineException("No se introdujo un string como parametro")
    if isinstance(args[0],str) and isinstance(args[1],str):
        args[0]=quitar(args[0])
        args[1]=quitar(args[1])
        listaStrip= ponerenFun(args[0].strip(args[1]))
        return  listaStrip
    else:
        raise CarbineException("los parametro %s (%s) y %s (%s) deben ser un strings" %(args[0],type(args[0]),args[1],type(args[1])))
                         
                
def impl_find(args):
    exep_fourargs(args)
    if len(args)== 2:
        if isinstance(args[0],str) and isinstance(args[1],str):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].find(args[1]))
        else:
            raise CarbineException("No se introdujo un string como parametro")
    if len(args)== 3:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].find(args[1],args[2]))
        else:
            raise CarbineException("No se introdujo un string como parametro")
    if len(args)== 4:
        if isinstance(args[0],str) and isinstance(args[1],str) and isinstance(args[2],int) and isinstance(args[3],int):
            args[0]=quitar(args[0])
            args[1]=quitar(args[1])
            return int(args[0].find(args[1],args[2],args[3]))
        else:
            raise CarbineException("No se introdujo un string como parametro")       
    
                
def impl_range(args):
    if len(args)== 1:
        if isinstance(args[0],int):
            return range(args[0])
        else:
            raise CarbineException("No se introdujo un int como parametro")
    if len(args)== 2:
        if isinstance(args[0],int) and isinstance(args[1],int):
            return range(args[0],args[1])
        else:
            raise CarbineException("No se introdujo un int como parametro")
    if len(args)== 3:
        if isinstance(args[0],int) and isinstance(args[1],int) and isinstance(args[2],int):
            return range(args[0],args[1],args[2])
        else:
            raise CarbineException("No se introdujo un int como parametro")
    else:
        raise CarbineException('Numero incorrecto de argumentos')

def impl_forward(args):
    if len(args) != 2:
            raise CarbineException("Numero incorrecto de argumentos")
    if isinstance(args[0],str) and isinstance(args[1],dict):
            args[0]=quitar(args[0])
            return [args[0],args[1],'controladorCarbine']
    else:
            raise CarbineException("el parametro %s (%s) debe ser un string" %(args[0],type(args[0])))
    
def impl_getParamVal(args):
	if len(args) != 2:
		raise CarbineException("Numero incorrecto de argumentos")
	elif isinstance(args[0],str):
		tablaVal=args[1]
		args[0]=quitar(args[0])
		if 'GET' in tablaVal:
			tempget = tablaVal['GET']
			try:
				regreso=ponerenFun(str(tempget[args[0]]))
				return regreso
			except KeyError:
				return 0
		elif 'POST' in tablaVal:
			temppost = tablaVal['POST']
			try:
				regreso=ponerenFun(str(temppost[args[0]]))
				return regreso
			except KeyError:
				return 0
		else:
			raise CarbineException("No GET or POST method call for this page")
	else:
		raise CarbineException("el parametro %s (%s) debe ser un string" %(args[0],type(args[0])))
    
def impl_getParamVals(args):
	if len(args) != 2:
		raise CarbineException("Numero incorrecto de argumentos en param")
	elif isinstance(args[0],str):
		tablaVal=args[1]
		valueReturn=[]
		args[0]=quitar(args[0])
		if 'GET' in tablaVal:	
			tempget = tablaVal['GET']
			tempname=args[0]+"carbineRepeat"
			keysget=tempget.keys()
			try:
				for i in keysget:
					if tempname in i:
						regreso=ponerenFun(str(tempget[i]))
						valueReturn.append(regreso)
				regreso=ponerenFun(str(tempget[args[0]]))
				valueReturn.insert(0,regreso)
				return valueReturn
			except KeyError:
				return []
		elif 'POST' in tablaVal:
			temppost = tablaVal['POST']
			tempname=args[0]+"carbineRepeat"
			keysget=temppost.keys()
			try:
				for i in keysget:
					if tempname in i:
						regreso=ponerenFun(str(temppost[i]))
						valueReturn.append(regreso)
				regreso=ponerenFun(str(temppost[args[0]]))
				valueReturn.insert(0,regreso)
				return valueReturn
			except KeyError:
				return []
		else:
			raise CarbineException("No GET or POST method call for this page")
	else:
		raise CarbineException("el parametro %s (%s) debe ser un string" %(args[0],type(args[0])))
    
def impl_getParamNames(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    elif isinstance(args[0],dict):
	tablaVal=args[0]
	if 'GET' in tablaVal:
		tempget = tablaVal['GET']
		valueReturn = tempget.keys()
		listaFinal=[]
		for i in valueReturn:
			if "carbineRepeat" not in i:
				regreso=ponerenFun(i)
				listaFinal.append(regreso)
		return listaFinal
	elif 'POST' in tablaVal:
		temppost = tablaVal['POST']
		valueReturn = temppost.keys()
		listaFinal=[]
		for i in valueReturn:
			if "carbineRepeat" not in i:
				regreso=ponerenFun(i)
				listaFinal.append(regreso)
		return listaFinal
	else:
		raise CarbineException("No GET or POST method call for this page")
    else:
        raise CarbineException("Problema interno")

def impl_getHeaderVal(args):
    if len(args) != 2:
        raise CarbineException("Numero incorrecto de argumentos")
    elif isinstance(args[0],str):
        tablaVal=args[1]
        if 'HEADERS' in tablaVal:
            temphead = tablaVal['HEADERS']
            args[0]=quitar(args[0])
            try:
                regreso=ponerenFun(str(temphead[args[0]]))
                return regreso
            except KeyError:
                return 0
        else:
            raise CarbineException("No HEADERS for this page")
    else:
        raise CarbineException("el parametro %s (%s) debe ser un string" %(args[0],type(args[0])))


def impl_getHeadersNames(args):
    if len(args) != 1:
        raise CarbineException("Numero incorrecto de argumentos")
    elif isinstance(args[0],dict):
        tablaVal=args[0]
        if 'HEADERS' in tablaVal:
            temphead = tablaVal['HEADERS']
            valueReturn = temphead.keys()
            listaFinal=[]
            for i in valueReturn:
                listaFinal.append(ponerenFun(i))
            return listaFinal
        else:
            raise CarbineException("No HEADERS for this page")
    else:
        raise CarbineException("Problema interno")
     
     
def impl_setHeaderValue(args):
    if len(args) != 2:
        raise CarbineException("Numero incorrecto de argumentos")
    elif isinstance(args[0],str) and isinstance(args[1],str):
        args[0]=quitar(args[0])
        args[1]=quitar(args[1])
        tempsethead= args[0]+':'+args[1]
        return tempsethead
    else:
        raise CarbineException("parametros deben ser strings, recibidos: %s (%s) y %s (%s)" %(args[0],type(args[0]),args[1],type(args[1])))
    
def recibo(session_dict):
	global session_dict2
	session_dict2=session_dict


def impl_getSessionValue(args):
        if len(args) != 2:
                raise CarbineException("Numero incorrecto de argumentos")
        elif (isinstance(args[0], str) and isinstance(args[1], str)):
                get_session_value(args[0], args[1])
        else:
                raise CarbineException("Parametros deben ser strings, recibidos: %s (%s) y %s (%s)" %(args[0],type(args[0]),args[1],type(args[1])))

def impl_setSessionValue(args):
        if len(args) != 3:
                raise CarbineException("Numero incorrecto de argumentos")
        elif (isinstance(args[0], str) and isinstance(args[1], str) and (isinstance(args[2], str) or isinstance(args[2], list) or isinstance(args[2], int))):
                get_session_value(args[0], args[1])
        else:
                raise CarbineException("Tipos de parametros incorrectos. Recibidos: %s (%s), %s (%s) y %s (%s)" %(args[0],type(args[0]),args[1],type(args[1]), args[2], type(args[2])))
