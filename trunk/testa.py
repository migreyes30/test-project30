import carbine
import carbine_interpreter
from types import *
from carbine import CarbineException,parse,CarbineExceptionCiclo
from carbine_interpreter import *
reload(carbine)
reload(carbine_interpreter)
reload(carbine)
reload(carbine_interpreter)

table={'z':5,'r':4,'w':[1,2,3,4,5,6],'x':'"hola"','y':[4,2,3,1,5,6]}
rr=(ii*ii for ii in xrange(100))
tt=[ij*ij for ij in [3,8,-1,7] if ij < 8]

#---------------------------------------------------------------------------
lst=[[1,2]]
typelst=tipoenlst(lst)
numlst=typelst.count(ListType)

trueparam=len(lst)-numlst
#print trueparam

                    

                
def obtenerChar(cadena):
    if '%' in cadena:
        posChar=cadena.find('%')
        y=cadena[posChar:posChar+3]
        temp=eval(y.replace('%','0x'))
        x=chr(temp)
        if temp != 39 and temp != 34:
            cadena=cadena.replace(y,x)
        else:
            cadena=cadena.replace(y,'')
        return obtenerChar(cadena)
    else:
        return cadena


resultado=obtenerChar('%27hola%22')
##print resultado

print tipoenlst([])
