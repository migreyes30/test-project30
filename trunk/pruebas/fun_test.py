import sys
from unittest import TestCase, makeSuite, TextTestRunner
from carbine import parse, CarbineException
from StringIO import StringIO
from carbine import CarbineException
from carbine_interpreter import *

class CarbineFunPLYTetsCase(TestCase):
	
	def setUp(self):
		self.output = StringIO()
		sys.stdout = self.output

	def tearDown(self):
        	self.output.close()
        	sys.stdout = sys.__stdout__
	
	def testFunlen(self):
		'prueba de fun len'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			i is summon len(y)
			write i
			i is summon len([1])
			write i
			i is summon len("hola")
			write i
			i is summon len("hola";"mundo")
			write i
			write summon len(j)
			write summon len("")
			write summon len(summon split(j))
			write summon len(y[1:4])
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '6\n1\n4\n9\n10\n0\n2\n3\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon len(3)
		
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		s1='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		
		write summon len(1+3)
		
		'''
		parseo2 = parse(s)
		table = create_table(parseo2[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo2[1])
		
		s2='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		
		write summon len(y[3])
		
		'''
		parseo3 = parse(s)
		table = create_table(parseo3[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo3[1])
		
	def testFunsort(self):
		'prueba de fun sort'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			u is summon sort(u)
			write u
			i is summon sort([3,1,2])
			write i
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[1, 2, 3, 4, 5, 9]\n[1, 2, 3]\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon sort("hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon sort(3)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
	
	def testFunreverse(self):
		'prueba de fun reverse'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			summon reverse(y)
			write y
			write summon reverse([1,2,3])
			
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[5, 4, 3, 2, 1, 0]\n[3, 2, 1]\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon reverse("hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon reverse(3)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
	
	def testFunpop(self):
		'prueba de fun pop'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			i is summon pop([3,1,2])
			write i
			i is summon pop(y)
			write i
			write y
			summon pop(y,1)
			write y
			summon pop(y,3)
			write y
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '2\n5\n[0, 1, 2, 3, 4]\n[0, 2, 3, 4]\n[0, 2, 3]\n')
		
				
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon pop(j)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon pop(y,6)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon pop(y,"h")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

	def testFunletra(self):
		'prueba de fun isletra'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon isletra(j)
			write summon isletra("5")
			write summon isletra(j)
			write summon isletra("4")
			write summon isletra("[1]")
			write summon isletra("h";"o")
			write summon isletra(summon str("hola"))
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '0\n0\n0\n0\n0\n1\n1\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon isletra(i)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon isletra(y)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

	def testFunnum(self):
		'prueba de fun isnum'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon isnum(j)
			write summon isnum("5")
			write summon isnum("ho6")
			write summon isnum(summon str(4))
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '0\n1\n0\n1\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon isnum([1])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		@@write summon isnum(1+3)
		write summon isnum(6)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon isnum(1+3)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
					
	def testFunlower(self):
		'prueba de fun islower'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon islower(j)
			write summon islower("HOLA")
			write summon islower("hola")
			write summon islower("HOLA";"-TU")
			write summon islower(summon str((summon len(y))))
			
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '1\n0\n1\n0\n0\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon islower([1])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon islower(i)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
	def testFunupper(self):
		'prueba de fun isupper'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon isupper(j)
			write summon isupper("HOLA")
			write summon isupper("hola")
			write summon isupper("HOLA";"-TU")
			write summon isupper(summon str((summon len(y))))
			
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '0\n1\n0\n1\n0\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon isupper([1])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon isupper(i)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
	
	def testFunspace(self):
		'prueba de fun isspace'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon isspace(j)
			write summon isspace("HOLA")
			write summon isspace("hola")
			write summon isspace("HOLA";"-TU")
			write summon isspace(summon str((summon len(y))))
			write summon isspace(" ")
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '0\n0\n0\n0\n0\n1\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon isspace([1])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon isspace(i)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

	def testFuntoup(self):
		'prueba de fun Upper and lower'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon upper(j)
			write summon upper("HOLA")
			write summon lower("HOLA")
			write summon lower(j)
			write summon upper("5";"hola")
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '"HOLA MUNDO"\n"HOLA"\n"hola"\n"hola mundo"\n"5HOLA"\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon upper([1])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon lower(1)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
	def testFunsplit(self):
		'prueba de fun split'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5],k is "hola-mundo-H"
			
			write summon split(j)
			write summon split("hola";" mundo")
			write summon split("hola-mundo","-")
			write summon split(k,"-",1)
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[\'"hola"\', \'"mundo"\']\n[\'"hola"\', \'"mundo"\']\n[\'"hola"\', \'"mundo"\']\n[\'"hola"\', \'"mundo-H"\']\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon split(y)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon split(i)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon split(summon num("3"))
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon split(j,"-","o")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])


	def testFuncast(self):
		'prueba de fun str,list and int'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5], m is "10"
			
			write summon num("9")
			write summon num(m)
			write summon num(i)
			write summon list("hi")
			write summon list("mundo")
			write summon list(j)
			write summon list([1])
			write summon list(summon split(j))
			write summon list(y[1:4])
			write summon str("hola")
			write summon str(3)
			write summon str([1])
			write summon str(summon len(y))
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '9\n10\n0\n[\'"h"\', \'"i"\']\n[\'"m"\', \'"u"\', \'"n"\', \'"d"\', \'"o"\']\n[\'"h"\', \'"o"\', \'"l"\', \'"a"\', \'" "\', \'"m"\', \'"u"\', \'"n"\', \'"d"\', \'"o"\']\n[1]\n[\'"hola"\', \'"mundo"\']\n[1, 2, 3]\n"hola"\n"3"\n"[1]"\n"6"\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon list(1+3)
		
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon list(y[3])
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon list(5)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon num("4hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon num("hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon num(y)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon str(y,3)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

	def testFunappend(self):
		'prueba de fun append'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			summon append(y,200)
			write y
			write summon append([1],200)
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[0, 1, 2, 3, 4, 5, 200]\n[1, 200]\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon append("hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon append(3,4)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

	def testFunremove(self):
		'prueba de fun remove'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			summon remove(y,4)
			write y
			write summon remove([1],1)
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[0, 1, 2, 3, 5]\n[]\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon remove("hi")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon remove(3,4)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
	
	def testFunfind(self):
		'prueba de fun find'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			write summon find(j,"r")
			write summon find(j,"m")
			write summon find(j,"h",1)
			write summon find(j,"h",0)
			write summon find(j," ",1,5)
			write summon find(j," ",1,3)
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '-1\n5\n-1\n0\n4\n-1\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon find(j,4)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon find(y,"4")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon find(j,"h","h")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon find(j,"-","h",5)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
	def testFuninsert(self):
		'prueba de fun insert'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			
			summon insert(y,5,100)
			write y
			write summon insert([1],0,200)
			summon insert(y,6,200)
			write y
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '[0, 1, 2, 3, 4, 100, 5]\n[200, 1]\n[0, 1, 2, 3, 4, 100, 200, 5]\n')
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		summon insert(y,"j",10)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
	def testFunstrip(self):
		'prueba de fun strip'
		source='''
			var i is 0,j is "hmola mundom.", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
			write summon strip(j,"hm.")
			write summon strip(j,"r")
		
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '"ola mundo"\n"hmola mundom."\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		i is summon strip(j,4)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
	def testFunEndStart(self):
		'prueba de fun endswith and startswith'
		source='''
			var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5],m is "10"
			write summon startswith(j,"hola")
			write summon startswith(j,"a")
			write summon endswith(j,"mundo")
			write summon endswith(j,"a")
			write summon startswith(j,m)
			write summon endswith(j,m)
			write summon endswith(j,"o",6)
			write summon endswith(j,"a",6)
			write summon startswith(j,"h",1)
			write summon startswith(j,"m",5)
			write summon startswith(j,"ola",1,5)
			write summon endswith(j,"undo",6,9)
		'''
		parseo = parse(source)
		table = create_table(parseo[0])
        	execute_statements(table,parseo[1])
		self.assertEquals(self.output.getvalue(), '1\n0\n1\n0\n0\n0\n1\n0\n0\n1\n1\n0\n')
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5]
		write summon startswith(j,5)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5],m is "10"
		write summon endswith(5,m)
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])
		
		s='''
		var i is 0,j is "hola mundo", y is [0,1,2,3,4,5],u is [9,3,4,2,1,5],m is "10"
		write summon startswith(j,"h","h")
		'''
		parseo1 = parse(s)
		table = create_table(parseo1[0])
		self.assertRaises(CarbineException,execute_statements,table,parseo1[1])

def run_test():                     
    TextTestRunner(verbosity=2).run(makeSuite(CarbineFunPLYTetsCase))
    
if __name__ == '__main__':
    run_test()