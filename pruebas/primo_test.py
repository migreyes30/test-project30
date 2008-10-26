
# File: primos_test.py
import sys
from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException
from StringIO import StringIO
from carbine import CarbineException
from carbine_interpreter import *


class CarbinePrimosPLYTetsCase(TestCase):
	
	global source
	source= '''
                        @@elemento mas grande
                        var lst
                        func mas_grande(lst)
                                var accum,i
                                accum is lst[0]
                                for i in lst
                                        if accum < i then
                                                accum is i
                                        end
                                end
                                return accum
                        end

                        var lista is [1,2,5,4,1]
                        write summon mas_grande(lista)
		'''
	
	def setUp(self):
		self.output = StringIO()
		sys.stdout = self.output

	def tearDown(self):
        	self.output.close()
        	sys.stdout = sys.__stdout__


	def testPrimos(self):
		
		"fun elemento mas grande Test"
		
		self.assertEquals(parse(source),
		[['var', 'lst'], 
		[['func', 'mas_grande', ['lst'], 
			[['var', 'accum', 'i'], 
			['is', 'accum', ['lst', 0, 'lst']], 
			['for', 'i', 'lst', 
				[['if', ['<', 'accum', 'i'], 
					[['is', 'accum', 'i']]]]], 
			['return', 'accum']]], 
		['var', ['is', 'lista', [1, 2, 5, 4, 1]]], 
		['write', ['summon', 'mas_grande', ['lista']]]]]
		)
		
		
	def testFunGrande(self):
		'prueba de fun mas grande'
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '5\n')

		
def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbinePrimosPLYTetsCase))
    
if __name__ == '__main__':
    run_test()
