class Plugboard: 
    def __init__(self, wiring): 
        """
        Initialize the Plugboard class.
        """
        self.wiring = {} 
        for pair in wiring:
            a, b = pair
            self.wiring[a] = b
            self.wiring[b] = a

    def swap(self, input): 
        """
        Swap the input character with its pair from the plugboard.
        If not found, return the character itself.
        """
        return self.wiring.get(input, input)
