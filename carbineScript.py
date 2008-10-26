#!/usr/bin/python

import carbine_interpreter
from carbine_interpreter import interpret,CarbineException,CarbineExceptionCiclo
import sys

name=sys.argv[0]
try:
	a=open(sys.argv[1])
	f=a.read()
	interpret(f)
	a.close()
except IndexError:
	raise CarbineException("mal rango")
except IOError:
	raise CarbineException("missing file '%s'",name)
