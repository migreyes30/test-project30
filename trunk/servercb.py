import socket
import os.path
from types import *
from carbine_interpreter import *
from carbine import CarbineException
from random import *
import time



CONFIG_VARS= {
    'port': "",
    'root': ""
    }

EXTENSIONES = {
    '.html': 'text/html',
    '.txt' : 'text/plain',
    '.css' : 'text/css',
    '.js'  : 'text/javascript',
    '.jpg': 'image/jpeg',
    '.png': 'image/png',
    '.gif' : 'image/gif'
} 

PAGE404= \
'''HTTP/1.0 404 Not Found
Content-type: text/html
Error-404: Not Found
Host: localhost:7772

<h1>Error 404 Page Not Found</h1>
<p>The page you have requested has not been found</p>
'''

PAGE405= \
'''HTTP/1.0 405 Method Not Allowed
Content-type: text/html
Allow: GET,POST
Host: localhost:7772

<h1>Error 405 Method Not Allowed</h1>
<p>The method you have requested has not been allowed</p>
'''


PAGE500= \
'''HTTP/1.0 500 Internal Server Error
Content-type: text/html
Error-500: Internal Server Error
Host: localhost:7772

<h1>Error 500 Internal Server Error</h1>
<p>Carbine Exception</p>

'''


PAGE600= \
'''HTTP/1.0 600 Internal Browser Error
Content-type: text/html
Error-600: Internal Browser Error
Host: localhost:7772

<h1>Error 600 Internal Browser Error</h1>
<p>Browser Exception</p>

'''

PLANT_ABRIR = '<pc>'
PLANT_CERRAR = '</pc>'

session_dict = {}

### archivo config

def leer_config():
    config_file = "a.txt"
    todo_bien = True
    if (os.path.exists(config_file) and  os.path.isfile(config_file)):
        f = open(config_file, "r")
        config = f.read()
        config = config.replace('\r\n', '\n').split('\n')
        for ind in config:
            a = ind.split(":")
            if CONFIG_VARS.has_key(a[0]):
                a[0] = a[0].strip(" ")
                a[1] = a[1].strip(" ")
                configurar(a[0],a[1])
        print "El puerto configurado es: " + str(CONFIG_VARS['port']) + " la ruta es: ", CONFIG_VARS['root']
    else:
         print "El archivo no existe"
         todo_bien = False
    if todo_bien:
        inicio()



def configurar(llave,valor):
    
    if llave == 'port' and valor.isdigit():
        valor = int(valor)
    
    CONFIG_VARS[llave] = valor

### servidor

def inicio():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', CONFIG_VARS['port']))
    sock.listen(1)

    try:
        while True:        
            print "Esperando conexion..."
            new_sock, address = sock.accept()         
            print "Conectado por:", address            
            procesa_peticion(new_sock)
    finally:
        sock.close()

  
def procesa_peticion(sock):

    try: 
        e = sock.recv(2 ** 20)
        #print "--------\n",e
        entrada = e.replace('\r\n', '\n').strip().split('\n')
        mensajito=genera_respuesta(entrada)
        sock.send(mensajito)
    finally:
        sock.close()
            

def paginaOK(tipo, contenido):
    if hay_cookie == False:
        id_sesion = randomString()
        add_session(id_sesion)
        set_session_value(id_sesion, 'timestamp', time.clock())
        return '\n'.join([
            'HTTP/1.1 200 OK',
            'Content-type: %s' % tipo,'Set-Cookie: id_sesion=%s' % id_sesion]) +'\n\n' + contenido
    else:
        return '\n'.join([
            'HTTP/1.1 200 OK',
            'Content-type: %s' % tipo]) +'\n\n' + contenido


def paginaOKmodif(tipo,contenido,newHead):
	x='\n'.join(newHead)
	
	if hay_cookie == False:
		id_sesion = randomString()
		add_session(id_sesion)
		set_session_value(id_sesion, 'timestamp', time.clock())        
		return '\n'.join([
			'HTTP/1.1 200 OK',
			'Content-type: %s' % tipo,
			'Set-Cookie: id_sesion=%s' % id_sesion])+'\n'+x+'\n\n' + contenido
	else:
		return '\n'.join([
			'HTTP/1.1 200 OK',
			'Content-type: %s' % tipo])+'\n'+x+'\n\n' + contenido

    #if recurso == '/':
    #    recurso = '/index.html'
    #vargtpo=""
    #hay_variables=recurso.find('?')
    #if hay_variables > -1:
        #si hay variables con el metodo get
    #    temp=recurso.split('?')
    #    recurso=temp[0]
    #    vargtpo=temp[1].split('&')     
    #if metodo == 'POST':
        #si hay variables con el metodo post
    #    vargtpo=peticion[-1].split('&')

def obtenerParam(peticion):
    vargtpo=""
    metodo, recurso, protocolo = peticion[0].split()
    hay_variables=recurso.find('?')
    if hay_variables > -1:
            ##si hay variables con el metodo get
            temp=recurso.split('?')
            recurso=temp[0]
            vargtpo=temp[1].split('&')
    if metodo == 'POST':
        ##si hay variables con el metodo post
        vargtpo=peticion[-1].split('&')
    return (vargtpo,recurso)


def genera_respuesta(peticion):
    contenido = ""
    header_params={}
    metodo, recurso, protocolo = peticion[0].split()
    if metodo == 'GET' or metodo == 'POST':
        #Aqui se porcesan las peticiones con metodos get y post
        temp = obtenerParam(peticion)
        vargtpo =temp[0]
        recurso=temp[1]
        if  isinstance(vargtpo,list):
            #procesar las variables si es que hubo un get o post con una forma
            indice = 1
            for i in vargtpo:
                tempvar=i.split('=')
                if len(tempvar)>1:
                    tempvar[1]=obtenerChar(tempvar[1])
                    tempvar[1]=tempvar[1].replace('+',' ')
                    if tempvar[0] not in header_params:
                        header_params[tempvar[0]]=tempvar[1]
                    else:
                        tempValRep=tempvar[0]+"carbineRepeat"+str(indice)
                        tempvar[0]=tempValRep
                        header_params[tempvar[0]]=tempvar[1]
                        indice = indice + 1
                else:
                    print "aki es el error con bombon"
                    return PAGE600
        headers=obtenerHeaders(peticion)
        ruta = CONFIG_VARS['root'] + recurso
        header_paramMethod=(metodo,header_params,headers)

        global hay_cookie
 
        if headers[1].has_key('Cookie'):
            #obtener el nombre de la sesion
            n = headers[1]['Cookie'].split('=')[1]
            try:
                x=tiempo_valido(get_session_value(n, 'timestamp'),30)
            except TypeError:
                x=False
            if(x):
                #actualizar timestamp
                set_session_value(n, 'timestamp', time.clock())
                hay_cookie = True
            else:
                remove_session(n)
                hay_cookie=False 
        else:
            hay_cookie = False

        if os.path.exists(ruta) and os.path.isfile(ruta):
            archivo = file(ruta, 'rb')
            contenido = archivo.read()
            archivo.close()
            if (recurso[recurso.rfind('.'):] == ".pcb"):
                return interpretar_pcb(contenido,False,{},header_paramMethod)
            elif (recurso[recurso.rfind('.'):] == ".cb"):
                return controller(contenido,header_paramMethod)
            else:
                tipo = ctype(recurso)
                return paginaOK(tipo, contenido)
        else:
            return PAGE404
    else:
        return PAGE405
    
def obtenerChar(cadena):
	if '%' in cadena:
		posChar=cadena.find('%')
		y=cadena[posChar:posChar+3]
		temp=eval(y.replace('%','0x'))
		if temp != 39 and temp != 34:
			cadena=cadena.replace(y,chr(temp))
		else:
			cadena=cadena.replace(y,'')
		return obtenerChar(cadena)
	else:
		return cadena


def obtenerHeaders(peticion):
	dicttemp={}
	cabezatemp=peticion.pop(0)
	for i in peticion:
		head=i.split(':',1)
		if len(head)==2:
			dicttemp[head[0]]=head[1]
	dicttemp['metodo']=cabezatemp
	return ('HEADERS',dicttemp)

def ctype(nombre):
        extension = nombre[nombre.rfind('.'):]
        if EXTENSIONES.get(extension) == None:
            return 'text/plain'
        else:
            return EXTENSIONES.get(extension)
        
##controller

def controller(control_file,cabecera):
    try:
        if cabecera[1] == {}:
            respuesta=interpret(control_file)
        else:
            respuesta=interpret(control_file,cabecera)
    except CarbineException,e:
        print e.value
        print "aki es el error con bombon 22222"
        return PAGE500
    else:
        h=respuesta[-1]
        chekHead=tipoenlst(h)
        if 'controladorCarbine' in respuesta:
            ruta = CONFIG_VARS['root']+"/"+respuesta[0]
            if os.path.exists(ruta) and os.path.isfile(ruta):
                archivo = file(ruta, 'rb')
                contenido = archivo.read()
                archivo.close()
                if ListType in chekHead:
                    return interpretar_pcb(contenido,True,respuesta[1],h[0])
                else:
                    return interpretar_pcb(contenido,True,respuesta[1],())
            else:
                return PAGE404 
        else:
            return PAGE500


###plantilla

## Se recibe el archivo con extencion .pcb. (.pcb contiene codigo de carbine y html)
## Se regresa el archivo para ser procesado como .html
        
def interpretar_pcb(archivo_html,flag,tabla,cabeceras):
        archivo_html = archivo_html.replace('\r\n', '\n').split('\n')
        buff = ""
        haypc = False
        respuesta = ""

        ## este for recorre el archivo que se envio, archivo_html es una lista con el contenido del .pcb
        for ind in archivo_html:
            ind = ind.lstrip()  
            ind = ind.rstrip()  
            left = ""
            a = 0
            crb = ""
            right = ""
            b = 0
            ## este if es para no procesar lineas en blanco
            if (ind != ""):
                
                ## se entra a este IF si no estoy procesando codigo de carbine, 
				##es decir si no hay un <pc> sin cerrar
                
                if (haypc == False):
                    a = ind.find(PLANT_ABRIR) 

                    ## este IF entra si encuentra un <pc>
                    if (a > -1):
                        haypc = True
                        left = ind[:a]
                        left = left.rstrip()

                    else:
                    ## este ELSE significa que la linea es 100% html
                        
                        left = ind
                                   

                    ## este IF sirve para no agregar lineas en blanco
                    if (left != ""):
                        buff = buff + 'write "' + left + '"' + ('\n')


                        
                ## este IF entra cuando hay un <pc> que no ha cerrado aun 
                if (haypc):
                    b = ind.find(PLANT_CERRAR) #</pc>
                    ## a este if se entra cuando en la linea esta el </pc>
                    if (b > -1):
                        haypc = False

                        right = ind[b + len(PLANT_CERRAR):]
                        right = right.lstrip()
                        crb = ind[a:b+5]
                        crb = crb.replace(PLANT_ABRIR, "")
                        crb = crb.replace(PLANT_CERRAR, "")

                        crb = crb.rstrip() ## creo que esto no tiene caso
                        crb = crb.lstrip()

                        ## se agrega lineas de crb dentro de esa linea antes del </pc>
                        if (crb != ""):
                                buff = buff + crb + ('\n')
                           
                            
                        ## se agrega lo que esta despues de </pc>
                        if (right != ""):
                                buff = buff + 'write "' + right + '"' + ('\n')                                

                            
                    else:
                        ## este el funciona cuando la linea procesada es 100% codigo de crb
                            buff = buff + ind.replace(PLANT_ABRIR, "") + ('\n') 
                        
        try:
            banderita=False
            if flag == True:
                tempresult = interpret(buff,tabla)
                if isinstance(cabeceras,list):
                    newHead=cabeceras
                    banderita = True
                respuesta =formato(tempresult)
            elif cabeceras[1] != {}:
                tempresult = interpret(buff,cabeceras)
                if isinstance(tempresult[0],list):
                    newHead=tempresult.pop(0)
                    banderita = True
                respuesta =formato(tempresult)
            else:
                tempresult = interpret(buff,cabeceras)
                if isinstance(tempresult[0],list):
                    newHead=tempresult.pop(0)
                    banderita = True
                respuesta =formato(tempresult)
            
            if banderita == False:
                return paginaOK('text/html',respuesta)
            else:
                return paginaOKmodif('text/html',respuesta,newHead)
        except CarbineException,e:
            print e.value
            return PAGE500
        
                
def formato(html):
    buff = ""
    for ind in html:
        ind = ind.lstrip('"')
        ind = ind.rstrip('"')
        buff = buff + ind + '\n'
    return buff
        

#Sesiones

def randomString():
    string=''
    for i in sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789', 15):
        string+=i
    return string

def tiempo_valido(timestamp, tiempo):
	#print "diferencia tiempo = ", time.clock() - timestamp
    #print timestamp, tiempo
    if time.clock() - timestamp < tiempo:
        return True
    else:
        return False

def add_session(id_sesion):
    session_dict[id_sesion] = {}

def remove_session(id_sesion):
    try:
        session_dict.pop(id_sesion)
    except KeyError:
        print "no quite nada"
        pass

def get_session_value(id_sesion, attr):
    try:
        return session_dict[id_sesion][attr]
    except KeyError:
        print "No existe esa sesion/atributo"
        pass

def set_session_value(id_sesion, attr, value):
    envioses(session_dict)
    session_dict[id_sesion][attr] = value

#Manejo de caracteres de escape

def envioses(session_dict):
	recibo(session_dict)

def unescape(text):
	    text = text.replace('$&', '&') \
	               .replace('$<', '<') \
	               .replace('$>', '>') \
	               .replace('$\'', '\'') \
	               .replace('$"', '"')
	    return text

def escape(text):
    text = text.replace('&', '$&') \
               .replace('<', '$<') \
               .replace('>', '$>') \
               .replace('\'', '$\'') \
               .replace('"', '$"')
    return text

#persistencia

def set_persistent(nombre, valor):
        db = MySQLdb.connect("localhost", "root", "jonjon", "carbine")
        cursor = db.cursor()
        get = "select valor from foro where nombre = '" + nombre + "'"
        cursor.execute(get)
        ant = cursor.fetchall()
        if len(ant) > 0:
            print ant[0][0]
            a = eval(ant[0][0])
            if (not isinstance(a[0], list) and not isinstance(a[1], list)):
                a[0] = [a[0],a[1]]
                a.remove(a[1])
            a.append(valor) 
            q = "update foro set valor='"+ MySQLdb.escape_string(str(a)) + "' where nombre='" + nombre + "'"
        else:
            q = "insert into foro values ('" + nombre + "','" + MySQLdb.escape_string(str(valor)) + "')"

        cursor.execute(q)
        db.commit()
        db.close()

def get_persistent(nombre, var):
        db = MySQLdb.connect("localhost", "root", "jonjon", "carbine")
        cursor = db.cursor()
        get = "select valor from foro where nombre = '" + nombre + "'"
        cursor.execute(get)
        result = cursor.fetchall()
        
        if result:
            r = eval(result[0][0])
            
            for e in r:
                if var in e:
                    return e[e.index(var)+1:]
            return None
        else:
            return None

#iniciar ejecucion del servido...
leer_config()

