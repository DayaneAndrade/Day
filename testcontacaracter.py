import unittest
from contacaracter import contaCaracter

class TestContaCaracter(unittest.TestCase):

	def test_deveria_retornar_quantidade_de_caracteres_correto(self):
		self.assertEqual(contaCaracter('lala'),{'a': 2, 'l': 2})
		self.assertEqual(contaCaracter('lele'),{'e': 2, 'l': 2})
		self.assertEqual(contaCaracter('lili'),{'i': 2, 'l': 2})
		self.assertEqual(contaCaracter('lolo'),{'l': 2, 'o': 2})
		self.assertEqual(contaCaracter('ll'),{'l': 2})

unittest.main()