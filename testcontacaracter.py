import unittest
from contacaracter import contaCaracter

class TestContaCaracter(unittest.TestCase):

	def test_deveria_retornar_quantidade_de_caracteres_correto(self):
		self.assertEqual(contaCaracter(lala),{'a': 2, 'l': 2})