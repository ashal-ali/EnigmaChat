import unittest
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enigma.rotor import Rotor
from enigma.reflector import Reflector
from enigma.plugboard import Plugboard
from enigma.enigmamachine import EnigmaMachine

class TestEnigmaMachine(unittest.TestCase):

    def setUp(self):
        """
        Set up the EnigmaMachine instance for testing.
        """
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)
        reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        plugboard = Plugboard([('A', 'B'), ('C', 'D')])
        
        self.enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
        self.initial_positions = [0, 0, 0]

    def test_initialization(self):
        """
        Test if the EnigmaMachine is initialized correctly.
        """
        self.assertEqual(len(self.enigma.rotors), 3)
        self.assertIsInstance(self.enigma.reflector, Reflector)
        self.assertIsInstance(self.enigma.plugboard, Plugboard)
        self.assertIsNone(self.enigma.initial_positions)

    def test_set_rotor_positions(self):
        """
        Test setting the initial rotor positions.
        """
        self.enigma.set_rotor_positions(self.initial_positions)
        self.assertEqual(self.enigma.initial_positions, self.initial_positions)
        for rotor, position in zip(self.enigma.rotors, self.initial_positions):
            self.assertEqual(rotor.position, position)

    def test_reset_rotor_positions(self):
        """
        Test resetting the rotor positions to initial positions.
        """
        self.enigma.set_rotor_positions(self.initial_positions)
        self.enigma.set_rotor_positions([1, 2, 3])

        # Debugging: Print rotor positions before reset
        print("Rotor positions before reset:", [rotor.position for rotor in self.enigma.rotors])

        self.enigma.reset_rotor_positions()

        # Debugging: Print rotor positions after reset
        print("Rotor positions after reset:", [rotor.position for rotor in self.enigma.rotors])

        for rotor, position in zip(self.enigma.rotors, self.initial_positions):
            self.assertEqual(rotor.position, position)

    def test_encrypt_decrypt(self):
        """
        Test encryption and decryption process.
        """
        message = "HELLO"
        self.enigma.set_rotor_positions(self.initial_positions)
        encrypted_message = self.enigma.encrypt(message)
        
        self.enigma.reset_rotor_positions()
        decrypted_message = self.enigma.encrypt(encrypted_message)

        self.assertEqual(decrypted_message, message)

if __name__ == '__main__':
    unittest.main()



