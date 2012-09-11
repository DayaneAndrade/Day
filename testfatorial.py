import unittest
from fatorial import fatorial

class TestFatorial(unittest.TestCase):

	def test_deveria_calcular_o_fatorial_de_1_corretamente(self):
		self.assertEqual(fatorial(1),1)
	
	def test_deveria_calcular_o_fatorial_de_2_corretamente(self):
		self.assertEqual(fatorial(2),2)
	
	def test_deveria_calcular_o_fatorial_de_5_corretamente(self):
		self.assertEqual(fatorial(5),120)
	
	def test_deveria_calcular_o_fatorial_de_6_corretamente(self):
		self.assertEqual(fatorial(6),720)

	def test_deveria_calcular_o_fatorial_de_10_corretamente(self):
		self.assertEqual(fatorial(10),3628800)

unittest.main()