from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException

class CarbinePLYTetsCase(TestCase):
	
    def testEmpty(self):
        "empty test"
        self.assertEquals(parse(' '), [[],[]])
        
    def testVars(self):
        "var test"
        self.assertEquals(parse('var x'), [['var','x'],[]])
	self.assertEquals(parse('var bla1, bla2'),[['var','bla1', 'bla2'], []])
	self.assertEquals(parse('var a, b, c, f'),[['var','a', 'b','c','f'], []])
	self.assertRaises(CarbineException,parse,'var x y')

    def testPrint(self):
        "print test"
        self.assertEquals(parse('write 10'), [[], [['write', 10]]])
       	self.assertEquals(parse('write a + 1'), [[], [['write', ['+', 'a', 1]]]])
        self.assertRaises(CarbineException, parse, 'write (x + 1')
	self.assertRaises(CarbineException, parse, 'print (x + 1)')
	
    def testAsignacion(self):
	"assign test"
	self.assertEquals(parse('x is 12'),[[],[['is','x',12]]])
	self.assertEquals(parse('x is y'), [[], [['is', 'x', 'y']]])
	self.assertEquals(parse('x is (1+3)'),[[], [['is', 'x', ['+', 1, 3]]]])
	self.assertEquals(parse('y is 3+2*(9+1)'),[[], [['is', 'y', ['+', 3, ['*', 2, ['+', 9, 1]]]]]])
	self.assertRaises(CarbineException,parse,'x = 5')

    
    def testIf(self):
        "if test"
        self.assertEquals(parse('if x then end'), [[], [['if', 'x', []]]])
        self.assertEquals(parse('if x < 5 then x is 10 end'), [[], [['if', ['<', 'x', 5], [['is', 'x', 10]]]]])
	self.assertEquals(parse('if x siis 1 then write x end'),[[], [['if', ['siis', 'x', 1], [['write', 'x']]]]])
        self.assertRaises(CarbineException, parse, 'if x < 5 y is 1 end')
   
    def testWhila(self):
	"whila test"
	self.assertEquals(parse('whila x then end'),[[],[['whila','x',[]]]])
	self.assertEquals(parse('whila x > 5 then write 10 end'),[[], [['whila', ['>', 'x', 5], [['write', 10]]]]])
	self.assertEquals(parse('whila x siis 5 then write 10 end'), [[], [['whila', ['siis', 'x', 5], [['write', 10]]]]])
	self.assertEquals(parse('whila x >= 1 then x is x + 1 end'),[[], [['whila', ['>=', 'x', 1], [['is', 'x', ['+', 'x', 1]]]]]])
	self.assertEquals(parse('whila x >= 1 then x is x + 1 if x % 2 siis 0 then write x end end'),
	[[], [['whila', ['>=', 'x', 1], [['is', 'x', ['+', 'x', 1]], ['if', ['siis', ['%', 'x', 2], 0], [['write', 'x']]]]]]])
	self.assertRaises(CarbineException, parse, 'whila x < 5 y is 1 end')

    def testElse(self):
	"else test"
	self.assertEquals(parse('if (x>5) then end else end'),[[],[['if',['>','x',5],[],'else',[]]]])
	self.assertEquals(parse('if x nois 2 then write x end else write "hola"end'),
	[[], [['if', ['nois', 'x', 2], [['write', 'x']], 'else', [['write', '"hola"']]]]])
	self.assertEquals(parse('if x nois 2 then write x end else if x siis 3 then write x end end'),
	[[], [['if', ['nois', 'x', 2], [['write', 'x']], 'else', [['if', ['siis', 'x', 3], [['write', 'x']]]]]]])
	self.assertRaises(CarbineException, parse, 'else x < 5 y is 1 end')


    def testSummonFunc(self):
	"summon and func test"
	self.assertEquals(parse('func x(y,x,t) write "hola ";1;2;3 end'),
	[[], [['func', 'x', ['y', 'x', 't'], [['write', [';', '"hola "', 1, ';', 2, ';', 3]]]]]])
	self.assertEquals(parse('var d is 3 func hi(d,x) write "hola ";x end'),
	[['var', ['is', 'd', 3]], [['func', 'hi', ['d', 'x'], [['write', [';', '"hola "', 'x']]]]]])
	self.assertEquals(parse('var d is 3 func fun(d) var x is 2 end'),
	[['var', ['is', 'd', 3]], [['func', 'fun', ['d'], [['var', ['is', 'x', 2]]]]]])

    def testLista(self):
	"list test"
	self.assertEquals(parse('write x[-3:]'),[[], [['write', ['funlist', '[', ['-', 3], ':', ']', 'x']]]])
	self.assertEquals(parse('write x[3:4]'),[[], [['write', ['funlist', '[', 3, ':', 4, ']', 'x']]]])
	self.assertEquals(parse('write x[3:]'),[[], [['write', ['funlist', '[', 3, ':', ']', 'x']]]])



def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbinePLYTetsCase))
    
if __name__ == '__main__':
    run_test()
