import unittest
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enigma.rotor import Rotor

class TestRotor(unittest.TestCase):

    def setUp(self):
        """
        Set up a rotor instance for testing.
        """
        self.wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.notch = 17
        self.rotor = Rotor(self.wiring, self.notch)

    def test_initialization(self):
        """
        Test if the rotor is initialized correctly.
        """
        self.assertEqual(self.rotor.wiring, self.wiring)
        self.assertEqual(self.rotor.notch, self.notch)
        self.assertEqual(self.rotor.position, 0)

    def test_step(self):
        """
        Test if the rotor steps correctly.
        """
        self.rotor.position = 16  # Set position just before the notch
        stepped = self.rotor.step()
        self.assertEqual(self.rotor.position, 17)
        self.assertTrue(stepped)

        stepped = self.rotor.step()
        self.assertEqual(self.rotor.position, 18)
        self.assertFalse(stepped)

    def test_encode_forward(self):
        """
        Test forward encoding of a character.
        """
        self.rotor.position = 0
        encoded_char = self.rotor.encode('A')
        self.assertEqual(encoded_char, 'E')

        self.rotor.position = 1
        encoded_char = self.rotor.encode('A')
        self.assertEqual(encoded_char, 'J')  # Updated expected value

    def test_encode_reverse(self):
        """
        Test reverse encoding of a character.
        """
        self.rotor.position = 0
        encoded_char = self.rotor.reverse_encode('E')
        self.assertEqual(encoded_char, 'A')

        self.rotor.position = 1
        encoded_char = self.rotor.reverse_encode('J')
        self.assertEqual(encoded_char, 'A')  # Updated expected value

if __name__ == '__main__':
    unittest.main()
