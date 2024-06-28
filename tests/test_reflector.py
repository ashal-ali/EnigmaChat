import unittest
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enigma.reflector import Reflector

class TestReflector(unittest.TestCase):

    def setUp(self):
        """
        Set up a reflector instance for testing.
        """
        self.wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.reflector = Reflector(self.wiring)

    def test_initialization(self):
        """
        Test if the reflector is initialized correctly.
        """
        self.assertEqual(self.reflector.wiring, self.wiring)

    def test_reflect(self):
        """
        Test reflection of characters.
        """
        test_cases = {
            'A': 'Y',
            'B': 'R',
            'C': 'U',
            'D': 'H',
            'E': 'Q',
            'F': 'S',
            'G': 'L',
            'H': 'D',
            'I': 'P',
            'J': 'X',
            'K': 'N',
            'L': 'G',
            'M': 'O',
            'N': 'K',
            'O': 'M',
            'P': 'I',
            'Q': 'E',
            'R': 'B',
            'S': 'F',
            'T': 'Z',
            'U': 'C',
            'V': 'W',
            'W': 'V',
            'X': 'J',
            'Y': 'A',
            'Z': 'T'
        }

        for input_char, expected_output in test_cases.items():
            with self.subTest(input_char=input_char, expected_output=expected_output):
                self.assertEqual(self.reflector.reflect(input_char), expected_output)

if __name__ == '__main__':
    unittest.main()