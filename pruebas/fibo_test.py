# File: fibonacci_test.py

import sys
from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException
from StringIO import StringIO
from carbine import CarbineException
from carbine_interpreter import *


class CarbineFibonacciPLYTetsCase(TestCase):
	
	global source
	source = '''
		@@ Fibonacci
		func fibonacci(x)
			var fibo is x,
			contador is 0, 
			a is 1,
			b is 1,
			c,
			resultado is [1,2,3,4,5,6]
			
			if ((fibo siis 1) || (fibo siis 2)) then
				resultado[0] is  1
				contador is contador + 1
			end
			if ((fibo nois 1) || (fibo nois 2)) then
				whila (fibo > 2) then
					a is b
					b is c
					c is (a + b)
					fibo is (fibo-1)
					resultado[0] is  c
					contador is contador + 1
				end
			end
			
			return [resultado,contador]
		end
                var x is 7,l
                l is summon fibonacci(x)
		write l
        	'''
	
	def setUp(self):
		self.output = StringIO()
		sys.stdout = self.output

	def tearDown(self):
        	self.output.close()
        	sys.stdout = sys.__stdout__
		
	def testFibo(self):
        	"Test Fibonacci"
		self.assertEquals(parse(source),
		[[], [['func', 'fibonacci', ['x'], 
		[['var', ['is', 'fibo', 'x'], ['is', 'contador', 0], ['is', 'a', 1], ['is', 'b', 1], 'c', 
		['is', 'resultado', [1, 2, 3, 4, 5, 6]]], 
		['if', ['||', ['siis', 'fibo', 1], ['siis', 'fibo', 2]], 
		[['is', ['lst', 0, 'resultado'], 1], ['is', 'contador', ['+', 'contador', 1]]]], 
		['if', ['||', ['nois', 'fibo', 1], ['nois', 'fibo', 2]], 
		[['whila', ['>', 'fibo', 2], 
		[['is', 'a', 'b'], ['is', 'b', 'c'], ['is', 'c', ['+', 'a', 'b']], 
		['is', 'fibo', ['-', 'fibo', 1]], ['is', ['lst', 0, 'resultado'], 'c'], 
		['is', 'contador', ['+', 'contador', 1]]]]]], 
		['return', ['resultado', 'contador']]]], 
		['var', ['is', 'x', 7], 'l'], ['is', 'l', ['summon', 'fibonacci', ['x']]], ['write', 'l']]]
	    	)
	    
	    
	def testFunfibo(self):
		'prueba de fun fibo'
		s='''
	func fibo(fibo_de)
		var en is 0,
		a is 1,
		b is 1,
		c is 1,
		resultado is [0,1,2,3,4,5,6,7]
		if(fibo_de <= 0) then
			return "Debes pedir un numero mayor a 0"
		end
		whila(fibo_de >= en) then
			if(en siis 0) then
				resultado[en] is 0
				en is en + 1
			end
			else
				if (en siis 1) || (en siis 2) then
					resultado[en] is 1
					@@write 1
					en is en + 1
				end
				else
					a is b
					b is c
					c is (a+b)
					resultado[en] is c
					@@write c
					en is en + 1
				end
			end
		end
		return resultado
	end
	write summon fibo(7)
		'''
		
		parseo = parse(s)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[0, 1, 1, 2, 3, 5, 8, 13]\n')



def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbineFibonacciPLYTetsCase))
    
if __name__ == '__main__':
    run_test()
