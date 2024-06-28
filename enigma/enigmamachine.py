class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        """
        Initialize the EnigmaMachine class.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        self.initial_positions = None

    def set_rotor_positions(self, positions):
        """
        Set the initial positions of the rotors and store them.
        """
        if len(positions) != len(self.rotors):
            raise ValueError("Number of positions must match number of rotors")

        if self.initial_positions is None:
            self.initial_positions = positions.copy()  # Store the initial positions only once

        for rotor, position in zip(self.rotors, positions):
            rotor.position = position

    def reset_rotor_positions(self):
        """
        Reset the rotor positions to the initial positions.
        """
        if self.initial_positions is None:
            raise ValueError("Initial positions have not been set.")

        self.set_rotor_positions(self.initial_positions)

    def step_rotors(self):
        """
        Step the rotors in the correct order.
        """
        step_next = self.rotors[-1].step()
        for i in range(len(self.rotors) - 2, -1, -1):
            if step_next:
                step_next = self.rotors[i].step()
            else:
                break

    def encrypt(self, message):
        """
        Encrypt or decrypt a message.
        """
        encrypted_message = []

        for char in message:
            self.step_rotors()
            swapped_char = self.plugboard.swap(char)
            for rotor in reversed(self.rotors):
                swapped_char = rotor.encode(swapped_char)
            reflected_char = self.reflector.reflect(swapped_char)
            for rotor in self.rotors:
                reflected_char = rotor.reverse_encode(reflected_char)
            final_char = self.plugboard.swap(reflected_char)
            encrypted_message.append(final_char)
        return ''.join(encrypted_message)

