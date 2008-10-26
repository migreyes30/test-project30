from unittest import TestCase, makeSuite, TextTestRunner
import sys
from StringIO import StringIO
from carbine import CarbineException
from carbine_interpreter import *

class CarbineInterpretTetsCase(TestCase):
	def setUp(self):
		self.output = StringIO()
		sys.stdout = self.output

	def tearDown(self):
        	self.output.close()
        	sys.stdout = sys.__stdout__

	def testCreateTable(self):
		'prueba de creacion de tabla de variables'
		self.assertEquals(create_table([]), {
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames
		}
		)
		self.assertEquals(create_table(['var','x']), {
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'x':0})
		self.assertEquals(create_table(['var',['is','x',[1,2]]]), {
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'x':[1,2]})
		self.assertEquals(create_table(['var',['is','x','"hola"']]), {
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'x':'"hola"'})
		self.assertEquals(create_table(['var',['is','x',4]]), {
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'x':4})
		self.assertEquals(create_table(['var','one', 'Two', 'THREE']),{
		'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'one':0, 'Two':0, 'THREE':0})
		self.assertEquals(create_table(['var',['is','one',1], ['is','Two',2], ['is','THREE',3]]),{
				'isletra' : impl_isletra,
		'isnum' : impl_isnum,
		'len' : impl_len,
		'islower' : impl_islower,
		'isupper' : impl_isupper,
		'isspace' : impl_isspace,
		'upper' : impl_upper,
		'lower' : impl_lower,
		'append' : impl_append,
		'insert' : impl_insert,
		'remove' : impl_remove,
		'sort' : impl_sort,
		'reverse' : impl_reverse,
		'pop' : impl_pop,
		'num' : impl_num,
		'str' : impl_str,
		'list' : impl_list,
		'endswith' : impl_endswith,
		'startswith' : impl_startswith,
		'split' : impl_split,
		'strip' : impl_strip,
		'find' : impl_find,
		'root' : impl_raiz,
		'range': impl_range,
		'forward': impl_forward,
		'get_parameter_value': impl_getParamVal,
		'get_parameter_values': impl_getParamVals,
		'get_parameter_names': impl_getParamNames,
		'one':1, 'Two':2, 'THREE':3})
		self.assertRaises(CarbineException, create_table, ['var','x', 'x'])
		self.assertRaises(CarbineException, create_table, ['var',['is','x',4],'x'])
		self.assertRaises(CarbineException, create_table, ['var',['is','x',4],['is','x',4]])
		self.assertRaises(CarbineException,create_table,['var','one', 'Two', 'THREE', 'four', 'Two', 'five'])

	def testEvalExpr(self):
		'pruebas de evualiacion de expresiones'
		table = {'x':10, 'y': -5,'w': 2,'j':1}
		self.assertEquals(eval_expr(table, 5), 5)
		self.assertEquals(eval_expr(table, 'x'), 10)
		self.assertRaises(CarbineException, eval_expr, table, 'omega')
		self.assertEquals(eval_expr(table, ['-', 'x']), -10)
		self.assertEquals(eval_expr(table, ['-', 'y']), 5)
		self.assertEquals(eval_expr(table, ['-', ['-', 'y']]), -5)
		self.assertEquals(eval_expr(table, ['<', 1, 'y']), 0)
		self.assertEquals(eval_expr(table, ['>', 1, 'y']), 1)
		self.assertEquals(eval_expr(table, ['<', 'x', 1]), 0)
		self.assertEquals(eval_expr(table, ['<=', 'x', 1]), 0)
		self.assertEquals(eval_expr(table, ['>', 'x', 1]), 1)
		self.assertEquals(eval_expr(table, ['>=', 'x', 1]), 1)
		self.assertEquals(eval_expr(table, ['<=', 'x', 10]), 1)
		self.assertEquals(eval_expr(table, ['>=', 'x', 10]), 1)
		self.assertEquals(eval_expr(table, ['+', 'x', 'y']), 5)
		self.assertEquals(eval_expr(table, ['-', 'w', 'j']), 1)
		self.assertEquals(eval_expr(table, ['+', 'x', 'y']), 5)
		self.assertEquals(eval_expr(table, ['+', 'x', ['-', 'y']]), 15)
		self.assertEquals(eval_expr(table, ['*', 'x', 'y']), -50)
		self.assertEquals(eval_expr(table, ['/', 'x', 'y']), -2)
		self.assertEquals(eval_expr(table, ['%', 'x', 'y']), 0)
		self.assertEquals(eval_expr(table, ['^', 'x', 2]), 100)
		self.assertEquals(eval_expr(table, ['*', 'x', ['-', 'y']]), 50)
		self.assertEquals(eval_expr(table, ['/', 'x', ['-', 'y']]), 2)
		self.assertEquals(eval_expr(table, ['/', 'x', ['-', 3]]), -4)
		self.assertEquals(eval_expr(table, ['%', 'x', ['-', 'y']]), 0)
		self.assertEquals(eval_expr(table, ['/', 1, ['-', 2]]), -1)
		self.assertEquals(eval_expr(table,['&&', ['>', 'x', 2], ['<', 'y', 1]]), 1)
		self.assertEquals(eval_expr(table,['||', ['>', 'x', 2], ['>', 'y', 1]]), 1)
		self.assertEquals(eval_expr(table,['siis', 'x', 10]),1)
		self.assertEquals(eval_expr(table,['siis', 'x', 3]),0)
		self.assertEquals(eval_expr(table,['nois', 'y', 10]),1)
		self.assertEquals(eval_expr(table,['nois', 'y', -5]),0)
		self.assertEquals(eval_expr(table,['+', ['+', 1, ['*', ['*', 2, 3], 4]], 5]),30)
		self.assertEquals(eval_expr(table,['/', ['+', ['*', ['^', 2, 3], 2], 2], 2]),9)
		self.assertRaises(CarbineException,eval_expr, table,['*', 'x', ['-', 'omega']])
	
	def testExecuteWrite(self):
		'prueba de write'
		table = {'x':10, 'y': 3, 'z':[1,2,3],'w': 2,'j':1}
		execute_write(table, [5])
		execute_write(table, [['+', 'x', 100]])
		execute_write(table, [['-', 'x']])
		execute_write(table, [['<', 'x', 'y']])
		execute_write(table,[['siis', 'x', 10]])
		execute_write(table,[['^', ['+', ['+', 'x', 3], 4], 2]])
		execute_write(table,[['+', ['+', 'x', 3], ['^', 4, 2]]])
		execute_write(table, ['x'])
		execute_write(table, ['"hola"'])
		execute_write(table, ['z'])
		execute_write(table,[['is','x', 2]])
		execute_write(table,[[1, 2]])
		execute_write(table, [['-', 'w', 'j']])
		self.assertRaises(CarbineException,execute_write,table, ['k'])
		self.assertEquals(self.output.getvalue(), '5\n110\n-10\n0\n1\n289\n29\n10\n"hola"\n[1, 2, 3]\n2\n[1, 2]\n1\n')

	def testExecuteIf(self):
		'prueba de enunciado if'
		table = {'x':10, 'y': 3}
		execute_if(table, [5, [['write', 1]]])
		execute_if(table, [3, [['write', 1]]])
		execute_if(table, ['d', [['write', 1]]])
		execute_if(table, ['"cadena"', [['write', 1]]])
		execute_if(table, [[1,2], [['write', 1]]])
		execute_if(table, [['>', 'x', 'y'], [['write', 100]]])
		execute_if(table, [['<', 'x', 'y'], [['write', 100]]])
		execute_if(table, [['siis', 'x', 10], [['write', ['+', 'x', 1]]]])
		self.assertRaises(CarbineException,execute_if,table, [['is','x', 2], [['write', 1]]])
        	self.assertEquals(self.output.getvalue(), '1\n1\n1\n1\n1\n100\n11\n')

	def testExecuteElse(self):
		'prueba de else'
		table = {'x':10, 'y': 3,'z' : 0}
		execute_else(table,[[['write',10]]])
		execute_else(table,[[['write',['is','x', 17]]]])
		execute_else(table,[[['if', ['siis', 'z', 0], [['is', 'z', 10], ['write', 'z']]]]])
		execute_else(table,[[['if', ['siis', 'z', 10], [['is', 'z', 20], ['write', '"hola"']]]]])
		execute_else(table,[[['write',['is','x', 19]],['write',['is','y', 4]]]])
		execute_else(table,[[['write', 'x'], ['write', 'y']], 'else', [['is', 'x', ['+', 'x', 1]], ['write', 'x']]])
		self.assertEquals(self.output.getvalue(), '10\n17\n10\n"hola"\n19\n4\n19\n4\n20\n')

	def testExecuteIfElse(self):
		'prueba de if con else'
		table = {'x':10, 'y': 3,'z' : 0}
		execute_if(table, [['<', 'x', 'y'], [['write', 1]],'else',[['write',10]]])
		self.assertEquals(self.output.getvalue(), '10\n')
		
	def testExecuteIs(self):
		'prueba de is'
		table = {'x':2, 'y': 5,'w':3}
		table2 = {'x':0, 'y': 6,'w':[1,2]}
		execute_is(table, ['x', 100])
		execute_write(table, ['x'])
		execute_is(table, ['x', ['+', 'x', 'y']])
		execute_write(table, ['x'])
		execute_is(table, ['y', ['*', 'x', 5]])
		execute_write(table, ['y'])
		execute_is(table, ['y', ['%', 'x', 'y']])
		execute_write(table, ['y'])
		execute_is(table, ['y','"hola"'])
		execute_write(table, ['y'])
		execute_is(table,['x', ['is', 'y', 5]])
		execute_write(table, ['x'])
		execute_is(table,['x', 'y'])
		execute_write(table, ['x'])
		execute_write(table, ['y'])
		execute_is(table,['w',[1,2]])
		execute_write(table, ['x'])
		execute_write(table, ['y'])		
		execute_write(table, ['w'])
		execute_is(table2,['w',3])
		execute_write(table2, ['w'])
		self.assertEquals(self.output.getvalue(), '100\n105\n525\n105\n"hola"\n5\n5\n5\n5\n5\n[1, 2]\n3\n')
		self.assertRaises(CarbineException,execute_is,table, ['z',3])
		
	def testExecuteVar(self):
		'prueba de var'
		table = {'x':2, 'y': 5}
		self.assertEquals(execute_var(table,['z']), {'x':2, 'y': 5, 'z': 0})
		self.assertEquals(execute_var(table,['r']), {'x':2, 'y': 5, 'r': 0, 'z': 0})
		self.assertEquals(execute_var(table,[['is','t',10]]), {'x':2, 'y': 5, 'r': 0, 'z': 0, 't':10})
		self.assertEquals(execute_var(table,[['is','a',10],['is','c',20]]), {'x':2, 'y': 5, 'r': 0, 'z': 0, 't':10,'a':10,'c':20})
		self.assertEquals(execute_var(table,['o','v']), {'x':2, 'y': 5, 'r': 0, 'z': 0, 't':10,'a':10,'c':20,'o':0,'v':0})
		self.assertRaises(CarbineException,execute_var,table, [['is','x',10]])
		self.assertRaises(CarbineException,execute_var,table, [['is','t',10]])
		
	def testExecutewhila(self):
		'prueba whila'
		table = {'x':0, 'y': 0}
		execute_whila(table,[['<', 'x', 3], [['is', 'x', ['+', 'x', 1]],['write', 'x']]])
		execute_whila(table,[['<', 'y', 10], [['is', 'y', ['+', 'y', 2]], ['write', 'y']]])
		execute_whila(table,[['nois', 'y', 0], [['is', 'y', ['-', 'y', 2]], ['write', 'y']]])
		self.assertEquals(self.output.getvalue(), '1\n2\n3\n2\n4\n6\n8\n10\n8\n6\n4\n2\n0\n')
	
	def testExecuteFunlist(self):
		'prueba de funlist'
		table={'z':5,'y':4,'x':[1,2,3,4,5,6]}
		rr=['[', ':', 2, ']', 'x']
		mm=['[', 1,':', ']', 'x']
		hh=['[', ':', 2, ']', 'u']
		ss=[ '[', 1, ':', 2, ']', 'z']
		ll=['[',1, ':',3, ']', 'x']
		jj=['[', ']', 'x']
		l=['[',1, ':','y', ']', 'x']
		s=['[',0, ':',['+','y',1], ']', 'x']
		self.assertEquals(execute_funlist(table,rr),[1,2])
		self.assertEquals(execute_funlist(table,mm),[2,3,4,5,6])
		self.assertEquals(execute_funlist(table,ll),[2,3])
		self.assertEquals(execute_funlist(table,jj),[1,2,3,4,5,6])
		self.assertRaises(CarbineException,execute_funlist,table,hh)
		self.assertRaises(CarbineException,execute_funlist,table,ss)
		self.assertEquals(execute_funlist(table,l),[2,3,4])
		self.assertEquals(execute_funlist(table,s),[1,2,3,4,5])
		execute_write(table,[['funlist', '[', ':', 2, ']', 'x']])
		self.assertEquals(self.output.getvalue(), '[1, 2]\n')
		
	def testExecutelst(self):
		'prueba de lst'
		table={'z':5,'y':4,'x':[1,2,3,4,5,6]}
		self.assertEquals(execute_lst(table,[ 3, 'x']),4)
		self.assertEquals(execute_lst(table,[ 0, 'x']),1)
		self.assertEquals(execute_lst(table,[ ['-',1], 'x']),6)
		execute_is(table,[['lst', 0, 'x'], 0])
		execute_write(table, ['x'])
		execute_is(table,[['lst', 0, 'x'],['+','z','y']])
		execute_write(table, ['x'])
		execute_is(table,[['lst', 1, 'x'],['is','z','y']])
		execute_write(table, ['x'])
		self.assertEquals(self.output.getvalue(), '[0, 2, 3, 4, 5, 6]\n[9, 2, 3, 4, 5, 6]\n[9, 4, 3, 4, 5, 6]\n')
		
	def testExecuteBreak(self):
		
		'prueba de break '
		#'break'
		table={'x':1,'y':4}
		table2={'x':1,'y':4}
		execute_whila(table,[['<', 'x', 8], [['write', 'x'], ['if', ['siis', 'x', 5], [['break']]],['is','x',['+','x',1]]]])
		execute_whila(table2,[['<', 'x', 8], [['if', ['siis', 'x', 3], [['break']]],['write', 'x'], ['is', 'x', ['+', 'x', 1]]]])
		self.assertEquals(self.output.getvalue(), '1\n2\n3\n4\n5\n1\n2\n')
	
	def testExecuteReturn(self):
		'prueba de return'
		table={'x':1,'y':4,'z':[1,2,3,4,5,6]}
		self.assertRaises(CarbineException,execute_return,table,['"hola"'])
		self.assertRaises(CarbineException,execute_return,table,[2])
		self.assertRaises(CarbineException,execute_return,table,[[1,2]])
		self.assertRaises(CarbineException,execute_return,table,['y'])
		self.assertRaises(CarbineException,execute_return,table,['+',1,3])
		self.assertRaises(CarbineException,execute_return,table,['/','x','y'])
		self.assertRaises(CarbineException,execute_return,table,['funlist', '[', 1,':', ']', 'z'])
		self.assertRaises(CarbineException,execute_return,table,['lst', 1, 'z'])

		
	def testExecutefor(self):
		'prueba for'
		table = {'x':0, 'y': [1,2,3],'z':0,'w':'"hola"'}
		execute_for(table,['x', 'y', [['write', 'x']]])
		execute_for(table,['z', '"cadena"', [['write', 'z']]])
		execute_for(table,['z', ['funlist', '[', 1, ':', ']', 'y'], [['write', 'z']]])
		execute_for(table,['z', [1,2], [['write', 'z']]])
		execute_for(table,['x', 'w', [['write', 'x']]])
		self.assertEquals(self.output.getvalue(), '1\n2\n3\nc\na\nd\ne\nn\na\n2\n3\n1\n2\nh\no\nl\na\n')
	
	def testExecuteConcatenar(self):
		'prueba de concatenar'
		table={'z':5,'y':4,'w':[1,2,3,4,5,6],'x':'"hola"'}
		self.assertRaises(CarbineException,execute_concatenar,table,[1, [1, 2, 3]])
		self.assertRaises(CarbineException,execute_concatenar,table,[1,2])
		self.assertEquals(execute_concatenar(table,['"cadena"', 1]),'"cadena1"')
		self.assertEquals(execute_concatenar(table,['"cadena"', [1, 2, 3]]),'"cadena[1, 2, 3]"')
		self.assertEquals(execute_concatenar(table,['x',[1, 2, 3]]),'"hola[1, 2, 3]"')
		self.assertEquals(execute_concatenar(table,['x', 2]),'"hola2"')
		self.assertEquals(execute_concatenar(table,['x', 'z']),'"hola5"')
		self.assertEquals(execute_concatenar(table,['x','x']),'"holahola"')
		self.assertEquals(execute_concatenar(table,['x','"cadena"']),'"holacadena"')
		self.assertEquals(execute_concatenar(table,['"cadena"','"cadena1"']),'"cadenacadena1"')
		self.assertEquals(execute_concatenar(table,[[1,2], [1,2]]),[1,2,1,2])
		execute_write(table,[[';', 'x', 'w', ';', 'y', ';', 'z']])
		self.assertRaises(CarbineException,execute_write,table,[[';', 'x', 'w', ';', 'y', ';', 'z', ';', 'e']])
		self.assertEquals(self.output.getvalue(), '"hola[1, 2, 3, 4, 5, 6]45"\n')
		
def run_test():
	TextTestRunner(verbosity=2).run(makeSuite(CarbineInterpretTetsCase))
    
if __name__ == '__main__':
	run_test()
