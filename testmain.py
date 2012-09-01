import unittest
from main import calculaPingPong

class TestCalculaPingPong(unittest.TestCase):

    def test_deveria_retornar_ping_para_os_numeros_informados(self):
        self.assertEqual(calculaPingPong(3),'ping')	
        self.assertEqual(calculaPingPong(33),'ping')
        self.assertEqual(calculaPingPong(66),'ping')
        self.assertEqual(calculaPingPong(99),'ping')
    
    def test_deveria_retornar_pong_para_os_numeros_informados(self):
        self.assertEqual(calculaPingPong(5),'pong')
        self.assertEqual(calculaPingPong(10),'pong')    
        self.assertEqual(calculaPingPong(50),'pong')
        self.assertEqual(calculaPingPong(80),'pong')
        self.assertEqual(calculaPingPong(100),'pong')

    def test_deveria_retornar_ping_pong_para_os_numeros_informados(self):
        self.assertEqual(calculaPingPong(15),'pingpong')
        self.assertEqual(calculaPingPong(30),'pingpong') 
        self.assertEqual(calculaPingPong(45),'pingpong')
        self.assertEqual(calculaPingPong(60),'pingpong')
        self.assertEqual(calculaPingPong(90),'pingpong')

    def test_deveria_retornar_os_numeros_informados(self):
        self.assertEqual(calculaPingPong(1),1)
        self.assertEqual(calculaPingPong(31),31)  
        self.assertEqual(calculaPingPong(56),56)
        self.assertEqual(calculaPingPong(61),61)
        self.assertEqual(calculaPingPong(98),98)

unittest.main()