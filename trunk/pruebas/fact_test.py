# File: factorial_test.py

import sys
from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException
from StringIO import StringIO
from carbine import CarbineException
from carbine_interpreter import *

class CarbineFactorialPLYTetsCase(TestCase):
	global source
	source = '''
            @@ Factorial
            var fact,numerito
            func fac (x)
                    var cont is 1
                    if x >= 0 then
                            whila x > 0 then
                                    cont is cont*x
                                    x is (x-1)
                            end
                    end
                    return cont
            end
            numerito is 3
            fact is summon fac(numerito)
            write "El factorial de " ; numerito ; " es " ; fact
            '''
	def setUp(self):
		self.output = StringIO()
		sys.stdout = self.output

	def tearDown(self):
        	self.output.close()
        	sys.stdout = sys.__stdout__
	
	
    	def testFact(self):
        	"Test Factorial"
        	self.assertEquals(parse(source),
                	     [['var', 'fact', 'numerito'], 
			     [['func', 'fac', ['x'], 
			     	[['var', ['is', 'cont', 1]],
			      	['if', ['>=', 'x', 0], 
			      		[['whila', ['>', 'x', 0], 
			      			[['is', 'cont', ['*', 'cont', 'x']], 
						['is', 'x', ['-', 'x', 1]]]]]], 
			      	['return', 'cont']]], ['is', 'numerito', 3], 
			      ['is', 'fact', ['summon', 'fac', ['numerito']]], 
			      ['write', [';', '"El factorial de "', 'numerito', ';', '" es "', ';', 'fact']]]]
			      )
	def testFunfact(self):
		'prueba de fun fact'
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '"El factorial de 3 es 6"\n')



def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbineFactorialPLYTetsCase))
    
if __name__ == '__main__':
    run_test()

