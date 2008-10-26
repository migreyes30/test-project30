
# File: primos_test.py

from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException

class CarbinePrimosPLYTetsCase(TestCase):
	
	def testPrimos(self):
		"Prime Test"
		source= '''
		
		@@ Numeros primos
		
		var rango is 10, primo is 1,num is 1, j is 1

		whila(num <= rango) then
    			whila(j<=num^(1/2)) then
        			if(num % j siis 0) && (j nois 1) then
            				primo is 0
					break
				end
        			else
            				j is j +1
        			end
    			end
    			if(primo siis 1) then
        			write "Los numeros primos son";num
   			end
    			else
       				primo is 1
    			end
   			num is num + 1
		end
		
		
		'''
		self.assertEquals(parse(source),
		[['var', ['is', 'rango', 10], ['is', 'primo', 1], ['is', 'num', 1], ['is', 'j', 1]], [['whila', ['<=', 'num', 'rango'], [['whila', ['<=', 'j', ['^', 'num', ['/', 1, 2]]], [['if', ['&&', ['siis', ['%', 'num', 'j'], 0], ['nois', 'j', 1]], [['is', 'primo', 0], ['break']], 'else', [['is', 'j', ['+', 'j', 1]]]]]], ['if', ['siis', 'primo', 1], [['write', [';', '"Los numeros primos son"', 'num']]], 'else', [['is', 'primo', 1]]], ['is', 'num', ['+', 'num', 1]]]]]]
		)
		
def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbinePrimosPLYTetsCase))
    
if __name__ == '__main__':
    run_test()
