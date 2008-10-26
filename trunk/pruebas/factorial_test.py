# File: factorial_test.py

from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException

class CarbineFactorialPLYTetsCase(TestCase):
    def testFact(self):
        "Test Factorial"
        source = '''
        @@ Factorial

        var i is 3, fact is 1

        if i >= 0 then
            whila i > 0 then
                fact is fact*(i)
                i is (i-1)
            end
        end
        write "El factorial de " ; i ; " es " ; fact

        '''
        self.assertEquals(parse(source),
	[['var',['is', 'i', 3], ['is', 'fact', 1]],
	 [['if', ['>=', 'i', 0], 
	 	[['whila', ['>', 'i', 0], 
			[['is', 'fact', ['*', 'fact', 'i']], 
			['is', 'i', ['-', 'i', 1]]]]]], 
	['write', [';', '"El factorial de "', 'i', ';', '" es "', ';', 'fact']]]]

	)


def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbineFactorialPLYTetsCase))
    
if __name__ == '__main__':
    run_test()
