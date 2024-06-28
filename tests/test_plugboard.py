import unittest
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enigma.plugboard import Plugboard

class TestPlugboard(unittest.TestCase):

    def setUp(self):
        """
        Set up a plugboard instance for testing with sample wiring.
        """
        wiring_pairs = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')]
        self.plugboard = Plugboard(wiring_pairs)

    def test_initialization(self):
        """
        Test if the plugboard is initialized correctly.
        """
        expected_wiring = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', 'E': 'F', 'F': 'E', 'G': 'H', 'H': 'G', 'I': 'J', 'J': 'I'}
        self.assertEqual(self.plugboard.wiring, expected_wiring)

    def test_swap(self):
        """
        Test swapping of characters.
        """
        test_cases = {
            'A': 'B',
            'B': 'A',
            'C': 'D',
            'D': 'C',
            'E': 'F',
            'F': 'E',
            'G': 'H',
            'H': 'G',
            'I': 'J',
            'J': 'I',
            'K': 'K'  # No swap exists
        }

        for input_char, expected_output in test_cases.items():
            with self.subTest(input_char=input_char, expected_output=expected_output):
                self.assertEqual(self.plugboard.swap(input_char), expected_output)

if __name__ == '__main__':
    unittest.main()