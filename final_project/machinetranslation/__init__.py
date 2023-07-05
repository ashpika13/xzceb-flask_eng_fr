import unittest
from translator import englishtofrench, frenchtoenglish
        
class Testfrenchtoenglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hi') 
        self.assertNotEqual(frenchtoenglish('Chien'), 'Hello')

class Testenglishtofrench(unittest.TestCase):
    def test2(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtofrench('Goodbye'), 'Bonjour')        

unittest.main()