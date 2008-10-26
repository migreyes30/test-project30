# File: fibonacci_test.py

from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException

class CarbineFibonacciPLYTetsCase(TestCase):
    def testFibo(self):
        "Test Fibonacci"
        source = '''
        @@@ Fibonacci

        var fibo is 5,contador is 0,a is  1,b is 1,resultado is 1

        if ((fibo siis 1) || (fibo siis 2)) then
            resultado is 1
        end
        if ((fibo nois 1) || (fibo nois 2)) then
            whila (fibo > 2) then
                a is b
                b is c
                c is (a + b)
                fibo is fibo - 1
            end
        end
        write "El fibonacci pedido es " ; fibo

        '''
        self.assertEquals(parse(source), 
            [['var',['is', 'fibo', 5], ['is', 'contador', 0], ['is', 'a', 1], ['is', 'b', 1], ['is', 'resultado', 1]],
	    [['if', ['||', ['siis', 'fibo', 1], ['siis', 'fibo', 2]], 
	    	[['is', 'resultado', 1]]], 
	    ['if', ['||', ['nois', 'fibo', 1], ['nois', 'fibo', 2]], 
	    	[['whila', ['>', 'fibo', 2], 
			[['is', 'a', 'b'], 
			['is', 'b', 'c'], 
			['is', 'c', ['+', 'a', 'b']], 
			['is', 'fibo', ['-', 'fibo', 1]]]]]], 
	    ['write', [';', '"El fibonacci pedido es "', 'fibo']]]]
	    )

def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbineFibonacciPLYTetsCase))
    
if __name__ == '__main__':
    run_test()
